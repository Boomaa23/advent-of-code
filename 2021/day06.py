def main():
    with open("input/day06.txt", "r") as input:
        line = input.readlines()[0]
        fishes = line.removesuffix("\n").split(",")
        fishes = [int(fish) for fish in fishes]

        sim_fish(fishes, 80)
        print(f"Part 1 - 80 days: {len(fishes)}")
        sim_fish(fishes, 256 - 80)
        print(f"Part 1 - 256 days: {len(fishes)}")

def sim_fish(fishes, num_days):
    for _ in range(num_days):
        for f in range(len(fishes)):
            if fishes[f] == 0:
                fishes[f] = 6
                fishes.append(8)
            else:
                fishes[f] -= 1

if __name__ == "__main__":
    main()