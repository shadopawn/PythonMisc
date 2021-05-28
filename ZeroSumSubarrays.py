import unittest
from collections import defaultdict

def numberOfTargetSumSubarrays(numbers, targetSum = 0):
    previousSums = defaultdict(lambda: 0)

    zeroSumCount = 0

    currentSum = 0
    for number in numbers:
        currentSum += number
        if currentSum == targetSum:
            zeroSumCount += 1
        
        if (currentSum - targetSum) in previousSums:
            zeroSumCount += previousSums[currentSum - targetSum]
        previousSums[currentSum] += 1
    
    print(previousSums)
    return zeroSumCount


class TestZeroSumSubarrays(unittest.TestCase):

    def test_find_number_of_subarrays_with_zero_sum(self):
        self.assertEqual(numberOfTargetSumSubarrays([1, 2, 3]), 0)
        self.assertEqual(numberOfTargetSumSubarrays([1, -1]), 1)
        self.assertEqual(numberOfTargetSumSubarrays([1, -1, 1, -1]), 4)
        self.assertEqual(numberOfTargetSumSubarrays([2, -2, 3, 0, 4, -7]), 4)


if __name__ == '__main__':
    unittest.main()