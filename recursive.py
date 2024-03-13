def allocate_budget(taps: list[int], companies: dict[str, int],
                    solution: dict[int, list[str]] = {}) \
        -> dict[int, list[str]]:
    if not taps:
        return solution

    tap = taps[0]
    providers = []

    for company, budget in companies.items():
        if tap > 0:
            value = min(budget, tap)
            companies[company] -= value
            tap -= value
            providers += [company]

    if tap == 0:
        solution |= {taps[0]: providers}

    companies = dict(filter(lambda item: item[1], companies.items()))

    return allocate_budget(taps[1:], companies, solution)


if __name__ == "__main__":
    taps = [10, 15, 20, 30, 50]
    companies = {
        "Hulo": 20,
        "Vattenfall": 30,
        "JetBrains": 40
    }

    solution = allocate_budget(taps, companies)
    print(solution)
