'''

In LeetCode Store, there are some kinds of items to sell. Each item has a price.
However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.
You are given the each item's price, a set of special offers, and the number we need to buy for each item. 
The job is to output the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers.
Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer,
other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.

Example 1:
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

Example 2:
Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation: 
The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.

Note:
There are at most 6 kinds of items, 100 special offers.
For each item, you need to buy at most 6 of them.
You are not allowed to buy more items than you want, even if that would lower the overall price.

'''


class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.res = []
        self.n = len(needs)
        self.price = price
        self.dfs(needs, 0, special)
        return min(self.res)

    def dfs(self, cur_needs, cur_cost, special_list):
        valid_special = self.check_valid_special(special_list, cur_needs)
        # No special at first
        new_cost = int(cur_cost)
        for i in range(self.n):
            new_cost += cur_needs[i]*self.price[i]
        self.res.append(new_cost)
        # Yes special
        for special in valid_special:
            next_needs = list(cur_needs)
            for i in range(self.n):
                next_needs[i] -= special[i]
            self.dfs(next_needs, cur_cost+special[-1], special_list)

    def check_valid_special(self, special_list, needs_list):
        valid_special = list()
        # special numbers less than required number
        for special in special_list:
            status = True
            for i in range(len(needs_list)):
                if special[i] > needs_list[i]:
                    # not allowed to buy more than needs
                    status = False
                    break
            if status:
                valid_special.append(special)
        return valid_special
        

if __name__ == "__main__":
    input_price = [2,3,4]
    input_special = [[1,1,0,4],[2,2,1,9]]
    input_needs = [1,2,1]
    solu = Solution()
    print([input_price,input_special,input_needs])
    print(solu.shoppingOffers(input_price,input_special,input_needs))
