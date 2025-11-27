import java.util.*;

class Solution {
    private static final HashMap<Character, int[]> location = new HashMap<>();
 
    private static void initLocation() {
        location.put('U', new int[]{0, 1});
        location.put('D', new int[]{0, -1});
        location.put('L', new int[]{-1, 0});
        location.put('R', new int[]{1, 0});
    }
    
    private static boolean isValidMove(int dx, int dy) {
        return -5 <= dx && -5 <= dy && dx <= 5 && dy <= 5;
    }
    
    public int solution(String dirs) {
        HashSet<String> answer = new HashSet<>();
        int x = 0, y = 0;
        initLocation();
        
        for(int i=0; i<dirs.length(); i++) {
            int[] offset = location.get(dirs.charAt(i));
            int dx = x + offset[0];
            int dy = y + offset[1];
            if(!isValidMove(dx, dy)) {
                continue;
            }
            System.out.println(dx + " " + dy);
            
            answer.add(x + " " + y + " " + dx + " " + dy);
            answer.add(dx + " " + dy + " " + x + " " + y);
            
            x = dx;
            y = dy;
        }
        
    
        return answer.size() / 2;
    }
}