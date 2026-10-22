class Solution {
public:
    bool isPalindrome(string s) {
        int a = 'a';
        int z = 'z';
        int A = 'A';
        int Z = 'Z';
        std::string str = "";
        for(int i = 0; i < s.size(); i++){
            if(s[i]>= A && s[i]<=Z) str += static_cast<char>(a+((int)s[i])-A);
            else if(s[i]>='0' && s[i]<='9') str += s[i];
            else if(s[i]>=a && s[i]<=z) str += s[i];
        }
        for(int i = 0, j = str.size()-1; i <= j; i++,j--){
            if(str[i] != str[j]) return false;
        }
        return true;
    }
};