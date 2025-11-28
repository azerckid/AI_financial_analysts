from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.data_analyst import data_analyst
from .sub_agents.financial_analyst import financial_analyst
from .sub_agents.news_analyst import news_analyst
from .prompt import PROMPT

MODEL = Gemini(model="gemini-2.5-flash-preview-09-2025")

def save_advice_report():
    pass

financial_advisor = Agent(
    name="FinancialAdvisor",
    instruction=PROMPT,
    model=MODEL,
    tools=[
        AgentTool(agent=financial_analyst),
        AgentTool(agent=news_analyst),
        AgentTool(agent=data_analyst),
        save_advice_report,
    ],
)

root_agent = financial_advisor
