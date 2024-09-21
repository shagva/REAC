""" 
Basic example of scraping pipeline using Code Generator with schema
"""

import os, json
from typing import List
from dotenv import load_dotenv
from langchain_core.pydantic_v1 import BaseModel, Field
from scrapegraphai.graphs import CodeGeneratorGraph

load_dotenv()

# ************************************************
# Define the output schema for the graph
# ************************************************

class Project(BaseModel):
    title: str = Field(description="The title of the project")
    description: str = Field(description="The description of the project")

class Projects(BaseModel):
    projects: List[Project]

# ************************************************
# Define the configuration for the graph
# ************************************************

openai_key = os.getenv("OPENAI_APIKEY")

graph_config = {
    "llm": {
        "api_key":openai_key,
        "model": "openai/gpt-4o",\
    },
    "library": "beautifulsoup",
    "verbose": True,
    "headless": False,
    "reduction": 2,
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

code_generator_graph = CodeGeneratorGraph(
    prompt="List me all the projects with their description",
    source="https://perinim.github.io/projects/",
    schema=Projects,
    config=graph_config
)

result = code_generator_graph.run()
print(result)
