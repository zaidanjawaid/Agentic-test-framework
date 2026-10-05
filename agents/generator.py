"""Generator agent: give it a goal in plain English. It explores saucedemo.com
in a real browser (observe -> think -> act -> check) and writes a pytest test.

Usage:  python agents/generator.py "A locked-out user should see an error"
Output: tests/test_generated.py  (git-ignored: review it before you keep it!)
"""
import os
import sys
from pathlib import Path

import anthropic
from playwright.sync_api import sync_playwright

client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY
MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")
OUT = Path("tests/test_generated.py")
ALLOWED = "https://www.saucedemo.com"   # guardrail: the only site the agent may visit

PROMPT = """You are a QA automation engineer.
Goal: {goal}

Rules:
- Start at https://www.saucedemo.com
- Call snapshot before every action
- Use role + name from the snapshot
  for click and fill
- When the goal is verified, call
  write_test with ONE pytest-playwright
  test using get_by_role and expect()
- Never use time.sleep()"""


# ---------- tools: the agent's hands ----------
def tool(name, desc, *params):
    props = {p: {"type": "string"} for p in params}
    schema = {"type": "object", "properties": props,
              "required": list(params)}
    return {"name": name, "description": desc,
            "input_schema": schema}


TOOLS = [
    tool("goto", "Open a URL", "url"),
    tool("snapshot", "Read the page's accessibility tree"),
    tool("click", "Click by role + name", "role", "name"),
    tool("fill", "Type text", "role", "name", "text"),
    tool("write_test", "Save test file and stop", "code"),
]


def act(page, name, a):
    if name == "snapshot":
        return page.locator("body").aria_snapshot()
    if name == "goto":
        if not a["url"].startswith(ALLOWED):
            return f"ERROR: only {ALLOWED} may be visited"
        page.goto(a["url"])
    if name in ("click", "fill"):
        el = page.get_by_role(a["role"], name=a["name"])
        el.click() if name == "click" else el.fill(a["text"])
    if name == "write_test":
        OUT.write_text(a["code"])
    return "ok"


# ---------- the agent loop ----------
def generate(goal: str, max_steps: int = 15):
    messages = [{"role": "user", "content": PROMPT.format(goal=goal)}]
    with sync_playwright() as p:
        page = p.chromium.launch(headless=False).new_page()
        page.set_default_timeout(5000)          # fail fast, so the agent can retry
        for step in range(max_steps):           # guardrail: step limit
            reply = client.messages.create(model=MODEL, max_tokens=4000,
                                           tools=TOOLS, messages=messages)
            messages.append({"role": "assistant", "content": reply.content})
            if reply.stop_reason != "tool_use":
                return print(reply.content[0].text if reply.content else "done")
            results = []
            for call in [b for b in reply.content if b.type == "tool_use"]:
                print(f"step {step}: {call.name} {call.input}")
                try:
                    out = act(page, call.name, call.input)
                except Exception as e:
                    out = f"ERROR: {e}"         # the agent sees its own mistakes
                results.append({"type": "tool_result", "tool_use_id": call.id, "content": out})
                if call.name == "write_test":
                    return print(f"saved {OUT}")
            messages.append({"role": "user", "content": results})
        print(f"stopped: hit the {max_steps}-step limit")


if __name__ == "__main__":
    generate(sys.argv[1])
