# 207. Course Schedule


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Construct an adjacency table
        requisites_map = {i: [] for i in range(numCourses)}
        for course in prerequisites:
            requisites_map[course[0]].append(course[1])
        # Tracks visited courses which are not yet checked
        visited = set()

        def dfs(course_num):
            if course_num in visited:
                return False
            if requisites_map[course_num] == []:
                return True
            # Mark the course as visited before checking if it can be completed
            visited.add(course_num)
            # Visit the course prequisites
            for pre_req in requisites_map[course_num]:
                if not dfs(pre_req):
                    return False
            # Remove course from visited after validation
            visited.remove(course_num)
            # Empty course prerequisites to avoid unecessary course validation from now
            requisites_map[course_num] = []
            return True

        # Check if all possible unconnected courses can be completed
        for course_num in range(numCourses):
            if not dfs(course_num):
                return False
        # If all courses can be completed
        return True
