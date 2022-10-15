// https://leetcode.com/problems/validate-ip-address

/**
 * @param {string} queryIP
 * @return {string}
 */
var validIPAddress = function(queryIP) {
    let count=0;
    let count2=0;
    for (let i of queryIP){
        if (i=='.'){
            count=count+1;}
        else if (i==':'){
            count2 =count2+1;
        }
    };console.log(count,count2);
    if (count==3){
        return "IPv4";
          
          }
    else if (count2 ==7){
        return "IPv6";
    } else {
        return "Neither";
    }
    
    
};