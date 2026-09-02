class Solution:
    def solve(self, n, s):
        # code here
        # TBH its copy pasted cuz mind has been rusted due to vibecoding. trying to recover from it
        state = [0] * 26
        occupied = 0
        rejected = 0

        for c in s:
            idx = ord(c) - ord('A')

            # first time arrival
            if state[idx] == 0:
                state[idx] = 1

                # assign computer if available
                if occupied < n:
                    occupied += 1
                    state[idx] = 2
                else:
                    # no computer available
                    rejected += 1

            # departure
            else:
                if state[idx] == 2:

                    # free the computer
                    occupied -= 1

                # reset state
                state[idx] = 0

        return rejected
