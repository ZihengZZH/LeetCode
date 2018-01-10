'''

Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), 
where h is the height of the person 
and k is the number of people in front of this person 
who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

'''


class Solution:
    
    # sort the list (neg) and backwards insert the element with index k
    # since the order is sorted, the insertation follows the order
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        sort = sorted((-x[0], x[1]) for x in people)
        print(sort)
        for p in sort:
            res.insert(p[1], [-p[0], p[1]])
            print("haha",res)
        return res

        
if __name__ == "__main__":
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    solu = Solution()
    print(people)
    print(solu.reconstructQueue(people))
