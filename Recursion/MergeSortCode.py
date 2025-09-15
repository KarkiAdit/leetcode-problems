class Solution:
    def merge(self, arr, l, m, r):
        i = l
        j = m + 1
        temp = []
        while (i <= m and j <= r):
            if (arr[i] < arr[j]):
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= m:
            temp.append(arr[i])
            i += 1
            
        while j <= r:
            temp.append(arr[j])
            j += 1
        
        for k in range(len(temp)):
            arr[l + k] = temp[k]

    def mergeSort(self, arr, l, r):
        if (l >= r): return
        m = (l + r) // 2
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)
        self.merge(arr, l, m, r)

# Example usage
sol = Solution()
arr = [5, 8, 1, 6, 3, 2]
sol.mergeSort(arr, 0, len(arr) - 1)
print(arr)