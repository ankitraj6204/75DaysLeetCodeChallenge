class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # Step 1: Count frequency manually
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []

        for _ in range(k):
            max_count = -1
            max_num = None

            for num in freq:
                if freq[num] > max_count:
                    max_count = freq[num]
                    max_num = num

            result.append(max_num)

            freq[max_num] = -1   

        return result
