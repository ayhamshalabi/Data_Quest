import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]

    while True:
        player: str = random.choice(players)
        action: str = random.choice(actions)
        yield (player, action)


def consume_event(
    events_list: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events_list) > 0:
        index: int = random.randrange(len(events_list))
        event: tuple[str, str] = events_list.pop(index)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream: typing.Generator[tuple[str, str], None, None] = gen_event()

    for i in range(1000):
        player, action = next(stream)
        print(f"Event {i}: Player {player} did action {action}")

    events_list: list[tuple[str, str]] = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
