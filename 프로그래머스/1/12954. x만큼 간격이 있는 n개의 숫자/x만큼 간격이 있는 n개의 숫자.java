class Solution {
    public long[] solution(long x, int n) {
        
        long[] answer = new long[n];
        
        for(int i=1; i<n+1; i++) {
            answer[i-1] = x*i;
        }
        
        
        return answer;
    }
}