class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Boolean> freq = new HashMap<>();
        for(int i:nums){
            if(freq.getOrDefault(i,false)){
                return true;
            }else{
                freq.put(i, true);
            }
        }
        return false;
    }
}