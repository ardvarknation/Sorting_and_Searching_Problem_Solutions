# Solution for LeetCode problem "Search in a Rotated Sorted Array".
# Description:
#  There is an integer array nums sorted in ascending order (with distinct values).
#  Prior to be being passed to the function, nums is possibly left rotated at an unknown
#  index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ...,
#  nums[n-1], nums[0], nums[1], nums[k-1]] (0-indexed). E.g. [0, 1, 2, 4, 5, 6, 7] might 
#  be left rotated by 3 indices and become [4, 5, 6, 7, 0, 1, 2].
#  Given the array nums after the possible rotation and an integer target, return the 
#  index of the target if it is in nums or -1 if it is not.
#  The algorithm must run in O(log n) runtime complexity.

# Constraints:
# - 1 <= nums.length <= 5000
# - -10^4 <= nums[i] <= 10^4
# - All values of nums are unique
# - nums is an ascending array possibly rotated
# - -10^4 <= target <= 10^4

# Complexity:
# - Time: O(log n)
# - Space: O(n)

def search(self, nums: List[int], target: int) -> int:
  # Initialise pointers for binary search
  left, right = 0, len(nums) - 1

  # Continue searching while search space remains valid
  while left <= right:
    # Find middle index
    mid = (left + right) // 2

    # Target found
    if nums[mid] == target:
      return mid

    # Check if left half is sorted
    if nums[left] <= nums[mid]:
      if nums[left] <= target < nums[mid]:
        # Search left half
        right = mid - 1
      else:
        # Search right half
        left = mid + 1
    else:
      # Determine if the target in sorted right half
      if nums[mid] < target <= nums[right]:
        # Search right half
        left = mid + 1
      else:
        # Search left half
        right = mid - 1

  # Target not found
  return -1
  
