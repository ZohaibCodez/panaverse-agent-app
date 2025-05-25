from agents import AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
import os
from dotenv import load_dotenv

load_dotenv()

set_tracing_disabled(True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
Base_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client = AsyncOpenAI(base_url=Base_URL, api_key=GEMINI_API_KEY)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=external_client)
