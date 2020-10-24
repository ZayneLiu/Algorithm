

class Solution:

    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        """
        Input: [1,1,0,1,1,1]
        Output: 3
        Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.
        """
        max_ones = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                if max_ones < counter:
                    max_ones = counter
                counter = 0
        return max_ones if max_ones > counter else counter

    def countDigits(self, nums: List[int]) -> int:
        """
        Input: nums = [12,345,2,6,7896]
        Output: 2
        Explanation:
        12 contains 2 digits (even number of digits).
        345 contains 3 digits (odd number of digits).
        2 contains 1 digit (odd number of digits).
        6 contains 1 digit (odd number of digits).
        7896 contains 4 digits (even number of digits).
        Therefore only 12 and 7896 contain an even number of digits.

        Input: nums = [555,901,482,1771]
        Output: 1
        Explanation:
        Only 1771 contains an even number of digits.
        """

        counter = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                counter += 1
        return counter

    def squareAndSort(self, A: [int]) -> int:
        """
        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]

        Input: [-7,-3,2,3,11]
        Output: [4,9,9,49,121]
        """
        for i in range(len(A)):
            A[i] *= A[i]
        return sorted(A)

    def duplicateZeroes(self, arr: [int]) -> None:
        """
        Input: [1,0,2,3,0,4,5,0]
        Output: null
        Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

        Input: [1,2,3]
        Output: null
        Explanation: After calling your function, the input array is modified to: [1,2,3]
        """
        # 1 0 2 3 0 4 5 0
        # 1 0 0 2 3 0 0 4
        # TODO:
        p1 = 0
        for p2 in range(len(arr)):
            if arr[p2] == 0:
                for i in range(len(arr), p2+1):
                    arr[i] = arr[i-1]
                arr[p2] = 0

            p1 += 1

    def mergeSortedArray(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        docstring
        """
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()

    def removeElement(self, nums: [int], val: int) -> int:
        """
        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2]
        Explanation: Your function should return length = 2, with the first two elements of nums being 2.
        It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,3,0,0], your answer will be accepted.

        Input: nums = [0,1,2,2,3,0,4,2], val = 2
        Output: 5, nums = [0,1,4,0,3]
        Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
        """
        p1 = 0
        for p2 in range(len(nums)):
            if nums[p2] != val:
                nums[p1] = nums[p2]
                p1 += 1
        return p1
