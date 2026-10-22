class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = s.size();
        if(!len) return 0;
        int lenLast = 0;
        for(int i = len-1; i >= 0; i--){
            if(s[i] == ' ') len-=1;
            else break;
        }
        for(int x = 0; x < len; x++){
            if(s[x] == ' ') lenLast = 0;
            else lenLast++;
        }
        return lenLast;
    }
};