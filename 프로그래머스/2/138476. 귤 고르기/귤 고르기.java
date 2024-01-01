import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        int sum = 0;
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        Arrays.sort(tangerine);
        for(int i : tangerine) {
            map.put(i,  map.getOrDefault(i, 0) + 1);
        }
        //각 값을 조회해서 큰 것부터 작은 것 순으로 정렬
        ArrayList<Integer> list = new ArrayList<>(map.values());
        Collections.sort(list, Collections.reverseOrder());
        for(int i : list) {
            if (sum + i >= k) {
                answer++;
                break;
            } else {
                sum += i;
                answer++;
            }
            }
        
        return answer;
    }
}