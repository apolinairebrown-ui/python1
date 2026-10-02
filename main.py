from src.python1.calculator import add, subtract, multiply, divide

def main() -> None:
    print("Testing Calculator Functions:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 4 = {divide(20, 4)}")

if __name__ == "__main__":
    main()