class Solution:
    def addDigits(self, num: int) -> int:
        result = num % 9
        n = num / 9
        if result == 0 and n != 0:
            result = 9
        elif num == 0:
            result = 0
        return result

# digital root 原理

# digital root = 0 if n = 0
# = 9 if n = 9k
# = n mod 9 if n!=9k
