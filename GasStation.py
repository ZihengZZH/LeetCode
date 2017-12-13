'''

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

'''

class Solution:
    def canCompleteCircuit(self, gas, cost):
        diff = [a-b for a,b in zip(gas,cost)]
        if sum(diff) < 0:
            return -1
        for i in range(len(diff)):
            if self.complete(diff,i):
                return i
        return -1

    def complete(self, diff, index):
        res = 0
        for i in range(len(diff)):
            res += diff[index]
            if res < 0:
                return False
            if index < len(diff)-1:
                index += 1
            else:
                index = 0
        return True

    def canCompleteCircuit_online(self, gas, cost):
        if len(gas) == 0 or len(cost) == 0:
            return -1
        N = len(gas)
        total = 0
        cur_sum = 0
        start = 0
        for i in range(N):
            diff = gas[i] - cost[i]
            total += diff
            cur_sum += diff
            if cur_sum < 0:
                start = i+1
                cur_sum = 0
        if total < 0:
            return -1
        else:
            return start


if __name__ == "__main__":
    gas = [1,2,3,3]
    cost = [2,1,5,1]
    solu = Solution()
    print(solu.canCompleteCircuit(gas,cost))
    print(solu.canCompleteCircuit_online(gas,cost))


'''

The idea is simple.

1. Whenever the sum is negative, reset it and let the car start from next point.
2. In the mean time, add up all of the left gas to total. If it's negative finally, return -1 since it's impossible to finish.
3. If it's non-negative, return the last point saved in res;

'''
    