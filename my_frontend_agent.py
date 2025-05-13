from agents import Agent, Runner, set_tracing_disabled , function_tool
from agents.extensions.models.litellm_model import LitellmModel
import os
from dotenv import load_dotenv , find_dotenv
from tavily import TavilyClient


load_dotenv(find_dotenv())


@function_tool
def weather_agent(user_input: str) -> str:
    """search tool"""
    tavily_client = TavilyClient(api_key=os.getenv("Tavily_Api_Key"))
    response = tavily_client.search(query=user_input)
    return response

def agent_creator() -> Agent:
    agent = Agent(
        name="Assistant",
        instructions="A helpful assistant that can answer questions and provide information.",
        model= LitellmModel( api_key=os.getenv("Groq_Api_Key"), model="groq/deepseek-r1-distill-llama-70b", ),
        tools=[weather_agent],

    )
    return agent

