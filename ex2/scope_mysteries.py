def mage_counter() -> callable:
    count = 0

    def counter():
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
    def enchantment() -> str:
        nonlocal enchantment_type
        return enchantment_type
    return enchantment


def memory_vault() -> dict[str, callable]:
    pass


if __name__ == "__main__":
    print("\nTesting mage counter...")
    counter1 = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}:", counter1())
    print("\nTesting enchantment factory...")
    enchantment1 = enchantment_factory()