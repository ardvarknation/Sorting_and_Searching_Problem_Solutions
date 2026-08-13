# Solution for LeetCode problem "Find the Kth Largest Element in an Array".
# This solution applies the Quickselect algorithm based on partitioning 
# process from Quicksort.

# Description:
#  Given an integer array nums, and an integer k, return the kth largest 
#  element in the array.
#  Note that it is the kth largest element in sorted order, not the kth
#  distinct element.

# Constraints:
# - 1 <= k <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4

# Complexity: 
# - Time: O(n) average time, O(n^2) when pivot choices are poor.
# - Space: O(1) extra space (excluding recursion stack).

def findKthLargest(self, nums: List[int], k: int) -> int:
  """
  Convert the k-th largest to the equivalent index of the k-th
  smallest element in a sorted array.
  """
  target_index = len(nums) - k

  def quickselect(left, right):
    # Base case: only one element left.
    if left == right:
      return nums[left]

    # Choose the rightmost element as the pivot.
    pivot = nums[right]

    # 'p' tracks where the smaller element should go.
    p = left

    # Partition the array:
    # Move all elements <= pivot to the left side.
    for i in range(left, right):
      if nums[i] <= pivot:
        # Swap the current element into the "smaller elements" region.
        nums[p], nums[i] = nums[i], nums[p]
        p += 1

    # Place the pivot at its final sorted position.
    nums[p], nums[right] = nums[right], nums[p]

    # At this point:
    # - elements to the left of p are <= pivot
    # - nums[p] is the pivot
    # - elements right of p are > pivot

    # If the pivot landed exactly where it needed to, the answer
    # has been found.
    if p == target_index:
      return nums[p]

    # If the target index is to the right, search only the right
    # partition.
    elif p < target_index:
      return quickselect(left, p - 1)

  return quickselect(0, len(nums) - 1)
  
