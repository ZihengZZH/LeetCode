'''

Reverse bits of a given 32 bits unsigned integer.

Example:
Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.

Follow up:
If this function is called many times, how would you optimize it?

'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ori_bi, ten = 0, 0
        rev_bi, res = 0, 0
        while n > 1:
            #ori_bi += int(n%2) * pow(10, ten)
            #rev_bi += int(n%2) * pow(10, (31-ten))
            res += int(n%2) * pow(2, (31-ten))
            ten += 1
            n /= 2
        return res

    # bin() return the binary representation of an integer.
    def reverseBits_online(self, n):
        return int(bin(n)[-1:1:-1]+'0'*(32-(len(bin(n))-2)),2)
        
        
if __name__ == "__main__":
    solu = Solution()
    print(43261596, solu.reverseBits(43261596))
    print(43261596, solu.reverseBits_online(43261596))
    #assert 10100101000001111010011100 == solu.reverseBits(43261596)
    #assert 111001011110000010100101000000 == solu.reverseBits(43261596)
    assert 964176192 == solu.reverseBits(43261596)
    assert 964176192 == solu.reverseBits_online(43261596)
