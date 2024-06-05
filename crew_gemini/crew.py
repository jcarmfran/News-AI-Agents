from crewai import Crew, Process
from agents import news_researcher, news_writer
from tasks import research_task, write_task

# Forming Tech-Focused Crew with Enhanced Configurations
crew = Crew(
    agents = [news_researcher, news_writer],
    tasks = [research_task, write_task],
    process = Process.sequential
)

## Starting task execution with enhanced feedback

result = crew.kickoff(inputs={"topic": "AI in healthcare"})
print(result)