import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int length = arr.length;
        int count = 0;
        
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i<length; i++){
            if(arr[i] % divisor == 0) {
                list.add(arr[i]);
            }
        }
        if(list.size() == 0) {
            int[] answer = {-1};
            return answer;
        } else {
            int[] answer = new int[list.size()];
        int size = 0;
        for(int i : list) {
            answer[size++] = i;
        }
        Arrays.sort(answer);
        return answer;
        }        
        
        
    }
}