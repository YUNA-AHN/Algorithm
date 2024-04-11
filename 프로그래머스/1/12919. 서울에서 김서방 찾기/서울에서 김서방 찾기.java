import java.util.Arrays;
class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        int idx = Arrays.asList(seoul).indexOf("Kim");
        answer = String.format("김서방은 %d에 있다", idx);
        return answer;
    }
}