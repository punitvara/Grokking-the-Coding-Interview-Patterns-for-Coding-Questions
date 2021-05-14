'''
Problem Statement
Given a string, sort it based on the decreasing frequency of its characters.
Example 1:
Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
Example 2:
Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = {}

        #create freq map of chars
        for i in range(len(s)):
            if s[i] not in freq_map:
                freq_map[s[i]] = 1
            else:
                freq_map[s[i]] += 1

        max_heap = []

        # push freq and char into heap. Push freq negative so maximum freq stays at top
        for char, freq in freq_map.items():
            heappush(max_heap, (-freq, char))

        new_string = []

        # Pop each freq and add those char to list
        while max_heap:
            freq, char = heappop(max_heap)
            print (freq)
            print (char)
            for _ in range(-freq):
                new_string.append(char)

        # join list of char to string
        return ''.join(new_string)

#answer
from heapq import *


def sort_character_by_frequency(str):

  # find the frequency of each character
  charFrequencyMap = {}
  for char in str:
    charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all characters to the max heap
  for char, frequency in charFrequencyMap.items():
    heappush(maxHeap, (-frequency, char))


  # build a string, appending the most occurring characters first
  sortedString = []
  while maxHeap:
    frequency, char = heappop(maxHeap)
    for _ in range(-frequency):
      sortedString.append(char)

  return ''.join(sortedString)


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()


'''
Time complexity
The time complexity of the above algorithm is O(D*logD) where ‘D’ is the number of distinct characters in the input string.
This means, in the worst case, when all characters are unique the time complexity of the algorithm will be O(N*logN)
where ‘N’ is the total number of characters in the string.
Space complexity
The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.
'''
