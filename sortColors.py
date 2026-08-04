# Solution for LeetCode problem "Sort Colors", using the Dutch Flag Algorithm.

# Description:
#  Given an array of nums with n objects coloured red, white, or blue, sort them in-place
#  so that objects of the same colour are adjacent, with the colours in order of red, 
#  white and blue, respectively.
#  Solve without library sort function.

# Complexity:
# - Time: O(n)  each element examined only once.
# - Space: O(1)  only three pointers.

def sortColors(self, nums: List[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """

  # Pointer for the next position of 0.
  low = 0

  # Current element being processed.
  mid = 0

  # Pointer for the next position of 2.
  high = len(nums) - 1

  # Continue while there are still unknown elements.
  while mid <= high:

    # Case 1: Found a 0.
    if nums[mid] == 0:
      # Put the 0 in the 0-region.
      nums[low], nums[mid] = nums[mid], nums[low]

      # Expand both the 0-region and the processed region.
      low += 1
      mid += 1

    # Case 2: Found a 1.
    elif nums[mid] == 1:
      # 1 is already in the correct middle region.
      mid += 1

    # Case 3: Found a 2.
    else:
      # Put a 2 in the 2-region.
      nums[mid], nums[high] = nums[high], nums[mid]

      # Shrink the unknown region from the right.
      high -= 1

      # IMPORTANT:
      # Do not increment mid here.
      # The new value swapped into nums[mid]
      # has not been examined yet.
