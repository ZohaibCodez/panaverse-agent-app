from agents import Runner
from agents.extensions.visualization import draw_graph
from openai.types.responses import ResponseTextDeltaEvent
import chainlit as cl
from panacloud_agents.panacloud_agent import panacloud_agent


@cl.on_chat_start
async def chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello there, how can i assist you today?").send()


@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})
    msg = cl.Message(content="")
    await msg.send()
    response = Runner.run_streamed(
        starting_agent=panacloud_agent,
        input=history,
    )
    async for event in response.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)
    history.append({"role": "system", "content": response.final_output})
    await msg.update()
    cl.user_session.set("history", history)
