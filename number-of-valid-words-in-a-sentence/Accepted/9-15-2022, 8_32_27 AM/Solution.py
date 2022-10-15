// https://leetcode.com/problems/number-of-valid-words-in-a-sentence

class Solution:
    def countValidWords(self, sentence: str) -> int:
        token_regex = re.compile(r'^([a-z]{1,}(\-[a-z]{1,})?[\.,!]?|[\.,!])$')
        return sum([1 for token in sentence.split()if re.search(token_regex, token)])
        

            
        