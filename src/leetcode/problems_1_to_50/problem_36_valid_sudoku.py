from collections.abc import Iterator


class Solution:
    """
    Solution to LeetCode problem 36, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/valid-sudoku/
    https://neetcode.io/problems/valid-sudoku

    Given a sudoku board, determine if the board is valid.
    Note that the board is not necessarily full or solvable.
    """

    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            is_valid_row = self.is_valid_group(self.get_row(board, i))
            is_valid_col = self.is_valid_group(self.get_col(board, i))
            is_valid_box = self.is_valid_group(self.get_box(board, i))
            if not is_valid_row or not is_valid_col or not is_valid_box:
                return False
        return True

    def get_row(self, board: list[list[str]], row_index: int) -> Iterator[str]:
        for i in range(9):
            yield board[row_index][i]

    def get_col(self, board: list[list[str]], col_index: int) -> Iterator[str]:
        for i in range(9):
            yield board[i][col_index]

    def get_box(self, board: list[list[str]], box_index: int) -> Iterator[str]:
        row_start = 3 * (box_index // 3)
        col_start = 3 * (box_index % 3)
        for i in range(9):
            row_offset = i // 3
            col_offset = i % 3
            yield board[row_start + row_offset][col_start + col_offset]

    def is_valid_group(self, group: Iterator[str]) -> bool:
        freq = {str(num): 0 for num in range(1, 10)}
        for cell in group:
            if cell == ".":
                continue
            if freq[cell] == 1:
                return False
            freq[cell] = 1
        return True


def test_solution() -> None:
    solution = Solution()
    assert solution.is_valid_sudoku(
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
    assert not solution.is_valid_sudoku(
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "1", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
