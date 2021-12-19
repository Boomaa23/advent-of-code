with open("input/day01.txt", "r") as input:
    increases = -1
    prev = -1
    for line in input.readlines():
        line = int(line)
        if line > prev:
            increases += 1
        prev = line
    print(f"Part 1 - Increases: {increases}")

    input.seek(0)
    lines = input.readlines()
    last_sliding = 0
    sliding = int(lines[0]) + int(lines[1])
    increases = -1
    for counter in range(2, len(lines)):
        sliding += int(lines[counter])
        if sliding > last_sliding:
            increases += 1
        last_sliding = sliding
        sliding -= int(lines[counter - 2])
    print(f"Part 2 - Increases: {increases}")
