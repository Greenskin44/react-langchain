"""
React Agent with LangChain RAG Implementation

A sophisticated ReAct (Reasoning and Acting) agent implementation using LangChain
for ice breaker applications with RAG capabilities. This module demonstrates
the integration of custom tools and callback handlers for enhanced AI interactions.

Original work by Eden Marco (@emarco177)
Educational implementation from Eden Marco's Udemy Course on LangChain

Author: Based on Eden Marco's educational content
License: MIT
"""

from typing import List, Union
from dotenv import load_dotenv

from langchain.agents import tool
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain_core.agents import AgentAction, AgentFinish, AgentStep
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import render_text_description, Tool
from langchain_openai import ChatOpenAI

from callbacks import AgentCallbackHandler

# Load environment variables from .env file
load_dotenv()


@tool()
def get_text_length(text: str) -> int:
    """
    Calculate the length of text by character count.
    
    This tool serves as a foundational example for RAG-enabled ice breaker
    applications, demonstrating how custom tools can be integrated into
    the agent's reasoning and action-taking capabilities.
    
    Args:
        text (str): The input text to measure
        
    Returns:
        int: The number of characters in the text
        
    Example:
        >>> get_text_length("Hello World")
        11
    """
    return len(text)


def find_tool_by_name(tools: List[Tool], tool_name: str) -> Tool:
    """
    Locate a specific tool from the available tools list by name.
    
    This utility function enables dynamic tool selection during agent execution,
    supporting the flexible tool usage patterns required for RAG applications.
    
    Args:
        tools (List[Tool]): List of available tools
        tool_name (str): Name of the tool to find
        
    Returns:
        Tool: The requested tool object
        
    Raises:
        ValueError: If the specified tool is not found
    """
    for tool in tools:
        if tool.name == tool_name:
            return tool

    raise ValueError(f'Tool not found: {tool_name}. Available tools: {[t.name for t in tools]}')


def main():
    """
    Main execution function for the React Agent demonstration.
    
    This function showcases the ReAct (Reasoning and Acting) pattern implementation
    for ice breaker applications with RAG capabilities. It demonstrates:
    - Tool registration and management
    - Agent prompt template configuration  
    - LLM integration with custom callbacks
    - Agent execution with intermediate step tracking
    
    The implementation serves as a foundation for more complex RAG applications
    involving grocery sales data and complementary datasets.
    """
    print('🚀 React Agent with LangChain RAG Implementation')
    print('=' * 50)
    print('Initializing agent for ice breaker application...\n')
    
    # Register available tools for the agent
    tools = [get_text_length]
    print(f"📋 Registered tools: {[tool.name for tool in tools]}")

    # Define the ReAct agent prompt template
    template = """
    You are an intelligent agent designed to support ice breaker applications with RAG capabilities.
    Answer the following questions as best you can. You have access to the following tools:

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
    
    When you need to call a tool, output ONLY:
    Thought: <your reasoning>
    Action: <tool name>
    Action Input: <input>
    Do NOT output any "Final Answer" or additional text after the Action Input.

    Begin!
    
    Question: {input}
    Thought: {agent_scratchpad}
    """

    # Configure the prompt template with available tools
    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([t.name for t in tools])
    )

    # Initialize the language model with custom callbacks
    llm = ChatOpenAI(
        temperature=0, 
        stop=["\nObservation"], 
        callbacks=[AgentCallbackHandler()]
    )
    
    # Track intermediate steps for reasoning transparency
    intermediate_steps = []

    # Create the agent pipeline
    agent = ({
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"]),
             }
             | prompt
             | llm
             | ReActSingleInputOutputParser()
             )

    # Execute the agent with a sample question
    print("\n🤔 Processing sample question...")
    sample_question = "How many characters in length are in the word: Fish ?"
    print(f"Question: {sample_question}\n")

    agent_step = ""
    step_count = 0
    
    while not isinstance(agent_step, AgentFinish):
        step_count += 1
        print(f"🔄 Step {step_count}:")
        
        agent_step: Union[AgentAction, AgentFinish] = agent.invoke(
            {
                "input": sample_question,
                "agent_scratchpad": intermediate_steps
            }
        )
        
        print(f"Agent Step: {agent_step}")

        if isinstance(agent_step, AgentAction):
            tool_name = agent_step.tool
            tool_to_use = find_tool_by_name(tools, tool_name)
            tool_input = agent_step.tool_input

            print(f"🔧 Using tool: {tool_name} with input: {tool_input}")
            observation = tool_to_use.func(str(tool_input))
            print(f"📊 Observation: {observation}")
            intermediate_steps.append((agent_step, str(observation)))

    print(f"\n✅ Agent completed in {step_count} steps")
    print("🎉 Demonstration completed successfully!")


if __name__ == "__main__":
    main()
