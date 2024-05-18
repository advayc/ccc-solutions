class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        c = nums1 + nums2
        c.sort()
        length = len(c)
        if length % 2 != 0:
            return float(c[length // 2])
        else:
            mid1 = c[length // 2 - 1]
            mid2 = c[length // 2]
            return (float(mid1) + float(mid2)) / 2

