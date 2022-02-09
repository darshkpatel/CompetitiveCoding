class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> distinctnums = new HashSet<>();
        for(int num: nums){
            if(distinctnums.contains(num)) return true;
            distinctnums.add(num);
        }
        return false;

    }
}
