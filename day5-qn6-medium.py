# Qn: Repeat and Missing Number Array

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        return_list = [-1, -1]
        unique_num = set()
        for num in A:
            if num not in unique_num:
                unique_num.add(num)
            else:
                return_list[0] = num
        for n in range(1, len(A) + 1):
            if n not in unique_num:
                return_list[1] = n
                break
        return return_list
        
                
        
                
        
