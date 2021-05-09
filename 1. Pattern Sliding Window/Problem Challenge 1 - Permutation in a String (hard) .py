'''
Problem Challenge 1
Permutation in a String (hard)
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.
Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
'''


# mycode 1 (not efficient)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Track char freq for s1 string
        s1_map = {}
        #Track char freq for s2 string
        s2_map = {}
        win_start = 0
        if len(s2) < len(s1):
            return False
        #Create hash table for s1 characters
        for i in range(len(s1)):
            if s1[i] not in s1_map:
                s1_map[s1[i]] = 1
            else:
                s1_map[s1[i]] += 1
        # print (s1_map)

        for win_end in range(len(s2)):
            #If character is not present in dict, add to dict else increase freq
            if s2[win_end] not in s2_map:
                s2_map[s2[win_end]] = 1
            else:
                s2_map[s2[win_end]] += 1

            #Main condition is here. Window. Window == len(s1) == sum(s1_map.values()). If window size grows beyond it, remove freq of letter starting from first.
            while sum(s2_map.values()) > sum(s1_map.values()) :

                s2_map[s2[win_start]] -= 1
                #Dont forget to del char when freq is zero else both s1 and s2 map wont match.
                if s2_map[s2[win_start]] == 0:
                    del s2_map[s2[win_start]]
                win_start += 1

            #compare both dict
            if s1_map == s2_map:
                return True

        return False

# mycode2
class Solution: #O(N+M) and O(M)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Track char freq for s1 string
        s1_map = {}
        matched = 0

        win_start = 0
        if len(s2) < len(s1):
            return False

        #Create hash table for s1 characters
        for i in range(len(s1)):
            if s1[i] not in s1_map:
                s1_map[s1[i]] = 1
            else:
                s1_map[s1[i]] += 1
        # print (s1_map)

        for win_end in range(len(s2)):

            if s2[win_end] in s1_map:
                s1_map[s2[win_end]] -= 1
                if s1_map[s2[win_end]] == 0:
                    matched += 1
            # print (s1_map)
            if matched == len(s1_map):
                # print (matched)
                # print (s1_map)
                return True

            if win_end >= len(s1) -1:
                # print (win_end)
                if s2[win_start] in s1_map:
                    # print (s1_map)
                    # print (s2[win_start])
                    # print (matched)
                    if s1_map[s2[win_start]] == 0:
                        matched -= 1
                    s1_map[s2[win_start]] +=  1
                win_start += 1

        return False

#answer
def find_permutation(str, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_frequency:
      # decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):
      return True

    # shrink the window by one character
    if window_end >= len(pattern) - 1:
      left_char = str[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  return False


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()


Time Complexity #
The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity #
The space complexity of the algorithm is O(M) since in the worst case,
the whole pattern can have distinct characters which will go into the HashMap.
