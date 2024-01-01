//규칙에 따라 전부 계산.
//시간복잡도 n
//

class Solution {
    public int solution(int n) {
        
        int m = 1234567;
        //현재 값.
        int fn = 0;
        //바로 전값.
        int f1 = 1;
        //전전값.
        int f0 = 0;
        int temp = 0;
        for(int i=2; i<=n; i++) {
            fn = (f1%m + f0%m)%m;
            temp = fn;
            f0 = f1;
            f1 = temp;
            }
        
        return fn;
    }
}