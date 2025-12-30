import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        HashSet<Integer> numSet = new HashSet<>();
        int length = numbers.length;
        for(int i=0; i<length; i++) {
            for(int j=i+1; j<length; j++) {
                numSet.add(numbers[i] + numbers[j]);
            }
        }
        
        return numSet.stream()
            .sorted()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}