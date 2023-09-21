class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        String text1 = my_string.substring(0, s);
        answer += text1;
        answer += overwrite_string;
        answer += my_string.substring(s + overwrite_string.length(), my_string.length());
        return answer;
    }
}