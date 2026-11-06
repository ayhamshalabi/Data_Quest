import sys


def parse_inventory(arguments: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in arguments:
        parts: list[str] = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item: str = parts[0]
        quantity: str = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            inventory[item] = int(quantity)
        except ValueError as err:
            print(f"Quantity error for '{item}': {err}")

    return inventory


def display_inventory_analytics(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    quantity_list: list[int] = list(inventory.values())
    total_quantity: int = sum(quantity_list)
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    if total_quantity > 0:
        for inv_item, inv_quantity in inventory.items():
            percentage: float = (inv_quantity / total_quantity) * 100
            print(f"Item {inv_item} represents {percentage:.1f}%")

    if inventory:
        most_item: str = item_list[0]
        least_item: str = item_list[0]

        for current_item in item_list:
            if inventory[current_item] > inventory[most_item]:
                most_item = current_item
            if inventory[current_item] < inventory[least_item]:
                least_item = current_item

        print(
            f"Item most abundant: {most_item} "
            f"with quantity {inventory[most_item]}"
        )
        print(
            f"Item least abundant: {least_item} "
            f"with quantity {inventory[least_item]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = parse_inventory(sys.argv[1:])

    display_inventory_analytics(inventory)


if __name__ == "__main__":
    main()
