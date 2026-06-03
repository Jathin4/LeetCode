class Solution(object):
    def shuffle(self, nums, n):
        for i in range(n):
            nums[i] = (nums[i] << 10) | nums[i + n]  # Store both numbers

        for i in range(n - 1, -1, -1):
            y = nums[i] & ((1 << 10) - 1)  # Extract lower 10 bits
            x = nums[i] >> 10               # Extract upper bits
            nums[2 * i] = x
            nums[2 * i + 1] = y
        return nums

        