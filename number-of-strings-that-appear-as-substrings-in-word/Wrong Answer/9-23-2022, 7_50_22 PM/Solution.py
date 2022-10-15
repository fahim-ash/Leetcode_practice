// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        list=[]
        for i in range (len(word)):
            if word[:i] not in list and word[i:] not in list:

                list.append(word[:i])
                list.append(word[i:])

        count=0
        for i in patterns:
            if i in list:
                count+=1
                
        return count

        