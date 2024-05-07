class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for (int i = 0; i < s.length(); i++){
            int num = 0;
            // 대문자인지 소문자인지 체크
            if (s.charAt(i) == ' ') {
                num =  Integer.valueOf(s.charAt(i));
            } else if (Character.isUpperCase(s.charAt(i))) {
                num = ((Integer.valueOf(s.charAt(i)) + n) > 90) ? Integer.valueOf(s.charAt(i)) + n  - 26: Integer.valueOf(s.charAt(i)) + n;
            } else {
                num = ((Integer.valueOf(s.charAt(i)) + n) > 122) ? Integer.valueOf(s.charAt(i)) + n  - 26 : Integer.valueOf(s.charAt(i)) + n;
            }
            
            char ch = (char)num;
            answer += ch;
        }
        return answer;
    }
}