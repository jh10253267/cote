import java.util.*;
class Solution {
    //첫 번째 예제
    //70키로인 사람이 100키로 무게제한 보트에 타려면 같이 탈 사람은 30키로 이하여야한다.
    //배열을 탐색한 결과 30키로보다 적게나가는 사람이 없으므로 answer++
    //50키로인 사람이 탈 경우 남은 키로수는 50 50보다 작거나 같은 사람이 같이 탈 수 있다.
    //그러나 최대한 limit에 가까운 사람을 태워야 
    //두 사람의 무게를 더했을 때 100이되므로 answer ++
    //80키로 answer ++
    public int solution(int[] people, int limit) {
int answer = 0;
        Arrays.sort(people);
        int index = 0;
        
        for (int i = people.length - 1; i >= index; i--) {
            if (people[i] + people[index] <= limit) {
                index++;
                answer++;
            }
            else {
                answer++;
            }
        }
        return answer;
    }
}