# 210. Course Schedule II


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req_map = {i: [] for i in range(numCourses)}
        for crs_num in prerequisites:
            req_map[crs_num[0]].append(crs_num[1])
        path = set()
        validated = set()
        curr_order = []

        def dfs(crs_num):
            if crs_num in path:
                return False
            if crs_num in validated:
                return True
            path.add(crs_num)
            for req_num in req_map[crs_num]:
                if not dfs(req_num):
                    return False
            path.remove(crs_num)
            validated.add(crs_num)
            curr_order.append(crs_num)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return curr_order
