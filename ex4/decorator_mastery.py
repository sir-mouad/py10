from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper() -> str:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func()
        end = time.time()
        print(f"Spell completed in {end-start:4f} seconds")
        return result
    return wrapper


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


def power_validator(min_power: int) -> callable:
    def decorator(func) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            power = args[-1] if args else kwargs.get('power', 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(7)
def fireball_power(power) -> str:
    return f"Fireball cast with power {power}!"


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(power: int) -> str:
            attempt = 1
            while max_attempts >= attempt:
                try:
                    power += 1
                    return func(power)
                except Exception as e:
                    print(f"{e}, retrying... (attempt "
                          f"{attempt}/{max_attempts})")
                attempt += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(5)
def check_power(power: int):
    if power < 10:
        raise Exception("Spell failed")
    return f"Fireball cast with power {power}!"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for c in name:
            if not (c.isspace() or c.isalpha()):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == "__main__":
    print("\nTesting spell timer...\n")
    print("Result: ", fireball())
    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name("Jordan"))
    print(mage.validate_mage_name(""))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 5))
