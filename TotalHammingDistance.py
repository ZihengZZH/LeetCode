'''

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

'''


class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) != 2:
            nums.append(nums[0])
        binary = []
        for num in nums:
            print(num)
            binary.append(self.change2Binary(num))
        res = 0
        for num1,num2 in zip(binary[:-1], binary[1:]):
            res += self.hammingDistance(num1,num2)
            #print(num1, num2, res)
        return res

    # Python version causes computational accuracy
    def change2Binary(self, num):
        num_lst = []
        while num/2 != 0:
            num_lst.append(num%2)
            num = int(num/2)
        num_lst.append(num)
        return num_lst[::-1]

    def hammingDistance(self, num1, num2):
        if len(num1) > len(num2):
            max_len = len(num1)
            num2 = (max_len-len(num2))*[0] + num2
        else:
            max_len = len(num2)
            num1 = (max_len-len(num1))*[0] + num1
        dist = 0
        for i in range(max_len):
            if num1[i] != num2[i]:
                dist += 1
        return dist

    # impressive
    def totalHammingDistance_online(self, nums):
        return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))
        


if __name__ == "__main__":
    solu = Solution()
    input_lst = [1,2,3,4,5]
    print(input_lst, solu.totalHammingDistance_online(input_lst))
    print(input_lst, solu.totalHammingDistance(input_lst))
    