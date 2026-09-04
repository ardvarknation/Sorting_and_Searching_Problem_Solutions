# Solution 2 (Staircase algorithm) for LeetCode problem "Seach a 2D Matrix II".
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
# - Time: O(m + n)
# - Space: O(1)

from typing import List

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
  if not matrix or not matrix[0]:
    return False
  rows = len(matrix)
  cols = len(matrix[0])

  # Start in the top-right corner
  row = 0
  cols = cols - 1

  while row < rows and col >= 0:
    current = matrix[row][col]

    if current == target:
      return True

    # Current value is too large:
    # everything below is larger,
    # so move left.
    elif current > target:
      col -= 1

    # Current value is too small:
    # everything to the left is also smaller,
    # so move down.
    else:
      row += 1

  return False
  
