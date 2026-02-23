from typing import Any


def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def power_accumulator() -> int:
        nonlocal total
        total += initial_power
        return total
    return power_accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any | str:
        if key in memory:
            return memory[key]
        return "Memory not found"
    return {"store": store,
            "recall": recall}


if __name__ == "__main__":
    print("\nTesting mage counter...")
    counter1 = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}:", counter1())
    print("\nTesting enchantment factory...")
    enchantment1 = enchantment_factory("Flaming")
    print(enchantment1("Sword"))
    enchantment1 = enchantment_factory("Frozen")
    print(enchantment1("Shield"))
