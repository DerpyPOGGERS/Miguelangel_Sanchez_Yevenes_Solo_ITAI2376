# Smart HVAC Customer Support Agent

# Problem Statement — What real-world problem does your agent solve? Who benefits?
My AI agent will be a Smart HVAC Customer Support

For my blueprint, I want my agent to answer customer questions, detect service issues, etc. The benefits for this customer support, is to reduce repetitive phone calls and emails and help many people around the same time.

# Option Choice — Which option (A or B) and why.

I am choosing option A because this allows me to demonstrate one system on how the system can act using deep learning. Option b, being a multi agent system would add complexity and potential for coordination issues whereas in single agent, It would be easier to manage and less complex since we are only focusing on one agent.

# Deep Learning Connection — Identify at least 2 course modules (CNNs, RNNs, Transformers, VAEs, GANs, etc.) and explain how they fit into your agent.

There are two course modules I have chosen, Transformers and CNN's will help me on this blueprint idea.
I chose Transformers because, this helps the agent understand the customers messages into their system and give out responses that are professional and human like. Transformers analyze the entire context of a conversation instantly to provide coherent responses.
The second choice is CNNs because of uploading pictures. If a customer needs to send an image for any problems of a thermostat, any leaks happening, or parts that are damaged, The CNN will help visualize the problem and recognize.

# Agent Framework — Which framework you plan to use (LangChain, CrewAI, AutoGen, smolagents, or other) and why.

I would use LangChain because it is made for building agents that combine language models with tools. LangChain agents can reason about a task, decide which tool to use, and work step-by-step toward a final answer.
They also have many connections with models, API's and many tools, making this very useful for the agent to use customer records.

# Tools & Data — What tools, APIs, and data sources will your agent need?

<img width="630" height="202" alt="image" src="https://github.com/user-attachments/assets/6573a370-bf05-4776-bac7-fef164e0f5ab" />

Anticipated Challenges — What could go wrong and how will you handle it?

A common challenge that can happen is the agent will misunderstand the customer's problem and give either the wrong results or get an error in responding. For now the Agent should ask follow up questions before the problem.

Safety is also another issue if the agent tells the customer to perform repairs on their own without a technician being called. To solve this it's always recommended the agent suggests a technician.

Lastly, image recognition. If the image is unclear, the agent will not be able to recognize it, so the agent should ask for a better picture.


This project is a fully functional AI agent prototype based on the Smart HVAC Customer Support blueprint. The agent answers HVAC customer questions considers gas leaks, air conditioning, weather, and more.

## Requirements Met

- Framework: LangChain
- Reasoning pattern: ReAct agent
- Tools: HVAC knowledge-base search, customer lookup, local weather, appointment lookup
- Memory: file-based conversation memory saved in
- Retrieval Augmented Generation: FAISS vector search over

## Setup

1. Create a virtual environment:

```
python -m venv .venv
```

2. Activate it:


```
.venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Create your `.env` file:

```
copy .env.example .env
```

5. Add your keys to `.env`:

```
OPENAI_API_KEY=openai_api_key_here
WEATHERAPI_KEY=weatherapi_key_here
CUSTOMER_CITY=Houston
CUSTOMER_STATE=TX
```

The WeatherAPI key is optional. The agent still works without it.
## Run

```
python src/main.py
```

## Example Messages

```text
My AC is not cooling and I changed the filter, but nothing fixed.
```

```text
My email is JohnDoe@example.com. Can you check my unit and help me schedule a seasonal check?
```

```text
There is a small drip on my counter when the unit turns off at night.
```

## Safety Design

The agent avoids giving instructions for dangerous repairs that should not be operated unless technician is nearby. Also to not give false information and making sure to ask follow up questions if stuck.
