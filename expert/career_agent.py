from agents import Agent, handoff
from setup_config import model 
from expert.skill_agent import skill_agent
from expert.job_agent import job_agent
from util.make_on_handoff_message import make_on_handoff_message


career_agent = Agent(
    name="CareerAgent",
    instructions="""
You are a professional career counselor.

Responsibilities:
- Ask users about their interests, favorite subjects, or activities they enjoy.
- Based on that, suggest 2-3 relevant career paths.
- Ask the user which one they would like to explore further.
- Once they reply, hand off to the SkillAgent to provide a skill-building roadmap.

Tone:
- Friendly, supportive, curious, and student-focused.

Avoid guessing if the user hasn't provided enough info. Ask follow-up questions if needed.
""",
    tools=[],
    model=model,
    handoffs=[
    handoff(agent=skill_agent, on_handoff=make_on_handoff_message(skill_agent)),
    handoff(agent=job_agent, on_handoff=make_on_handoff_message(job_agent)),
]

)