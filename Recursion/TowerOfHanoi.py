# You are given n disks placed on a starting rod (from), with the smallest disk on top and the largest at the bottom. There are three rods: the starting rod(from), the target rod (to), and an auxiliary rod (aux).
# You have to calculate the total number of moves required to transfer all n disks from the starting rod to the target rod, following these rules:
#       1. Only one disk can be moved at a time.
#       2. A disk can only be placed on top of a larger disk or on an empty rod.
# Return the number of moves needed to complete the task.


class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        # code here
        if n == 1: 
            # print(f"move disk {n} from rod {fromm} to rod {to}")
            return 1
        # Move rods from to auxiliary
        count = self.towerOfHanoi(n-1, fromm, aux, to)
        # print(f"move disk {n} from rod {fromm} to rod {to}")
        count += 1
        # Move rods auxiliary to to
        count += self.towerOfHanoi(n-1, aux, to, fromm)
        return count
            
            