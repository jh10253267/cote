class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int a = 0;
        int b = x;
        
        while(true) {
            a += b % 10;
            b =  b/10;
            if(b < 10) {
                a += b;
                break;
            }
        }
        if( x % a != 0) {
            answer = false;
        }
        
        
        return answer;
    }
}