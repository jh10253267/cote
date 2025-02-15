import java.util.*;
//배열의 경우 수정과 삭제가 어렵다.
//최솟값을 제거한 뒤에도 순서는 그대로여야한다.
//정렬한 후 그 수를 기억.
//그 수만 빼고 원본배열 그대로 넣기.

class Solution {
    public int[] solution(int[] arr) {
        int min = arr[0];
        if(arr.length != 1) {
            
            for(int i = 0; i<arr.length; i++) {
                if(min > arr[i]) {
                    min = arr[i];
                }
            }
             ArrayList<Integer> arr1 = new ArrayList<>();
        
            for(int j = 0; j<arr.length; j++) {
                 if(arr[j] != min) {
                     arr1.add(arr[j]);
                 }
            }
            int[] answer = arr1.stream().mapToInt(x->x).toArray();
            
            return answer;
        } else {
            int[] answer = {-1};
            return answer;
        }
    }
}