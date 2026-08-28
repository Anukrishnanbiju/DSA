class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False

        buckets = {}
        w = valueDiff + 1

        def get_bucket(x):
            return x // w

        for i, x in enumerate(nums):
            b = get_bucket(x)

            if b in buckets:
                return True

            if b - 1 in buckets and abs(x - buckets[b - 1]) <= valueDiff:
                return True

            if b + 1 in buckets and abs(x - buckets[b + 1]) <= valueDiff:
                return True

            buckets[b] = x

            if i >= indexDiff:
                old = nums[i - indexDiff]
                del buckets[get_bucket(old)]

        return False