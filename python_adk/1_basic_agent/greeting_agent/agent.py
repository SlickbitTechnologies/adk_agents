
from google.adk.agents import Agent

root_agent=Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="A  greeting agent",
    instruction="""you are a helpful assistant that greets users.
    ask the user for their name and greet them by name.""",
)