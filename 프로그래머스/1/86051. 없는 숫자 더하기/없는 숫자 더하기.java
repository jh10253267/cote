class Solution {
    public int solution(int[] numbers) {
        int sum = 0;
        int length = numbers.length;
        
        for(int i=0; i<length; i++) {
            sum += numbers[i];
        }
        
        return 45 - sum;
    }
}