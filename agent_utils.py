import os

from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent

from agent_components import CustomPromptTemplate, CustomOutputParser

import openai

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
WOLFRAM_ALPHA_APPID = os.environ.get("WOLFRAM_ALPHA_APPID")

openai.api_key = OPENAI_API_KEY

def setup_agent():
    search = GoogleSerperAPIWrapper()
    wolfram = WolframAlphaAPIWrapper()

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
        )
    ]
    
    # Set up the base template
    template = """Answer the following questions as best you can, but speaking as a pirate might speak. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    If answering a coding question only provide code, add comments to communicate your thought process.
    If given multiple answer choices only provide the letter or answer choice.
    If answering a free response question only provide the answer.

    Begin!

    Question: {input}
    {agent_scratchpad}"""
    
    prompt = CustomPromptTemplate(
        template=template,
        tools=tools,
        # This omits the `agent_scratchpad`, `tools`, and `tool_names` variables because those are generated dynamically
        # This includes the `intermediate_steps` variable because that is needed
        input_variables=["input", "intermediate_steps"]
    )
    
    output_parser = CustomOutputParser()
    
    llm = ChatOpenAI(temperature=0.5, model="gpt-4")

    llm_chain = LLMChain(llm=llm, prompt=prompt)
    
    tool_names = [tool.name for tool in tools]
    agent = LLMSingleActionAgent(
        llm_chain=llm_chain, 
        output_parser=output_parser,
        stop=["\nObservation:"], 
        allowed_tools=tool_names
    )
    
    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

    return agent_executor

agent_executor = setup_agent()

def ask_agent(message):
    return agent_executor.run(message)