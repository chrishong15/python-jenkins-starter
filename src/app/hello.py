def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    while True:
        name = input("Enter your name (or 'q' to quit) : ")
        if name.lower() == "q":
            break
        print(hello(name))