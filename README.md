# Smart HVAC Customer Support Agent

This project is a fully functional AI agent prototype based on the Smart HVAC Customer Support blueprint. The agent answers HVAC customer questions, retrieves troubleshooting guidance, checks demo customer records, considers weather context, and suggests appointment windows.

## Requirements Met

- Framework: LangChain
- Reasoning pattern: ReAct agent
- Tools: HVAC knowledge-base search, customer lookup, local weather, appointment lookup
- Memory: file-based conversation memory saved in `memory/chat_history.json`
- Retrieval Augmented Generation: FAISS vector search over `data/hvac_faq.md`
- No hard-coded API keys

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create your `.env` file:

```bash
copy .env.example .env
```

On Mac/Linux use:

```bash
cp .env.example .env
```

5. Add your keys to `.env`:

```bash
OPENAI_API_KEY=your_openai_api_key_here
WEATHERAPI_KEY=optional_weatherapi_key_here
CUSTOMER_CITY=Houston
CUSTOMER_STATE=TX
```

The WeatherAPI key is optional. The agent still works without it, but the weather tool will return a setup message instead of live weather.

## Run

```bash
python src/main.py
```

## Example Messages

```text
My AC is not cooling and I already changed the filter.
```

```text
My email is demo@example.com. Can you check my record and help me schedule a seasonal check?
```

```text
There is a small drip on my counter when the unit turns off at night.
```

## Safety Design

The agent avoids giving instructions for dangerous repairs involving electricity, gas, refrigerant, or internal equipment. If the issue sounds urgent, it recommends a technician and offers the earliest service window.
