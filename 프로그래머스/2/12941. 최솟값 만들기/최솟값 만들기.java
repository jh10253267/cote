//곱한 값이 최소가 되는 경우 작은 수 * 작은 수
//제일 큰수 * 제일 작은수
import java.util.*;
class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        int sum = 0;
        int length = A.length;
        Arrays.sort(A);
        Arrays.sort(B);
        for(int i = 0; i<length; i++) {
            sum = sum + (A[i]*B[length-1-i]);
        }
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        

        return sum;
    }
}