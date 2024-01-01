class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        int temp;
        int remain = n;
        while(true) {
            temp = (remain / a) * b; // 6
            remain = remain % a + temp; //2 + 6
            answer += temp;
            
            if(remain < a) break;
        }
        
        
        return answer;
    }
}