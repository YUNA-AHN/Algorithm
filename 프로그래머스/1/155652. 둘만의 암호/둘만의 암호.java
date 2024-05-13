import java.util.*;
class Solution {
    public String solution(String s, String skip, int index) {
        List<String> alpha = new ArrayList<>(Arrays.asList("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"));
        for (int i = 0; i < skip.length(); i++) {
            alpha.remove(String.valueOf(skip.charAt(i)));
        }
        String answer = "";
        for (int j = 0; j < s.length(); j++){
            int check = alpha.indexOf(String.valueOf(s.charAt(j)));
            answer += alpha.get((check + index) % alpha.size());
        }
        return answer;
    }
}