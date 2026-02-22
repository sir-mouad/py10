from functools import reduce, partial
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(operator.add, spells)
    if operation == "multiply":
        return reduce(operator.mul, spells)
    if operation == "max":
        return reduce(max, spells)
    if operation == "min":
        return reduce(min, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    pass


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> callable:
    pass


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_num = spell_reducer(num, "add")
    mul_num = spell_reducer(num, "multiply")
    max_num = spell_reducer(num, "max")
    print("Sum:", sum_num)
    print("Product:", mul_num)
    print("Max:", max_num)
