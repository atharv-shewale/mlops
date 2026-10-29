def get_message(name: str = "World") -> str:
    return f"Hello, {name}! Welcome to MLOps UAT Environment."

def main():
    message = get_message("DevOps Team")
    print("=" * 50)
    print(message)
    print("Application Status: RUNNING (OK)")
    print("=" * 50)

if __name__ == "__main__":
    main()
