from google.adk import Agent
from google.adk.apps.app import App

def read_project_note(project_name: str):
    """Consult this to find deadlines for a project."""
    # In a real scenario, this would search Google Drive or a DB
    notes = {
        "Phoenix": "Deadline is Friday at 5 PM.",
        "Alpha": "Launch date is next Monday."
    }
    return notes.get(project_name, "No notes found for this project.")

def check_calendar_slot(day: str, time: str):
    """Checks if a specific time is free on the calendar."""
    # Simulating a calendar check
    return f"The slot at {time} on {day} is currently FREE."

# 1. Define the worker agents (Sub-agents)
scheduler_agent = Agent(
    name="scheduler",
    model="gemini-2.5-flash",
    instruction="You handle calendar queries and task timing.",
    tools=[check_calendar_slot]
)

info_agent = Agent(
    name="info_retriever",
    model="gemini-2.5-flash",
    instruction="You retrieve information from the user's project notes.",
    tools=[read_project_note]
)

# 2. Define the Root Agent (The Manager)
# This is the 'entry point' the ADK looks for
root_agent = Agent(
    name="manager",
    model="gemini-2.5-flash",
    instruction="Route user requests to the scheduler or the info_retriever.",
    sub_agents=[scheduler_agent, info_agent]
)

app = App(
    name="Task scheduler and data retriever",
    root_agent=root_agent
)
