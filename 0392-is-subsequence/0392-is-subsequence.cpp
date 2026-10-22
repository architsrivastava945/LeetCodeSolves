class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0;
        int lens = s.size();
        int lent = t.size();
        if(lens < lent){
            for(int j=0; j < lent; j++){
                if(t[j] == s[i]) i++;
            }
        }
        if( i == lens) return true;
        else return false;
    }
};