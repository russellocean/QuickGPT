import os

from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.utilities import WikipediaAPIWrapper
from langchain.agents import Tool

import openai

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
WOLFRAM_ALPHA_APPID = os.environ.get("WOLFRAM_ALPHA_APPID")

openai.api_key = OPENAI_API_KEY

def setup_agent():
    search = GoogleSerperAPIWrapper()
    wolfram = WolframAlphaAPIWrapper()
    wikipedia = WikipediaAPIWrapper()

    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="Useful for when you need to answer questions about current events. You should ask targeted questions"
        ),
        Tool(
            name="Wolfram",
            func=wolfram.run,
            description="Useful for when you need to answer questions about math, science, geography."
        ),
        Tool(
            name="Wikipedia",
            func=wikipedia.run,
            description="Useful for when you need to answer questions about history, geography, and other topics."
        )
    ]

    prefix = """Answer the following questions as best you can. You have access to the following tools:"""
    suffix = """If answering a coding question only provide code, add comments to communicate your thought process.
    If given multiple answer choices only provide the letter or answer choice.
    If answering a free response question only provide the answer. If you are unable to answer a question fully, provide as much as you can and where you got stuck.

    Question: {input}
    {agent_scratchpad}"""

    prompt = ZeroShotAgent.create_prompt(
        tools, 
        prefix=prefix, 
        suffix=suffix, 
        input_variables=["input", "agent_scratchpad"]
    )

    llm_chain = LLMChain(llm=ChatOpenAI(temperature=0.2, model="gpt-4"), prompt=prompt)
    tool_names = [tool.name for tool in tools]

    agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=tool_names)

    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

    return agent_executor

agent_executor = setup_agent()

def ask_agent(message):
    try:
        return agent_executor.run(message)
    except ValueError as e:
        print(f"Error: {e}")
        return "An error occurred. Please try again."