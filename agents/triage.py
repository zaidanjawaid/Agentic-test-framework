"""Triage: reads pytest's JUnit XML and asks Claude why tests failed.

Used by CI only when the test step fails. Output is Markdown.
Usage:  python agents/triage.py results.xml
"""
import os
import sys
import xml.etree.ElementTree as ET

import anthropic

if not os.path.exists(sys.argv[1]):
    sys.exit(print("## AI triage\nNo results file: tests did not run (check the install steps)."))

failures = []
for case in ET.parse(sys.argv[1]).iter("testcase"):
    for f in case.findall("failure") + case.findall("error"):
        log = (f.text or "")[:1500]
        failures.append(f"{case.get('name')}:\n{log}")

if failures:
    reply = anthropic.Anthropic().messages.create(
        model=os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5"), max_tokens=1000,
        messages=[{"role": "user", "content":
            "Triage these failing UI tests. For each give: likely cause "
            "(product bug / test bug / flaky / environment), evidence "
            "and a one-line fix.\n\n" + "\n\n".join(failures)}])
    print("## AI triage\n" + reply.content[0].text)
else:
    print("## AI triage\nNo test failures found in the results file.")
