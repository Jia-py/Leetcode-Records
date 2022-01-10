# @algorithm @lc id=2213 lang=python3 weekname=weekly-contest-269
# @title find-all-people-with-secret


from cn.Python3.mod.preImport import *
# @test(6,[[1,2,5],[2,3,8],[1,5,10]],1)=[0,1,2,3,5]
# @test(4,[[3,1,3],[1,2,2],[0,3,3]],3)=[0,1,3]
# @test(5,[[3,4,2],[1,2,1],[2,3,1]],1)=[0,1,2,3,4]
# @test(6,[[0,2,1],[1,3,1],[4,5,1]],1)=[0,1,2,3]
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        import collections
        meeting_lis = sorted(meetings,key=lambda x: x[2])
        print(meeting_lis)
        unionfind = UnionFind()
        unionfind.add(0)
        unionfind.add(firstPerson)
        unionfind.merge(0,firstPerson)
        time_lis = [x[2] for x in meeting_lis]
        counter = collections.Counter(time_lis)
        time_lis = sorted(list(set(time_lis)))
        index = 0
        for time in time_lis:
            people = set()
            for j in range(counter[time]):
                pp1 = meeting_lis[index][0]
                pp2 = meeting_lis[index][1]
                unionfind.add(pp1)
                unionfind.add(pp2)
                unionfind.merge(pp1,pp2)
                index += 1
                people.add(pp1)
                people.add(pp2)
            father = unionfind.find(0)
            for pp in people:
                if unionfind.find(pp) != father:
                    unionfind.father[pp] = None
        ans = []
        father = unionfind.find(0)
        for pp in unionfind.father:
            if unionfind.find(pp) == father:
                ans.append(pp)
        return ans
class UnionFind:
    def __init__(self):
        self.father = {} # key-节点,value-父节点
        self.size_of_set = {} # key-父节点,value-size
        self.num_of_set = 0
    def add(self, x):
        # 点如果已经存在，操作无效
        if x in self.father: return
        # 初始化点的父节点，点所在集合大小，另外使集合数量+1
        self.father[x] = None
        self.num_of_set += 1
        self.size_of_set[x] = 1
    def merge(self, x, y):
        # 找到两个节点的根
        root_x, root_y = self.find(x), self.find(y)
        # 如果不是同一个根则连接
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_set -= 1
            self.size_of_set[root_y] += self.size_of_set[root_x]
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        # 优化步骤，将路径上所有点指向根节点root
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    def get_num_of_set(self):
        return self.num_of_set
    def get_size_of_set(self, x):
        return self.size_of_set[self.find(x)]
                    
                    
