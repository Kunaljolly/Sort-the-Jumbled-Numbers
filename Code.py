class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        sor = []
        for x in nums:
            t = ''
            for y in str(x):
                t += str(mapping[int(y)])
            sor.append(int(t))
        d = []
        for x in range(len(nums)):
            d.append([nums[x],sor[x]])
        d = sorted(d, key = lambda x: x[1])
        new = [x[0] for x in d]
        return new

            









