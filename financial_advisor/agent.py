from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

MODEL = LiteLlm("gemini/gemini-2.5-flash-preview-09-2025")


weather_agent = Agent(
    name="WeatherAgent",
    instruction="You help the user with weather related questions",
    model=MODEL,
)

root_agent = weather_agent
