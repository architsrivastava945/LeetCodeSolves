class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        boolean flag = false;
        int count = 0;
        for(String x: words){
            for(char y: x.toCharArray()){
                flag = false;
                for(char z: allowed.toCharArray()){
                    if(y == z){
                        flag = true;
                        break;
                    }
                }
                if(flag == false){
                    break;
                }
            }
            if ( flag != false){
                count++;
            }
        }
        return count;
    }
}