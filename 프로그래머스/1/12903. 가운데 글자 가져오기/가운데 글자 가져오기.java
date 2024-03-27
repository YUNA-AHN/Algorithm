class Solution {
    public String solution(String s) {
        String answer = "";
        int slen = s.length();
        answer = (slen % 2 == 0) ? s.substring(slen / 2 - 1, slen / 2 + 1) : s.substring(slen / 2, slen / 2 + 1);
        return answer;
    }
}