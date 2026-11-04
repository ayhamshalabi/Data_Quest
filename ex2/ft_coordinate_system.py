import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts: list[str] = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")

        parsed_coords: list[float] = []
        has_error: bool = False

        for part in parts:
            trimmed_part: str = part.strip()
            try:
                parsed_coords.append(float(trimmed_part))
            except ValueError as err:
                print(f"Error on parameter '{trimmed_part}': {err}")
                has_error = True
                break

        if not has_error:
            return (parsed_coords[0], parsed_coords[1], parsed_coords[2])


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()

    print(f"Got a first tuple: ({pos1})")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center: float = calculate_distance(pos1)
    print(f"Distance to center: {dist_center:.4f}")

    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()

    dist_between: float = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    main()