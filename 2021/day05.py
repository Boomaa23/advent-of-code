def main():
    with open("input/day05.txt", "r") as input:
        lines = input.readlines()
        pt1_board = [[0]*1000 for _ in range(1000)]
        pt2_board = [[0]*1000 for _ in range(1000)]
        for line in lines:
            a, b, c = line.removesuffix("\n").split(",")
            b = b.split(" -> ")
            x1, y1, x2, y2 = int(a), int(b[0]), int(b[1]), int(c)
            if x1 == x2:
                for y in abs_range(y1, y2):
                    pt1_board[x1][y] += 1
                    pt2_board[x1][y] += 1
            elif y1 == y2:
                for x in abs_range(x2, x1):
                    pt1_board[x][y2] += 1
                    pt2_board[x][y2] += 1
            else:
                x_step = 1 if x2 > x1 else -1
                y_step = 1 if y2 > y1 else -1
                x_ctr, y_ctr = x1, y1
                while x_ctr != x2:
                    pt2_board[x_ctr][y_ctr] += 1
                    x_ctr += x_step
                    y_ctr += y_step
                pt2_board[x_ctr][y_ctr] += 1

        pt1_count = 0
        for row in pt1_board:
            for cell in row:
                if cell >= 2:
                    pt1_count += 1
        pt2_count = 0
        for row in pt2_board:
            for cell in row:
                if cell >= 2:
                    pt2_count += 1
        print(f"Part 1 - horiz/vert: {pt1_count}")
        print(f"Part 2 - w/ diag: {pt2_count}")

def abs_range(a, b):
    return range(min(a, b), max(a, b) + 1)

if __name__ == "__main__":
    main()