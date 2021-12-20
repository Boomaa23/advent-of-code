class Board:
    def __init__(self, numbers):
        self.original_numbers = [row[:] for row in numbers]
        self.numbers = numbers

    def mark(self, num):
        for r, row in enumerate(self.numbers):
            for c, cell in enumerate(row):
                if cell == num:
                    self.numbers[r][c] = -1
                    
    
    def check_won(self):
        for r, row in enumerate(self.numbers):
            if sum(row) == -5:
                return True
        rot_num = list(zip(*self.numbers))[::-1]
        for c, col in enumerate(rot_num):
            if sum(col) == -5:
                return True
        return False

    def board_sum(self):
        total = 0
        for row in self.numbers:
            for cell in row:
                total += cell if cell != -1 else 0
        return total

    def reset(self):
        self.numbers = [row[:] for row in self.original_numbers]

    def __repr__(self):
        return str(self.numbers)

    def arr2d_rep(self, arr):
        out = ""
        for line in arr:
            for num in line:
                out += str(num) + " "
            out += "\n"
        return out

def split_board(row):
    out = []
    ctr = 0
    while ctr < len(row):
        out.append(int(row[ctr:ctr + 2]))
        ctr += 3
    return out

def main():
    with open("input/day04.txt", "r") as input:
        lines = input.readlines()
        calls = lines.pop(0).split(",")
        lines_iter = iter(lines)

        boards = []
        while True:
            try:
                next(lines_iter)
                board_nums = [split_board(next(lines_iter)) for _ in range(5)]
                boards.append(Board(board_nums))
            except StopIteration:
                break
        
        has_first_win = False
        for call in calls:
            call = int(call)
            for board in boards:
                board.mark(call)
                if board.check_won():
                    print(f"Part 1 - bingo: {board.board_sum() * call}")
                    has_first_win = True
                    break
            if has_first_win:
                break
        
        for board in boards:
            board.reset()
        losing_board = None
        for call in calls:
            call = int(call)
            for board in boards:
                board.mark(call)
            num_won = sum([1 for board in boards if board.check_won()])
            if not losing_board and num_won == len(boards) - 1:
                losing_board = [board for board in boards if not board.check_won()][0]
            elif losing_board and losing_board.check_won():
                print(f'Part 2 - giant squid: {losing_board.board_sum() * call}')
                return

if __name__ == "__main__":
    main()