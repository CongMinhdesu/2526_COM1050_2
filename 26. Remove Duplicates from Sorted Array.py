class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = []
        cnt = 0
        if len(nums) == 1:
            return 1
        else:
            for i in range (len(nums) - 1):
                if nums[i] == nums [i+1]:
                    cnt = cnt + 1
                else:
                    k.append(nums[i])
            if nums[len(nums)-1] != nums[len(nums)-2]:
                k.append(nums[len(nums)-1])
            if nums[len(nums)-1] == nums[len(nums)-2]:
                k.append(nums[len(nums)-1])
            nums[:] = k
            return len(nums)
        

        #ahihihihih
        #jljljljljljljljljll
        