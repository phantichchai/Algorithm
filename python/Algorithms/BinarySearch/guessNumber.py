class Solution:
    def __init__(self, pick: int):
        self.pick = pick

    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low)//2
            res = self.guess(mid)
            if res == 1:
                low = mid + 1
                print(f"{mid} is too low")
            elif res == -1:
                high = mid - 1
                print(f"{mid} is too high")
            else:
                print(f"{mid} is correct")
                return mid
            
    def guess(self, n: int) -> int:
        if n > self.pick:
            return -1
        elif n < self.pick:
            return 1
        else:
            return 0

if __name__ == "__main__":
    pick = int(input("pick: "))
    n = int(input("n: "))
    solution = Solution(pick)
    solution.guessNumber(n)