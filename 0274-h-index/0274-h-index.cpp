class Solution {
public:
    int hIndex(vector<int>& citations) {
        std::sort(citations.begin(), citations.end());
        int H_index = citations.size();
        for(int i: citations){
            if(i < H_index) H_index--;
        }
        return H_index;
    }
};