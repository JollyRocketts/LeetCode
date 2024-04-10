class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        for i in dic.values():
            if len(i)>=2:
                for j in range(len(i)-1):
                    for l in range(j+1,len(i)):
                        if abs(i[j]-i[l]) <= k:
                            return True
        return False