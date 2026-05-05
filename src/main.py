"""Command-line entry point for the Smart HVAC Support Agent."""

from __future__ import annotations

from agent import run_agent_once


def main() -> None:
    print("Smart HVAC Support Agent")
    print("Type 'exit' to stop.\n")

    while True:
        customer_message = input("Customer: ").strip()
        if customer_message.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not customer_message:
            continue

        try:
            answer = run_agent_once(customer_message)
        except Exception as error:
            answer = (
                "I could not complete the request because of a setup or API error. "
                f"Details: {error}"
            )

        print(f"\nAgent: {answer}\n")


if __name__ == "__main__":
    main()
