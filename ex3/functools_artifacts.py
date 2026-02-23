from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(operator.add, spells)
    if operation == "multiply":
        return reduce(operator.mul, spells)
    if operation == "max":
        return reduce(max, spells)
    if operation == "min":
        return reduce(min, spells)


def partial_enchanter(base_enchantment) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment with {power} power on {target}"


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> callable:
    @singledispatch
    def spell_system(target: Any) -> str:
        return f"Cannot cast spell on {target} of unknown type."

    @spell_system.register
    def _(damage: int) -> str:
        return f"Damage spell for {damage} points!"

    @spell_system.register
    def _(enchantment: str) -> str:
        return f"Enchantment spell: {enchantment} cast!"

    @spell_system.register(list)
    def _(multi_cast: list[Any]) -> list[str]:
        return [spell_system(t) for t in multi_cast]
    return spell_system


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_num = spell_reducer(num, "add")
    mul_num = spell_reducer(num, "multiply")
    max_num = spell_reducer(num, "max")
    print("Sum:", sum_num)
    print("Product:", mul_num)
    print("Max:", max_num)
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
