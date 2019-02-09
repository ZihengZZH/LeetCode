'''

Implement a MapSum class with insert, and sum methods.
For the method insert, you'll be given a pair of (string, integer). 
The string represents the key and the integer represents the value. 
If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, 
and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5

'''

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map_sum = list()


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        exist = False
        for m in self.map_sum:
            if m[0] == key:
                m[1] = val
                exist = True
        if not exist:
            self.map_sum.append([key, val])
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sum_pre = 0
        for m in self.map_sum:
            if prefix in m[0]:
                sum_pre += m[1]
        return sum_pre


class MapSum_online:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dict[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        res = 0
        for key in self.dict:
            if key.startswith(prefix):
                res += self.dict[key]
            else:
                continue
        return res



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
if __name__ == "__main__":
    obj = MapSum_online()
    print(obj.insert("aa", 3))
    print(obj.sum("a"))
    print(obj.insert("aa", 2))
    print(obj.sum("a"))
