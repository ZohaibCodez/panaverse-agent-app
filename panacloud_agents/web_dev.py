from panacloud_agents.config import model
from panacloud_agents.agentic_dev import agenticdev_agent
from agents import Agent

webdev_agent = Agent(
    name="Web App Developer",
    instructions="You are a web developer for Panacloud. You are responsible for developing web applications for the company.",
    model=model,
    handoff_description="You are the Web Dev Agent, specialized in assisting users with queries related to web development. Your primary function is to provide accurate, clear, and helpful information on web development topics, including but not limited to front-end, back-end, frameworks, languages, and best practices.",
    handoffs=[agenticdev_agent],
)
