from calculator import calculate


def read_number(prompt: str) -> float:
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def read_operator(prompt: str) -> str:
    valid = {"+", "-", "*", "/"}
    while True:
        op = input(prompt).strip()
        if op in valid:
            return op
        print("Please choose one of: +, -, *, /")


def interactive_mode() -> None:
    print("Simple Calculator")
    print("-----------------")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        first = input("Enter first number (or 'q' to quit): ").strip()
        if first.lower() == "q":
            print("Goodbye!")
            break

        try:
            a = float(first)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        op = read_operator("Enter operator (+, -, *, /): ")

        second = input("Enter second number (or 'q' to quit): ").strip()
        if second.lower() == "q":
            print("Goodbye!")
            break

        try:
            b = float(second)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        try:
            result = calculate(a, op, b)
        except ZeroDivisionError as exc:
            print(f"Error: {exc}\n")
            continue
        except ValueError as exc:
            print(f"Error: {exc}\n")
            continue

        print(f"Result: {result}\n")


def cli() -> None:
    import sys

    if len(sys.argv) == 4:
        # Command-line mode: python main.py 2 + 3
        _, first, op, second = sys.argv
        try:
            a = float(first)
            b = float(second)
            result = calculate(a, op, b)
            print(result)
            return
        except ValueError as exc:
            print(f"Error: {exc}")
            sys.exit(1)
        except ZeroDivisionError as exc:
            print(f"Error: {exc}")
            sys.exit(1)

    # Fallback to interactive calculator
    interactive_mode()


if __name__ == "__main__":
    cli()
