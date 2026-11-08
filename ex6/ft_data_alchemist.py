def main():
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    new_list = [x.capitalize() for x in players if x]

    print(f"Initial list of players: {new_list}")

if __name__ == "__main__":
    main()
