class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        long length = 0;
        int temp  = a + b;
        
        if(a == b) {
            answer = (long)a;
        } else if(a > b) {
            length = Math.abs(a - b) + 1;
            answer = (length*temp)/2;
        } else {
            length = Math.abs(b - a) + 1;
            answer = (length*temp)/2;
        }
        
        return answer;
    }
}