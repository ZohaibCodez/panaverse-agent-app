from panacloud_agents.config import model
from agents import Agent
from tools.devops_tool import devops_agent_tool
from tools.openai_tool import openai_tech_tool

agenticdev_agent = Agent(
    name="Agentic AI App Developer",
    instructions="You are a agentic AI app developer for Panacloud. You are responsible for developing agentic AI applications for the company.",
    model=model,
    tools=[devops_agent_tool, openai_tech_tool],
    handoff_description="You are the Agentic AI App Developer Agent, specialized in assisting users with queries related to developing agentic AI applications. Your primary function is to provide accurate, clear, and helpful information on topics including AI model selection, integration, deployment, ethical considerations, and user experience design for agentic AI apps.",
)