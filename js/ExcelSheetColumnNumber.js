/*

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

*/

/**
 * @param {string} s
 * @return {number}
 * method: use of ascii value
 */
var titleToNumber = function(s) {
    var s_lst = s.split("");
    var base = "A".charCodeAt(0)-1;
    var result = 0;
    for (i=0; i<s.length; i++) {
        var val = s_lst[i].charCodeAt(0);
        result += (val-base) * Math.pow(26, (s.length-1-i));
    }
    return result;
};

var s = "ABC";
var res = titleToNumber(s);
document.write(s + "<br>");
document.write(res);