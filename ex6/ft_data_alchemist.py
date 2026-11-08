import random


def main() -> None:
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

    print(f"Initial list of players: {players}")

    capitalized_players: list[str] = [x.capitalize() for x in players]
    print(f"New list with all names capitalized: {capitalized_players}")

    capitalized_only: list[str] = [x for x in players if x == x.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only}")

    scores: dict[str, int] = {
        player: random.randrange(1000) for player in capitalized_players
    }
    print(f"Score dict: {scores}")

    score_average: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(score_average, 2)}")

    high_scores: dict[str, int] = {
        p: s for p, s in scores.items() if s > score_average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
