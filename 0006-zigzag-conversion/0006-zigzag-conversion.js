/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 0,4,8,12   1,3,5,7,9   2,6,10   => 3 => 4,0  2,2   0,4
 0,6,12     1,5,7,11,13     2,4,8,10    3,9   => 4 => 6,0   4,2     2,4     0,6
 0,8,16,24      1,7, => 5 => 8,0      6,2    4,4     2,6     0,8
 */
var convert = function(s, numRows) {
    let ans = "";
    if(s.length < 2 || numRows < 2) return s;
    let i=[(numRows*2)-2,0];
    for(let a = 0; a < numRows; a++){
        b = a;
        count = 0;
        while(b<s.length){
            if(i[count%2]){
                ans += s[b];
                b += i[count%2];
            }
            count++;
        }
        i[0] -= 2;
        i[1] += 2;
    }
    return ans;
};