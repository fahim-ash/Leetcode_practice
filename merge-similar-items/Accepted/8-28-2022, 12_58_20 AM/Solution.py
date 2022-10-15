// https://leetcode.com/problems/merge-similar-items

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        all_items = items1 + items2
        all_items.sort()
        dict_items = defaultdict(int)
        ans = []
        for i in all_items:
            dict_items[i[0]] += i[1]
        for value, weight in dict_items.items():
            ans.append([value, weight])
        return ans
        