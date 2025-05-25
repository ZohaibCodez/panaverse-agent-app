from panacloud_agents.config import model
from panacloud_agents.agentic_dev import agenticdev_agent
from agents import Agent

mobiledev_agent = Agent(
    name="Mobile App Developer",
    instructions="You are a mobile developer for Panacloud. You are responsible for developing mobile applications for the company.",
    model=model,
    handoff_description="You are the Mobile App Developer Agent, specialized in assisting users with queries related to mobile application development. Your primary function is to provide accurate, clear, and helpful information on mobile development topics, including but not limited to native development, cross-platform frameworks, mobile app design, and deployment.",
    handoffs=[agenticdev_agent],
)
