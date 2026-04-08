class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m={i:[] for i in range(numCourses)}
        pre=prerequisites
        for i in pre:
            m[i[0]].append(i[1])
        visiting=set()
        visited=set()
        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            for n in m[i]:
                if not dfs(n):
                    return False
            visiting.remove(i)
            visited.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True