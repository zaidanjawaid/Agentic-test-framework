---
description: Fix a UI test that broke because the page changed
argument-hint: [failing test name]
disable-model-invocation: true
---

Test to heal: $ARGUMENTS

1. Run it with pytest and read the failure.
2. Open the page with the Playwright tools and take a snapshot.
3. If a locator no longer matches, fix it in pages/ (not in the test).
4. If the app itself looks broken, stop and report a product bug instead.
5. Run the test again and show me the diff. Never commit.
