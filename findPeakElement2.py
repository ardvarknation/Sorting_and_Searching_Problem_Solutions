# Solution for LeetCode problem "Find Peak ELement" using recursive search.

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
# - Space: O(log n)

def findPeakElement(self, nums: List[int]) -> int:
  """
  Returns the index of any peak element.
  A peak element is greater than its immediate neigbours.
  """

  def search(left, right):
    # Base case:
    # When the search space has been reduced to a single element,
    # that element is a peak.
    if left == right:
      return left

    # Find the middle index.
    mid = left + (right - left) // 2

    # Compare the middle element with its right neighbour.
    if nums[mid] < nums[mid + 1]:
      # The slope is increasing.
      # Therefore, at least one peak exists in the right half.
      return search(mid + 1, right)
    else:
      # The slope is decreasing (or peak already been passed).
      # Therefore, a peak must exist in the left half, including
      # the middle itself.
      return search(left, mid)

  # Start the recursive binary search.
  return search(0, len(nums) - 1)
