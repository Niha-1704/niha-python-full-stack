class Solution: 
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
sol = Solution()
res = sol.sum(num1,num2)
print(res)