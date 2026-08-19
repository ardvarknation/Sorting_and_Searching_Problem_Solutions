# Solution for LeetCode problem "Find Peak ELement" using iterative search.

# Description:
# A peak element is an element that is strictly greater than its neighbours.
# Given a 0-indexed array of integers nums, find the peak element, and return
# its index. If the array contains multiple peaks, return the index to any of
# the peaks.
# You may imagine that nums[-1] = nums[n] = -inf. In other words, an element
# is always considered to be strictly greater than a neighbour that is outside
# the array.
# The algorithm must run in O(log n) time.

# Constraints:
- 1 <= nums.length <= 1000
- 2^-31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i.

# Complexity:
# - Time: O(log n)
# - Space: O(1)

def findPeakElement(self, nums: List[int]) -> int:
  """
  Returns the index of any peak element.
  A peak element is greater than its immediate neigbours.
  """

  # Initialise left and right pointers.
  left, right = 0, len(nums) - 1

  # While element on left is smaller than element on right:
  while left < right:

    # Compute middle element.
    mid = left + (right - left) // 2

    # Compare the middle element with middle plus one element.
    if nums[mid] < nums[mid + 1]:

      # Search left half.
      left = mid + 1

    else:

      # Search right half.
      right = mid

  # When left == right, that index is a peak.
  return left
