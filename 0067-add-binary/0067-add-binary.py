class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        ans = []

        def calculator(d: str, e: str, f: str) -> str:
            nonlocal carry
            if d == "0" and e == "0" and f == "0":
                carry = "0"
                return "0"
            elif d == "0" and e == "0" and f == "1":
                carry = "0"
                return "1"
            elif d == "0" and e == "1" and f == "0":
                carry = "0"
                return "1"
            elif d == "0" and e == "1" and f == "1":
                carry = "1"
                return "0"
            elif d == "1" and e == "0" and f == "0":
                carry = "0"
                return "1"
            elif d == "1" and e == "0" and f == "1":
                carry = "1"
                return "0"
            elif d == "1" and e == "1" and f == "0":
                carry = "1"
                return "0"
            elif d == "1" and e == "1" and f == "1":
                carry = "1"
                return "1"
            return "0"

        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry == "1":
            x = a[i] if i >= 0 else "0"
            y = b[j] if j >= 0 else "0"
            ans.append(calculator(carry, x, y))
            i -= 1
            j -= 1
        if carry == "1":
            ans.append(carry)

        return "".join(reversed(ans))


