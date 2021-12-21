import itertools

signal_lookup = [
    'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
        'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'
]

def main():
    with open("input/day08.txt", "r") as input:
        lines = input.readlines()
        count = 0
        value = 0
        for line in lines:
            output = line[line.index("|") + 2:len(line) - 1].split(" ")
            output = [sorted(v) for v in output]
            for digit in output:
                digit_len = len(digit)
                if digit_len == 2 or digit_len == 3 or digit_len == 4 or digit_len == 7:
                    count += 1
        print(f"Part 1 - 1478: {count}")
        for p in itertools.permutations('abcdefg'):
            if all(convert(x) in signal_lookup for x in patterns):
                return int(''.join(str(signal_lookup.index(convert(p, x))) for x in outputs))
        print(value)

def convert(p, x):
    return ''.join(sorted(chr(ord('a') + p.index(c)) for c in x))

if __name__ == "__main__":
    main()