class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> hm = new HashMap<>();
        int len = s.length();
        for(int i = 0; i < len; i++){
            char ch = s.charAt(i);
            int freq = hm.getOrDefault(ch, 0);
            hm.put(ch, freq+1);
        }
        for(int i = 0; i < len; i++){
            if(hm.get(s.charAt(i)) == 1) return i;
        }
        return -1;
    }
}