# The sorted list in which we want to search
nums = [2, 5, 8, 12, 16, 20, 24, 28]

# The number we want to find
target = 15

# low stores the index of the first element
low = 0

# high stores the index of the last element
# len(nums) counts the elements (8), so subtract 1 to get index 7
high = len(nums) - 1

# Continue searching while the search range is valid
while low <= high:

    # Calculate the middle index of the current search range
    mid = (low + high) // 2

    # Check whether the middle element is our target
    if nums[mid] == target:

        # If found, display its index
        print(mid)

        # Stop searching because we found the target
        break

    # If the middle element is smaller than the target
    elif nums[mid] < target:

        # Eliminate the left half, including the middle element
        low = mid + 1

    # If the middle element is greater than the target
    else:

        # Eliminate the right half, including the middle element
        high = mid - 1