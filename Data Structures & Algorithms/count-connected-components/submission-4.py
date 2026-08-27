class Solution:
    def find(self, n, union_find):
        while n != union_find[n]:
            union_find[n] = union_find[union_find[n]]
            n = union_find[n]
        return n
    

    def union(self, n1, n2, union_find, size):
        parent1, parent2 = self.find(n1, union_find), self.find(n2, union_find)
        if parent1 == parent2:
            return False
        final_parent = None
        if size[parent1] < size[parent2]:
            final_parent = parent2
            size[parent2] += size[parent1]
        else:
            final_parent = parent1
            size[parent1] += size[parent2]
        union_find[parent1] = union_find[parent2] = final_parent
        return True

        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = list(range(n))
        size = [1] * n
        comp = n
        for n1, n2 in edges:
            comp -= self.union(n1, n2, union_find, size)
        return comp
            
        