import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    total_args: int = len(sys.argv)

    if total_args < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_args - 1}")
        for argv_num in range(1, total_args):
            print(f"Argument {argv_num}: {sys.argv[argv_num]}")

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
