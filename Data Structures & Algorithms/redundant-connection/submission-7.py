class Solution:
    def find(self, n, union_find):
        while(n != union_find[n]):
            union_find[n] = union_find[union_find[n]]
            n = union_find[n]
        return n

    def union(self, node1, node2, union_find, size):
        parent1, parent2 = self.find(node1, union_find), self.find(node2, union_find)
        if parent1 == parent2:
            return False
        final_parent = None
        if size[parent1] < size[parent2]:
            size[parent2] += size[parent1]
            final_parent = parent2
        else:
            size[parent1] += size[parent2]
            final_parent = parent1
        union_find[parent1] = final_parent
        union_find[parent2] = final_parent
        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = [i for i in range(len(edges) + 1)]
        size = [1 for i in range(len(edges) + 1)]
        for node1, node2 in edges:
            if not self.union(node1, node2, union_find, size):
                result = [node1, node2]
                break
        return result
