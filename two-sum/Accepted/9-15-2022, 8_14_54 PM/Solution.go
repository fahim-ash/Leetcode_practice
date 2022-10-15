// https://leetcode.com/problems/two-sum

func twoSum(nums []int, target int) []int {
     length := len(nums)
    var ask []int
    
    for i, num := range nums {
        
        for j := i+1; j < length; j++ {
            if  num + nums[j] == target  {
                ask = append(ask, i, j)
                return ask
            }
        }
        
    }
    
    return ask
}
   
    
    