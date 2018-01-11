'use strict';

/*

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].

*/


var convertToBase7 = function(num) {
  if (num == 0)
    return "0";

  let prefix = num < 0 ? '-' : ''
  , res = []
  , base = 7;

  num = Math.abs(num);

  while (num) {
    res.push(num % base);
    num = ~~(num / base);
  }

  return prefix + res.reverse().join('');
};

for (var i = 0; i < 200; i++)
{
  var result = convertToBase7(i)
  console.log(i, result);
}
