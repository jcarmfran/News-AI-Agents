from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

## Call Gemini Models

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY")
                             )

## AGENT CREATION ##

## Creating "Senior Research" Agent

news_researcher = Agent(
    role = "Senior Researcher",
    goal = "Uncover groundbreaking technologies in {topic}",
    verbose = True,
    memory = True,
    backstory = ("Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could change the world."),
    tools = [tool],
    llm = llm,
    allow_delegation = True # true to communicate to other agents
)

# Creating a "News Blog Writer" Agent
news_writer = Agent(
    role = "News Blog Writer",
    goal = "Narrate compelling tech stories about {topic}",
    verbose = True,
    memory = True,
    backstory = ("Having a knack for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner."),
    tools = [tool],
    llm = llm,
    allow_delegation = False # Not necessary to communicate to other agents
)