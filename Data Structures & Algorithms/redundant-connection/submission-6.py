class Solution:
    def find(self, n, union_find):
        while(n != union_find[n]):
            n = union_find[union_find[n]]
        return n

    def union(self, node1, node2, union_find):
        parent1, parent2 = self.find(node1, union_find), self.find(node2, union_find)
        if parent1 == parent2:
            return False
        union_find[parent1] = min(parent1, parent2)
        union_find[parent2] = min(parent1, parent2)
        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = [i for i in range(len(edges) + 1)]
        for node1, node2 in edges:
            if not self.union(node1, node2, union_find):
                result = [node1, node2]
                break
        return result
