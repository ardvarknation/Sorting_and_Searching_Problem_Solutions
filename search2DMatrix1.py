# Solution 1 (Binary Search every row) for LeetCode problem "Seach a 2D Matrix II".
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
# - Time: O(m log n)
# - Space: O(1)

from typing import List

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
  rows = len(matrix)

  for row in range(rows):
    # Skip rows where the target cannot possibly exist.
    if target < matrix[row][0] or target > matrix[row][-1]:
      continue

    # Standard binary search on the current row
    left, right = 0, len(matrix[row]) - 1

    while left <= right:
      mid = (left + right) // 2

      if matrix[row][mid] == target:
        return True
      elif matrix[row][mid] < target:
        left = mid + 1
      else:
        right = mid - 1

  return False
  
        
