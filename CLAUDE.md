# Test framework rules (read before writing tests)

## Project
- Python + pytest + Playwright. Site under test: https://www.saucedemo.com
- Page objects live in pages/. Test data lives in config.py.
- Users: standard_user, locked_out_user. Password: secret_sauce.

## When you write a test
- Use the login_page fixture and page objects, never raw URLs
- Locators: get_by_role > get_by_placeholder > get_by_test_id
- Assert with expect(); check exact text, not just visibility
- Never use time.sleep()
- One behaviour per test, named test_<what_it_checks>

## When you are done
- Run: pytest <file> -q   and fix until it passes
- Show me the diff. Never commit or push.
