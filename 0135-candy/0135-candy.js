/**
 * @param {number[]} ratings
 * @return {number}
 */
// 3,1,0,2 => 3,2,1,2;
// 4,3,2,1 => 4,3,2,1
// 3,4,5,6 => 1,2,3,4
//   ratings[i] = ratings[i] + 1
// ratings[i] += 1
// 
var candy = function(ratings) {
    let candies = 0;
    // let candies = new Array(ratings.length).fill(0);
    let i = 0;
    for(; i < ratings.length; i++){
        candies++;
        let a = i;
        while(a < ratings.length-1 && ratings[a]>ratings[a+1])
            a++;
        a -= i;
        let b = i;
        let c = 0;
        while(b > 0 && ratings[b]>ratings[b-1]){
            b--;
            c++;
        }
        candies += (a>c)?a:c;
        
    }
    return candies;
};