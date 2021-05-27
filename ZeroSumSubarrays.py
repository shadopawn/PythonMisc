import unittest
from collections import defaultdict

def numberOfZeroSumSubarrays(numbers):
    previousSums = defaultdict(lambda: 0)

    zeroSumCount = 0

    currentSum = 0
    for number in numbers:
        currentSum += number
        if currentSum == 0:
            zeroSumCount += 1
        
        if currentSum in previousSums:
            zeroSumCount += previousSums[currentSum]
        previousSums[currentSum] += 1
    
    return zeroSumCount


class TestZeroSumSubarrays(unittest.TestCase):

    def test_find_number_of_subarrays_with_zero_sum(self):
        self.assertEqual(numberOfZeroSumSubarrays([1, 2, 3]), 0)
        self.assertEqual(numberOfZeroSumSubarrays([1, -1]), 1)
        self.assertEqual(numberOfZeroSumSubarrays([2, -2, 3, 0, 4, -7]), 4)


if __name__ == '__main__':
    unittest.main()