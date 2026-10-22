class Solution {
    public String longestCommonPrefix(String[] strs) {
        String preFix = "";
        int minLenght = strs[0].length();
        for(String str : strs){
            int len = str.length();
            if(len < minLenght) minLenght = len;
        }
        for(int i = 0; i < minLenght; i++){
            char ch = strs[0].charAt(i);
            boolean isPrefix = true;
            for(String str : strs){
                if(str.charAt(i) != ch){
                    isPrefix = false;
                    break;
                }
            }
            if(isPrefix) preFix = preFix + ch ;
            else break;
        }
        return preFix;
    }
}