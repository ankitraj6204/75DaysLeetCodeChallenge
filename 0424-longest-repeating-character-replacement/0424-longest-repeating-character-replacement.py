class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            # update frequency
            index = ord(s[right]) - ord('A')
            count[index] += 1

            # track max frequency in window
            max_freq = max(max_freq, count[index])

            # if window is invalid, shrink it
            while (right - left + 1) - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            # update result
            result = max(result, right - left + 1)

        return result
        