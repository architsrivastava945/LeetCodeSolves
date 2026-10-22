class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> hm = new HashMap<>();
        for(int i:nums){
            int freq = hm.getOrDefault(i,0);
            hm.put(i,freq+1);
        }
        for(Map.Entry<Integer, Integer> iterator: hm.entrySet()){
            if(iterator.getValue() == 1){
                return iterator.getKey();
            }
        }
        return 0;
    }
}