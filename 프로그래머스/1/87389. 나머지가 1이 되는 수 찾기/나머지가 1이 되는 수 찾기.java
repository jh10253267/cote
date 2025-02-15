class Solution {
    public int solution(int n) {
        int answer = 0;
        
        
        for(int i=2; i<n; i++) {
            int temp = n/i;
            if(i*temp + 1 == n) {
                answer = i;
                break;
            }
            
        }
        return answer;
    }
}