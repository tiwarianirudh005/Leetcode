class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Step 1: Different lengths can never be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Create an empty dictionary
        count = {}

        # Step 3: Count every character in s
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        # Step 4: Remove counts using t
        for char in t:

            # Character not present
            if char not in count:
                return False

            count[char] -= 1

            # More occurrences in t than in s
            if count[char] < 0:
                return False

        # Step 5: All counts matched
        return True