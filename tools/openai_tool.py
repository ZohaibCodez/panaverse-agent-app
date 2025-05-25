from agents.tool import function_tool


@function_tool
def openai_tech_tool() -> str:
    return "OpenAI Tech Tool used...!"
