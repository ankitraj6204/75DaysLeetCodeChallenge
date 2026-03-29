class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # mapping closing -> opening
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # if opening bracket
            if char in mapping.values():
                stack.append(char)
            else:
                # if stack empty or mismatch
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0