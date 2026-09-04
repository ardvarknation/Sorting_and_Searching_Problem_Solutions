# Solution 3 (Divide-and-Conquer Search) for LeetCode problem "Seach a 2D Matrix II".
# Description: 
#   Write an efficient algorithm that searches for a value, target,
#   in an m x n integer matrix, matrix.
#   This matrix has the following properties:
#   - Integers in each row are sorted in ascending order from left to right.
#   - Integers in each column are sorted in ascending order from top to bottom.

# Constraints:
# - m == matrix.length
# - n == matrix[i].length
# - 1 <= n, m <= 300
# - -10^9 <= matrix[i][j] <= 10^9
# - All the integers in each row are sorted in ascending order
# - All the integers in each column are sorted in ascending order
# - -10^9 <= target <= 10^9

# Complexity: 
# - Time: O(m log n) approx.
# - Space: O(log n)

from typing import List

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
  if not matrix or not matrix[0]:
    return False

  rows = len(matrix)
  cols = len(matrix[0])

  # Recursive search function
  def search(left, top, right, bottom):
    # Invalid submatrix
    if left > right or top > bottom:
      return False

    # Target outside the range of this submatrix
    if (
      target < matrix[top][left]
      or target > matrix[bottom][right]
    ):
      return False

    # Choose the middle column
    mid_col = (left + right) // 2

    # Binary-style scan down the middle column
    row = top

    while row <= bottom and matrix[row][mid_col] <= target:
      if matrix[row][mid_col] == target:
        return True
      row += 1

    # Search:
    # 1. Bottom-left region
    # 2. Top-right region
    return (
      search(left, row, mid_col - 1, bottom)
      or
      search(mid_col + 1, top, right, row - 1)
    )

  return search(0, 0, cols - 1, rows - 1)

