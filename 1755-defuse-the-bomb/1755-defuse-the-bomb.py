class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        new_arr = [0]*len(code)

        sub_sum = 0
        window = 0
        init=0

        if k >= 0:

            k = k % len(code)

            for i in range(1, len(code)+k):

                index = i % (len(code))
                sub_sum += code[index]
                window += 1

                if window == k:
                    new_arr[index - k] = sub_sum
                    sub_sum -= code[index-k+1]
                    window -= 1

            return new_arr

        if k < 0:

            start = len(code)+k

            for i in range(start, len(code) + start - k + 1):

                index = i % (len(code))
                sub_sum += code[index]
                window += 1

                if window == -k:

                    new_arr[init] = sub_sum
                    sub_sum -= code[start]
                    window -= 1
                    start = (start + 1) % len(code)
                    init = (init + 1) % len(code)

            return new_arr