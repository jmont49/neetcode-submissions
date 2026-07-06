class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def inout(subset: List[int], idx: int):

            if idx >= len(nums):
                return

            subset_in = subset.copy()
            subset_in.append(nums[idx])
            result.append(subset_in)

            subset_out = subset

            inout(subset_in, idx + 1)
            inout(subset_out, idx + 1)


        result = [[]]

        inout([], 0)

        return result

        


        