BINARY_LEN = 12

def main():
    with open("input/day03.txt", "r") as input:
        bit_ctr = [0]*BINARY_LEN
        lines = input.readlines()
        for line in lines:
            for idx, bit in enumerate(line[:BINARY_LEN]):
                bit_ctr[idx] += int(bit)

        gamma = 0
        epsilon = 0
        for idx, count in enumerate(bit_ctr):
            bin_exp = BINARY_LEN - idx - 1
            if count > len(lines) / 2:
                gamma += pow(2, bin_exp)
            else:
                epsilon += pow(2, bin_exp)
        print(f"Part 1 - gamma * epsilon: {gamma * epsilon}")

        o2 = lines[:]
        co2 = lines[:]
        for idx in range(BINARY_LEN):
            if len(o2) != 1:
                o2 = proc_mcb(o2, idx, True)
            if len(co2) != 1:
                co2 = proc_mcb(co2, idx, False)
        o2_out = int(o2[0], 2)
        co2_out = int(co2[0], 2)
        print(f"Part 2 - life support: {o2_out * co2_out}")


def proc_mcb(lines, idx, keep_mcb):
    mcb = int(sum([int(line[idx]) for line in lines]) >= len(lines) / 2)
    out = []
    for line in lines:
        line = line[:BINARY_LEN]
        if keep_mcb and int(line[idx]) == mcb:
            out.append(line)
        if not keep_mcb and int(line[idx]) != mcb:
            out.append(line)
    return out

if __name__ == "__main__":
    main()