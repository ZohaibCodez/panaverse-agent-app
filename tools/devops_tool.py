from agents.tool import function_tool


@function_tool
def devops_agent_tool() -> str:
    return "Devops Agent Tool used...!"
