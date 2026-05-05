"""Smart HVAC Customer Support Agent using LangChain ReAct."""

import json
from pathlib import Path

from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.memory import ConversationBufferWindowMemory
from langchain_openai import ChatOpenAI

from tools import (
    check_available_appointments,
    get_local_weather,
    lookup_customer_record,
    search_hvac_knowledge_base,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MEMORY_FILE = PROJECT_ROOT / "memory" / "chat_history.json"

SYSTEM_GUIDANCE = """
You are a professional and friendly Smart HVAC Support Agent.
Use ReAct reasoning and tools when helpful.
Ask follow-up questions if the problem is unclear.
Do not give dangerous advice.
For gas smells, major leaks, or burning smells, recommend urgent service.
Use HVAC knowledge before troubleshooting and offer appointment windows when service is needed.
"""


def get_memory():
    memory = ConversationBufferWindowMemory(
        k=6,
        memory_key="chat_history",
        input_key="input",
        output_key="output",
        return_messages=True,
    )

    if MEMORY_FILE.exists():
        for msg in json.loads(MEMORY_FILE.read_text(encoding="utf-8")):
            if msg["role"] == "user":
                memory.chat_memory.add_user_message(msg["content"])
            else:
                memory.chat_memory.add_ai_message(msg["content"])

    return memory


def save_memory(memory):
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = [
        {
            "role": "user" if msg.type == "human" else "assistant",
            "content": msg.content,
        }
        for msg in memory.chat_memory.messages
    ]
    MEMORY_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def build_agent():
    load_dotenv(PROJECT_ROOT / ".env")

    tools = [
        search_hvac_knowledge_base,
        lookup_customer_record,
        get_local_weather,
        check_available_appointments,
    ]

    prompt = hub.pull("hwchase17/react-chat").partial(system_message=SYSTEM_GUIDANCE)

    memory = get_memory()

    agent = create_react_agent(
        llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.2),
        tools=tools,
        prompt=prompt,
    )

    return AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=6,
    ), memory


def run_agent_once(customer_message):
    executor, memory = build_agent()
    result = executor.invoke({"input": customer_message})
    save_memory(memory)
    return result["output"]
