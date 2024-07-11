class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]

        return len(res) == len(set(res))

def main():
    solution = Solution()
    board = []

    for i in range(9):
        row = []
        for j in range(9):
            cell_value = input(f"Enter value for cell ({i+1},{j+1}): ")
            row.append(cell_value)
        board.append(row)

    if solution.isValidSudoku(board):
        print("The Sudoku board is valid.")
    else:
        print("The Sudoku board is invalid.")

if __name__ == "__main__":
    main()
