import java.util.*;

class Solution {
    public String solution(String s) {
        String[] temp = s.split(" ");
        List<Integer> list = new ArrayList<>();

        for (String c : temp) {
            list.add(Integer.parseInt(c));
        }

        int min = Collections.min(list);
        int max = Collections.max(list);

        return min + " " + max;
    }
}