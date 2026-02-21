def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(target) -> tuple:
        return spell1(target), spell2(target)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def mega_fireball() -> int:
        return base_spell() * multiplier
    return mega_fireball


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(target: str) -> str:
        if condition(target):
            return spell(target)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def casts(target: str) -> list:
        result = []
        for spell in spells:
            result.append(spell(target))
        return result
    return casts


if __name__ == "__main__":
    print("\nTesting spell combiner...")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"
    combined = spell_combiner(fireball, heal)
    combined_l = combined("Dragon")
    len(combined_l)
    i = 0
    for value in combined_l:
        print(value, end="")
        if i + 1 != len(combined_l):
            print(", ", end="")
        i += 1
    print("")
    print("\nTesting power amplifier...")

    def fireball():
        return 10
    Original = fireball()
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {Original}, Amplified: {mega_fireball()}")
