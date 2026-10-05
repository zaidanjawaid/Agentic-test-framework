"""Planner: turns a feature description into test cases.

Not an agent yet - one LLM call, no tools, no loop.
Usage:  python agents/planner.py "Login form on saucedemo.com"
"""
import os
import sys

import anthropic

client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY
MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")

PROMPT = """You are a senior QA engineer.
Write test cases for the feature below as a Markdown table:
ID | Scenario | Steps | Expected result.
Cover happy path, negative, boundary and security cases.

Feature: {feature}"""


def plan(feature: str) -> str:
    reply = client.messages.create(
        model=MODEL, max_tokens=2000,
        messages=[{"role": "user",
                   "content": PROMPT.format(feature=feature)}])
    return reply.content[0].text


if __name__ == "__main__":
    print(plan(sys.argv[1]))
