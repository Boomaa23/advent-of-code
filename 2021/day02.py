with open("input/day02.txt", "r") as input:
    pos = 0
    depth_pt1 = 0
    depth_pt2 = 0
    aim = 0

    for line in input.readlines():
        cmd, num = line.split(" ")
        num = int(num)
        if cmd == "forward":
            pos += num
            depth_pt2 += aim * num
        elif cmd == "down":
            depth_pt1 += num
            aim += num
        elif cmd == "up":
            depth_pt1 -= num
            aim -= num
    print(f"Part 1 - pos * depth: {pos * depth_pt1}")
    print(f"Part 2 - pos * depth (aim): {pos * depth_pt2}")
