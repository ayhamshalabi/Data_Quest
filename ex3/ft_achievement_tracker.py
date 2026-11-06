import random


def all_achievements() -> list[str]:
    return [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder",
    ]


def gen_player_achievements() -> set[str]:
    achievements: list[str] = all_achievements()

    count: int = random.randint(1, len(achievements))

    selected_achievements: list[str] = random.sample(achievements, count)

    return set(selected_achievements)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    player_1: set[str] = gen_player_achievements()
    player_2: set[str] = gen_player_achievements()
    player_3: set[str] = gen_player_achievements()
    player_4: set[str] = gen_player_achievements()

    print(f"Player Alice: {player_1}")
    print(f"Player Bob: {player_2}")
    print(f"Player Charlie: {player_3}")
    print(f"Player Dylan: {player_4}\n")

    print(
        f"All distinct achievements:"
        f"{set.union(player_1, player_2, player_3, player_4)}\n"
    )

    print(
        f"Common achievements: "
        f"{set.intersection(player_1, player_2, player_3, player_4)}\n"
    )

    print(
        f"Only Alice has: "
        f"{set.difference(player_1, player_2, player_3, player_4)}"
    )
    print(
        f"Only Bob has: "
        f"{set.difference(player_2, player_1, player_3, player_4)}"
    )
    print(
        f"Only Charlie has: "
        f"{set.difference(player_3, player_1, player_2, player_4)}"
    )
    print(
        f"Only Dylan has: "
        f"{set.difference(player_4, player_1, player_2, player_3)}\n"
    )

    achievements: set[str] = set(all_achievements())

    print(
        f"Alice is missing: "
        f"{set.difference(achievements, player_1)}"
    )
    print(
        f"Bob is missing: "
        f"{set.difference(achievements, player_2)}"
    )
    print(
        f"Charlie is missing: "
        f"{set.difference(achievements, player_3)}"
    )
    print(
        f"Dylan is missing: "
        f"{set.difference(achievements, player_4)}"
    )


if __name__ == "__main__":
    main()
