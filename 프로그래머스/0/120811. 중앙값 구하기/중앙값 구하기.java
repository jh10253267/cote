import java.util.Arrays; 

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int len = array.length;
        Arrays.sort(array);
        int midIndex = array.length/2;
        answer = array[midIndex];

        return answer;
    }
}