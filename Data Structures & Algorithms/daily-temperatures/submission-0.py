class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            days = 0
            for j in range(i + 1, len(temperatures)):
                days += 1
                if i != j and temperatures[i] < temperatures[j]:
                    result.append(days)
                    break
                
                if j == len(temperatures) - 1:
                    result.append(0)
        
        result.append(0)
        return result

        