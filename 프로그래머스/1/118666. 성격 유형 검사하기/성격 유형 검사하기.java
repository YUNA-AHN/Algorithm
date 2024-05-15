import java.util.*;
class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        HashMap<String, Integer> test = new HashMap<String, Integer>();
        for (int i = 0; i < survey.length; i++){
            String curStr = "";
            Integer curScore = 0;
            if (choices[i] < 4){
                curStr = String.valueOf(survey[i].charAt(0));
                test.putIfAbsent(curStr, 0);
                curScore = test.get(curStr) + 4 - choices[i];
            } else if (choices[i] > 4) {
                curStr = String.valueOf(survey[i].charAt(1));
                test.putIfAbsent(curStr, 0);
                curScore = test.get(curStr) + choices[i] - 4;
            }
            test.replace(curStr, curScore);
        }
        answer += testCompare(test, "R","T");
        answer += testCompare(test, "C","F");
        answer += testCompare(test, "J","M");
        answer += testCompare(test, "A","N");
        return answer;
    }
    public String testCompare(Map<String, Integer> test, String fst, String sec) {
        return (test.getOrDefault(fst, 0) >= test.getOrDefault(sec, 0)) ? fst : sec;
    }
}