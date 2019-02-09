/*

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 * method: two arrays to store number & freq 
 */
var topKFrequent = function(nums, k) {
    nums.sort(function(a,b){return a-b});
    var number = [], freq = [], res = [], prev;
    for (var i=0; i<nums.length; i++) {
        if (nums[i] !== prev) {
            number.push(nums[i]);
            freq.push(1);
        }
        else {
            freq[freq.length-1]++;
        }
        prev = nums[i];
    }
    //document.write(number + "<br>");
    //document.write(freq + "<br>");
    for (var j=0; j<k; j++) {
        var id = indexOfMax(freq);
        //document.write(id + "<br>");
        res.push(number[id]);
        freq[id] = Number.MIN_SAFE_INTEGER;
        //document.write(res + "<br>");
    }
    return res;
};

var indexOfMax = function(arr) {
    if (arr.length === 0) {
        return -1;
    }
    var max = arr[0];
    var maxIndex = 0;
    for (var i=0; i<arr.length; i++) {
        if (arr[i] > max) {
            maxIndex = i;
            max = arr[i];
        }
    }
    return maxIndex;
}

var num_lst = new Array(1,10,1,1,12,20,2,3,3,4,5,6,4,6,7,8);
var k = 2;
var res = topKFrequent(num_lst, k);
document.write(num_lst + "<br>");
document.write(k + "<br>");
document.write(res);


