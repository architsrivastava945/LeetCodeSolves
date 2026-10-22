    // let level = 1
    // let i = 0, j = height.length-1;
    // while(i < j){
    //     while(height[i] < level) i++;
    //     while(height[j] < level) j--;
    //     for(let a = i; a < j; a++)
    //         if(height[a]<level)
    //             water++;
    //     level++;
    // }
/**
 * @param {number[]} height
 * @return {number}
 */
function calculate(i, j, height){
    while(height[i]<=height[i+1]) i++;
    while(height[j]<=height[j-1]) j--;
    let well_width= j-i-1;
    if(well_width<1) return 0;
    let max_idx = i+1;
    for(let k = i+2; k<j; k++)
        if(height[max_idx]<height[k])
            max_idx = k;
    let max = height[max_idx];
    let small = (height[i] < height[j])? i: j;
    if(max < height[small])
        return well_width*(height[small]-max) + calculate(i, max_idx, height) + calculate(max_idx, j, height);
    return calculate(i, max_idx, height) + calculate(max_idx, j, height);
};
var trap = function(height) {
    let i = 0, j = height.length-1;
    if(j-i<2) return 0;
    return calculate(i,j,height);
};