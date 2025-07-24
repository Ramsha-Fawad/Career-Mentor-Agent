from typing import TypedDict
from agents import function_tool, RunContextWrapper, AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class CareerRoadmapInput(TypedDict):
    career_field: str

@function_tool
async def get_career_roadmap(wrapper: RunContextWrapper, input: CareerRoadmapInput) -> dict:
    try:
        prompt = (
           f"I'm aiming to build a career as a {input['career_field']}. "
"Could you outline a clear roadmap of skills I need at beginner, intermediate, and advanced levels? "
"Lay it out using bullet points or numbered sections, and include suggested milestones or projects for each stage."

        )

        response = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content

        return {
            "skill_roadmap": output.strip()
        }

    except Exception as e:
        print("❌ Error in get_career_roadmap tool:", str(e))
        return {
            "error": f"⚠️ Oops—something went wrong while generating your roadmap. Please try again or check your input.: {str(e)}"
        }