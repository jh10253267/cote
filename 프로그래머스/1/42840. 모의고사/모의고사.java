//최대 맞은 문제.
//구해야하는 것 정답을 맞춘사람.
//정답 배열은 한 번만 돌면 되고 각각을 돌면 되지 않을까?
//리턴해야 하는 값은 학생의 고유 숫자.
// 테스트 코드의 배열은 작지만 실제 시험 문제는 10,000문제.
import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] a = {1,2,3,4,5};
        int[] b = {2,1,2,3,2,4,2,5}; 
        int[] c = {3,3,1,1,2,2,4,4,5,5};
        int[] score = {0, 0, 0};
        
        int index = 0;
        for(Integer i : answers) {
          if (i == a[index%5]) score[0]++;
          if (i == b[index%8]) score[1]++;
          if (i == c[index%10]) score[2]++;
          index++;
        }
        
        int max = Math.max(Math.max(score[0], score[1]), score[2]);
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i<score.length; i++) {
            if(score[i] == max) {
                list.add(i+1);
            }
        }
        Integer temp[] = list.toArray(new Integer[list.size()]);
        int[] answer = list.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}