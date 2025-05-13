from my_frontend_agent import agent_creator
from agents import Runner , set_tracing_disabled
set_tracing_disabled(True)

import chainlit as cl


@cl.on_chat_start
async def start():
    await cl.Message(content="I am your personal assistant.").send()
    cl.user_session.set("chat_history", [])


@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("chat_history") or []

    history.append({"role": "user", "content": message.content})

    agent = agent_creator()

    response = await Runner.run(starting_agent=agent , input=history)

    history.append({"role": "assistant", "content": response.final_output}) 

    cl.user_session.set("chat_history", history)

    await cl.Message(content=response.final_output).send()

