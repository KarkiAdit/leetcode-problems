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
        
# Optimized mathematical solution using O(1) space
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        # Find square and sum for integers in A
        given_integers_sum = 0
        given_integers_square_sum = 0
        for num in A:
            given_integers_sum += num
            given_integers_square_sum += num ** 2
        # Find square and sum for generic n integers
        sum_of_n_integers = 0
        square_sum_of_n_integers = 0
        for n in range(1, len(A) + 1):
            sum_of_n_integers += n
            square_sum_of_n_integers += n ** 2
        # Use formula
        sum_difference = given_integers_sum - sum_of_n_integers
        square_sum_difference = given_integers_square_sum - square_sum_of_n_integers
        sum_a_and_b = square_sum_difference / sum_difference
        a = (sum_a_and_b + sum_difference) // 2
        b = sum_a_and_b - a
        return [int(a), int(b)]  

# Optimized O(n) time and O(1) space solution. Only tuple is changed to list
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        list_A = list(A)
        for num in A:
            curr_val = abs(num)
            if list_A[curr_val - 1] < 0:
                repeated = curr_val
            else:
                list_A[curr_val - 1] *= -1
        for idx in range(len(list_A)):
            if list_A[idx] > 0:
                missing  = idx + 1
                break
        return [repeated, missing]
              
        
            
        
                
        
                
        

        
        
                
        
