"""Tools for the Smart HVAC Support Agent."""

import json
import os
from pathlib import Path

import requests
from langchain.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def load_customers():
    return json.loads((DATA_DIR / "customers.json").read_text(encoding="utf-8"))


def get_vector_store():
    index_dir = DATA_DIR / "faq_faiss_index"
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    if index_dir.exists():
        return FAISS.load_local(
            str(index_dir),
            embeddings,
            allow_dangerous_deserialization=True,
        )

    faq = (DATA_DIR / "hvac_faq.md").read_text(encoding="utf-8")
    docs = [f"## {s.strip()}" for s in faq.split("## ") if s.strip()]
    store = FAISS.from_texts(docs, embeddings)
    store.save_local(str(index_dir))
    return store


@tool
def search_hvac_knowledge_base(question: str) -> str:
    """Search HVAC troubleshooting, safety, maintenance, and scheduling guidance."""
    results = get_vector_store().similarity_search(question, k=3)
    return "\n\n".join(doc.page_content for doc in results)


@tool
def lookup_customer_record(email: str) -> str:
    """Look up a demo customer record by email address."""
    record = load_customers().get(email.lower().strip())

    if not record:
        return "No customer record found. Ask for name, address, and equipment details."

    return json.dumps(record, indent=2)


@tool
def get_local_weather(city: str = "Houston", state: str = "TX") -> str:
    """Get local weather for HVAC scheduling context."""
    location = f"{city}, {state}"
    api_key = os.getenv("WEATHERAPI_KEY")

    if not api_key:
        return f"No WeatherAPI key found for {location}. Use general scheduling advice."

    data = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params={"key": api_key, "q": location, "aqi": "no"},
        timeout=10,
    ).json()

    current = data["current"]
    return (
        f"Current weather in {location}: {current['temp_f']}°F, "
        f"{current['condition']['text']}, humidity {current['humidity']}%."
    )


@tool
def check_available_appointments(urgency: str = "normal") -> str:
    """Return demo appointment windows based on urgency."""
    if urgency.lower() in {"urgent", "emergency", "high"}:
        return "Earliest urgent window: today 12 PM - 2 PM, then tomorrow 8 AM - 10 AM."

    return "Available windows: tomorrow 8 AM - 12 PM, tomorrow 12 PM - 4 PM, or next business day 8 AM - 12 PM."
