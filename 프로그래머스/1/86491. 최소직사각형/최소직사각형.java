//추상화해보기
//가로 길이와 세로 길이 최댓값 찾기
//명함을 회전시키는 경우 
//최대길이는 무조건 최댓값
//각각 최대를 찾으면 회전시킬 수 있는 경우 포함 안됨.
//가로 세로 새로운 배열을 만들어서 각각 최댓값 찾기.
//스트림으로 해결할 수 있는지 확인해보기
import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int length = sizes.length;
        int[] a = new int[length];
        int[] b = new int[length];
        //배열 스캔해서 가로길이 세로길이 배열 만들기.
        for(int i=0; i<length; i++) {
            //만약 세로의 길이가 가로의 길이보다 크면 회전시키기.
            if(sizes[i][0] >= sizes[i][1]) {
            a[i] = sizes[i][0]; 
            b[i] = sizes[i][1];
            } else {
                a[i] = sizes[i][1];
                b[i] = sizes[i][0];
            }
        }        
       Arrays.sort(a);
       Arrays.sort(b);
      answer = a[length-1] * b[length-1];
        
      
         
        return answer;
    }
}