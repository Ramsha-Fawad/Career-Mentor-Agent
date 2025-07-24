import chainlit as cl
from agents import Runner
from agents.run import RunConfig
from expert.career_agent import career_agent
from setup_config import google_gemini_config

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message("Hello! I’m your personalized Career Mentor.""Tell me about the subjects you enjoy, your skills so far, or your dream career path!").send()

@cl.on_message
async def handle(msg: cl.Message):
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": msg.content})

    thinking = cl.Message("Thinking...")
    await thinking.send()

    try:
        result = await Runner.run(
            career_agent,
            history,
            run_config=google_gemini_config
        )
        output = result.final_output

        thinking.content = output
        await thinking.update()

        history = result.to_input_list()
        cl.user_session.set("history", history)

    except Exception as e:
        thinking.content = f"Error: {e}"
        await thinking.update()