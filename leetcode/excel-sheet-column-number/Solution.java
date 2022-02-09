class Solution {
    public int titleToNumber(String columnTitle) {
        // similar to calculating decimal val for base 26 string
        int multiplier = 1;
        int columnVal = 0;
        for(int i=columnTitle.length()-1;i>=0;i--){
            columnVal += ((int)columnTitle.charAt(i)-64)*multiplier;
            multiplier *= 26;
        }
        return columnVal;
    }
}
