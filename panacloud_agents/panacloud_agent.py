from agents import Agent
from panacloud_agents.config import model
from panacloud_agents.agentic_dev import agenticdev_agent
from panacloud_agents.mobile_dev import mobiledev_agent
from panacloud_agents.web_dev import webdev_agent

panacloud_agent = Agent(
    name="Panacloud Marketing Agent",
    instructions="You are a marketing agent for Panacloud. You are responsible for generating marketing content for the company.",
    model=model,
    handoffs=[webdev_agent, mobiledev_agent, agenticdev_agent],
)
