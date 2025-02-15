//일단 스캔하기, 약수의 갯수 O(1)로 알아낼 수 있는 방법 찾아보기
//반복문으로 돌리기.

class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        
        //숫자 범위 탐색하기.
        for(int i=left; i<=right; i++) {
            int cnt = 0;
            for(int j=1; j<=i; j++) {
                if(i % j == 0) {
                    cnt ++;
                }
            }
            if(cnt % 2 == 0) {
                        answer += i;
                    } else {
                        answer -= i;
                    }
        }
        return answer;
    }
}