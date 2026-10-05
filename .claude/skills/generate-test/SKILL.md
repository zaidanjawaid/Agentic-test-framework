---
description: Explore the app and write one pytest-playwright test
argument-hint: [behaviour to test]
disable-model-invocation: true
---

Goal: $ARGUMENTS

1. Use the Playwright tools: navigate, take a snapshot
   before every action, then click/type to reach the goal.
2. Read pages/ and conftest.py. Reuse page objects;
   add a locator or method to a page object if one is missing.
3. Write ONE test in tests/ following CLAUDE.md.
4. Run it with pytest. If it fails, read the error,
   fix the test (not the app), and run again.
5. Stop when it passes. Summarise what you did.
