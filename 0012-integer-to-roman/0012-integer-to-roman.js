/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let I4 = Math.trunc(num/1000);
    num -= I4*1000;
    let I3 = Math.trunc(num/100);
    num -= I3*100;
    let I2 = Math.trunc(num/10);
    num -= I2*10;
    let I1 = num;
    let str1 = str2 = str3 = str4 = "";
    for(let i = 0; i < I4; i++)
        str4 += "M";
    if(I3 > 0)
        if(I3 > 4)
            if(I3 == 9) str3 += "CM";
            else{
                str3 += "D";
                for(let i = 0; i < I3-5; i++)
                    str3 += "C";
            }
        else
            if(I3 == 4) str3 += "CD";
            else
                for(let i = 0; i < I3; i++)
                    str3 += "C";
    if(I2 > 0)
        if(I2 > 4)
            if(I2 == 9) str2 += "XC";
            else{
                str2 += "L";
                for(let i = 0; i < I2-5; i++)
                    str2 += "X";
            }
        else
            if(I2 == 4) str2 += "XL";
            else
                for(let i = 0; i < I2; i++)
                    str2 += "X";
    if(I1 > 0)
        if(I1 > 4)
            if(I1 == 9) str1 += "IX";
            else{
                str1 += "V";
                for(let i = 0; i < I1-5; i++)
                    str1 += "I";
            }
        else
            if(I1 == 4) str1 += "IV";
            else
                for(let i = 0; i < I1; i++)
                    str1 += "I";

    return str4 + str3 + str2 + str1;
};