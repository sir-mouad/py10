def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])
    min_power = min(mages, key=lambda x: x["power"])
    sum_power = sum(map(lambda x: x["power"], mages))
    avg_power = sum_power / len(mages)
    return {"max_power": max_power,
            "min_power": min_power,
            "avg_power": avg_power}


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts = [{"name": "Fire Staff", "power": 92, "type": "magic"},
                 {"name": "Crystal Orb", "power": 85, "type": "magic"}
                 ]
    artifacts_s = artifact_sorter(artifacts)
    i = 0
    for value in artifacts_s:
        print(f"{value['name']} ({value['power']} power)", end="")
        if i + 1 != len(artifacts_s):
            print(" comes before ", end="")
        else:
            print("")
        i += 1
    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    spells = spell_transformer(spells)
    for name in spells:
        print(f"{name} ", end="")
    print("")
