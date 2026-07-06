class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def inout(subset: List[int], comb_sum: int, idx: int):

            if (comb_sum == target):
                result.append(subset)
                return

            if (idx >= len(nums) or comb_sum > target):
                return

            
            subset_in = subset.copy()
            comb_sum_in = comb_sum

            subset_out = subset.copy()
            comb_sum_out = comb_sum

            inout(subset_out, comb_sum_out, idx + 1)

            subset_in.append(nums[idx])
            comb_sum_in += nums[idx]
            inout(subset_in, comb_sum_in, idx)

        result = []

        inout([], 0, 0)

        return result




        