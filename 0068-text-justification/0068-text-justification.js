/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function(words, maxWidth) {
    var result = [];
    var k = 0;
    for(let i = 0; i < words.length;){
        let Width = maxWidth;
        var ans = [];
        do{
            ans.push(words[i]);
            Width--;
            Width -= words[i].length;
            i++;
        }while(words[i] && words[i].length <= Width);
        if(i < words.length && ans.length > 1){
            let line = ans.join(" ");
            Width = maxWidth - line.length;
            let j = 0;
            let a = 1;
            while(Width){
                if(line[j] == " "){
                    line = line.slice(0,j) + " " + line.slice(j,line.length);
                    Width--;
                    j += a;
                }
                j++;
                if( j == line.length) {
                    j = 0;
                    a++;
                }
            }
            result[k] = line;
        }
        else{
            let line = ans.join(" ");
            Width = maxWidth - line.length;
            line = line + " ".repeat(Width);
            result[k] = line;
        }
        k++;
    }
    return result;
};