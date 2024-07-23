def lengthOfLongestSubstring(s):
    longestSubstring = ''
    longest = 0

    for i in range(len(s)-1):
        substring = s[i]
        for j in range(i+1, len(s)):
            if s[j] not in substring:
                substring = substring + s[j]
            else:
                if len(substring) > longest:
                    longest = len(substring)
                    longestSubstring = substring
                    break

    #return longest
    return len(longestSubstring)


# Example 1:
# Input: 
s = "abcabcbb"
print(lengthOfLongestSubstring(s))
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: 
s = "bbbbb"
print(lengthOfLongestSubstring(s))
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: 
s = "pwwkew"
print(lengthOfLongestSubstring(s))
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
