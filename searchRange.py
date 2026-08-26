# Solution for Leetcode problem "Search for a Range".
# Description:
#  Given an array of integers nums sorted in non-decreasing order, find the starting and ending positions of a given target value.
#  If target is not found in array, return [-1, -1].
#  The algorithm must run in O(log n) runtime complexity.

# Constraints:
# - 0 <= nums.length <= 10^5
# - -10^9 <= nums[i] <= 10^9
# - nums is a non-decreasing array
# - -10^9 <= target <= 10^9

# Complexity:
# - O(log n) runtime.

def searchRange(self, nums: List[int], target: int) -> List[int]:
  # Find the first (leftmost) occurrence of target
  def find_left():

    left, right = 0, len(nums) - 1
    answer = -1

    while left <= right:
      # Find middle value
      mid = (left + right) // 2

      # Target must be in right half
      if nums[mid] < target:
        left = mid + 1

      # Target must be in right half
      elif nums[mid] > target:
        right = mid - 1

      else:
        # Target found
        answer = mid

        # Continue searching left to find earlier occurrences
        right = mid - 1

    return answer

  # Find the last (rightmost) occurrence of target
  def find_right():

    left, right = 0, len(nums) - 1
    answer = -1

    while left <= right:
      # Find middle value
      mid = (left + right) // 2

      # Target must be in the right half
      if nums[mid] < target:
        left = mid + 1

      # Target must be in the left half
      elif nums[mid] > target:
        right = mid - 1

      else:
        # Target found
        answer = mid

        # Continue searching right to find later occurrences
        left = mid + 1

    return answer

  # Return the first and last positions of target
  return [find_left(), find_right()]
  
