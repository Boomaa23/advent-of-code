def main():
    with open("input/day07.txt", "r") as input:
        line = input.readlines()[0]
        crabs = line.removesuffix("\n").split(",")
        crabs = [int(crab) for crab in crabs]

        crab_range = range(min(crabs), max(crabs))
        min_fuel = float('inf')
        for align in crab_range:
            fuel = sum([abs(crab - align) for crab in crabs])
            if fuel < min_fuel:
                min_fuel = fuel
        print(f"Part 1 - single fuel: {min_fuel}")

        min_fuel = float('inf')
        for align in crab_range:
            fuel = sum([fuel_cost(abs(crab - align)) for crab in crabs])
            if fuel < min_fuel:
                min_fuel = fuel
        print(f"Part 2 - exp fuel: {min_fuel}")

fc_dict = {}
def fuel_cost(diff):
    if diff in fc_dict:
        return fc_dict[diff]
    out = 0
    inc = 1
    for _ in range(diff):
        out += inc
        inc += 1
    fc_dict[diff] = out
    return out

if __name__ == "__main__":
    main()