# Bonus: build the agent loop yourself

Claude Code runs the observe -> think -> act -> check loop for you. These three
scripts show the same loop written by hand with the Claude API (about 20 lines).

They need a Claude API key with credits from platform.claude.com. That is
billed separately from a Claude Pro/Max subscription.

    export ANTHROPIC_API_KEY="sk-ant-..."
    python agents/planner.py "Login form on saucedemo.com"
    python agents/generator.py "A locked-out user sees an error"
    python agents/triage.py results.xml
