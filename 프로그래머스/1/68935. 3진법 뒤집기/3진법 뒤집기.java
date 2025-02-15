// n은 1이상 1억 이하 시간복잡도 n이하로 구하면 됨.
//어떤 수를 3진법으로 변환하려면?
import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        
        while(n > 2) {
            stack.push(n % 3);
            n = n / 3;
            if(n >= 3 && n < 9) {
                stack.push(n % 3);
                stack.push(n/3);
                break;
            }
        }
        int index = 0;
        while(!stack.isEmpty()) {
            answer += (stack.pop()* Math.pow(3, index));
            index ++;
        }
        if(n ==1 ) {
            return 1;
        } else {
        return answer;
        }
    }
}