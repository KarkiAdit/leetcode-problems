# Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.

# Unoptimized O(n^2) solution
class Solution:
	def lps(self, str):
		# code here
		size = len(str)
		lps = 0
		prefix_start = 0 
		for i in range(size - 1):
		    prefix_end = i
		    suffix_start = size - 1 - i
		    counter = 0
		    for j in range(prefix_start, prefix_end + 1):
		        if str[j] != str[suffix_start + j]:
		            break
		        counter += 1
		    if counter == prefix_end - prefix_start + 1:
		        lps = counter
		return lps