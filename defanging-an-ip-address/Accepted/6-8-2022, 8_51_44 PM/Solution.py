// https://leetcode.com/problems/defanging-an-ip-address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        replaced_text=address.replace(".","[.]")
        return replaced_text
        