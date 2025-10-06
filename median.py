class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # Partition for nums1
            j = half - i             # Partition for nums2

            # Edge cases
            Aleft = nums1[i - 1] if i > 0 else float("-infinity")
            Aright = nums1[i] if i < m else float("infinity")
            Bleft = nums2[j - 1] if j > 0 else float("-infinity")
            Bright = nums2[j] if j < n else float("infinity")

            # Check if partitions are correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total length
                if total % 2:
                    return min(Aright, Bright)
                # Even total length
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1
