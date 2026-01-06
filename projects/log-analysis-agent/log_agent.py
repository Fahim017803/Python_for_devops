from strands import Agent
from strands_tools import file_read

SYSTEM_PROMPT = """
You are a DevOps Log Analysis Agent.

You can use tools to read files when needed.
Analyze only the given log content.

Output:
- Summary
- just Errors counts
- just Warnings counts
- just info counts
- Possible Root Cause in short
- DevOps Suggestions in short
"""

agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    tools=[file_read]
)

agent("Read the app.log file and analyze it.")
