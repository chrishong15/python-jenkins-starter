def hello(name: str) -> str:
    return f"Hello, {name}!"


def run_interactive_loop() -> None:
    while True:
        name = input("Enter your name (or 'q' to quit) : ")
        if name.lower() == "q":
            break
        print(hello(name))


if __name__ == "__main__":
    run_interactive_loop()
