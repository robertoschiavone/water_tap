# Each water tap costs a variable amount of money
# e.g. 6 water taps
# each company donates a variable amount of money (10-50 euros)
# water tap costs 20, first company puts 10 the other 10 and there are 40 euros left
if __name__ == "__main__":
    taps = [10, 15, 20, 30, 50]
    companies = {"Hulo": 20, "Vattenfall": 30, "JetBrains": 40}

    solution = {}
    providers = []
    for i, tap in enumerate(taps):
        for company, budget in companies.items():
            if tap > 0:
                value = min(budget, tap)
                companies[company] -= value
                tap -= value
                providers += [company]
        if tap == 0:
            solution |= {taps[i]: providers}
        providers = []
        companies = dict(filter(lambda item: item[1], companies.items()))
    print(solution)
