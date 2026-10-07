from python1.calculator import add, divide, multiply, subtract

# Dispatch table: maps each menu choice to (symbol, function).
ACTIONS = {
    "1": ("+", add),
    "2": ("-", subtract),
    "3": ("*", multiply),
    "4": ("/", divide),
}

MENU = """
=== Calculator ===
1) Add
2) Subtract
3) Multiply
4) Divide
q) Quit
"""


def safe_float(prompt: str) -> float | None:
    """Ask the user for a number.

    Args:
        prompt: Text shown to the user.
    Returns:
        The number entered, or None if the input was not a valid number.
    """
    try:
        return float(input(prompt).strip())
    except ValueError:
        print("Please enter a valid number.")
        return None


def main() -> None:
    """Run the calculator menu until the user quits."""
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in ACTIONS:
            print("Invalid choice. Please pick 1-4 or q.")
            continue

        a = safe_float("First number: ")
        if a is None:
            continue
        b = safe_float("Second number: ")
        if b is None:
            continue

        symbol, operation = ACTIONS[choice]
        try:
            result = operation(a, b)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"{a} {symbol} {b} = {result}")
