//가능여부만 알면 되니 규착이 있는지 생각해보기 시간복잡도 1로 풀 수 있는지 보기
//스택
import java.util.Stack;
class Solution
{
    public int solution(String s)
    {
        int index = 0;
        int answer = 0;
        int length = s.length();

        Stack<Character> stack = new Stack<>();
        for(int i=0; i<length; i++) {
            if(stack.empty()) {
                stack.push(s.charAt(i));
            }
             else if(stack.peek() == s.charAt(i)) {
                stack.pop();
            } else {
                stack.push(s.charAt(i));
            }
        }
        if(stack.empty()) {
            answer = 1;
        } 

        return answer;
    }
}