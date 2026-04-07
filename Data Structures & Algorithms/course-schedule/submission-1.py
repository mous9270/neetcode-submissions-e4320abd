class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre=prerequisites
        m={i:[] for i in range(numCourses)}
        for i in pre:
            m[i[0]].append(i[1])
        visiting=set()
        visited=set()
        def dfs(i):
            if i in visited:
                return True
            if i in visiting:
                return False
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
        return len(visited)==numCourses