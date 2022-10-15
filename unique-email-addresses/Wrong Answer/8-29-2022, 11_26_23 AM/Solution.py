// https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
       
        count=0
        for i in emails:
            if i[-13:]=="@leetcode.com":
                count+=1
        return count