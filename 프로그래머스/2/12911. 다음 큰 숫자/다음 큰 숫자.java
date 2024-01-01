class Solution {
    public int solution(int n) {
        int answer = n;
        
        int bit_count =  Integer.bitCount(n);
        while(true) {
            answer++;
            if(Integer.bitCount(answer) == bit_count) {
                break;
            }
        }
        return answer;
    }
}