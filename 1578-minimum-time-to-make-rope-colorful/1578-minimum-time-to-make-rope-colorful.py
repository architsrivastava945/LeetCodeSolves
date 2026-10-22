class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        List = []
        for i in range(len(colors)-1):
            List.append(neededTime[i])
            if colors[i] != colors[i+1]:
                List.sort()
                time += sum(List[:-1])
                List = []
        List.append(neededTime[-1])
        List.sort()
        return time + sum(List[:-1])
        