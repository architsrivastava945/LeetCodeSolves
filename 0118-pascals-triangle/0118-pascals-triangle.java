class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        // for(int i = 1; i <= numRows; i++){
            for(int j = 1; j <= numRows; j++){
                List<Integer> lvl = new ArrayList<>();
                lvl.add(1);
                int num1 = 0, num2 = 1;
                for(; num2 < j-1; num1++, num2++){
                    List<Integer> prevLvl = result.get(j-2);
                    lvl.add(prevLvl.get(num1) + prevLvl.get(num2));
                }
                if(num2 < j) lvl.add(1);
                result.add(lvl);
            }
        // }
        return result;
    }
}