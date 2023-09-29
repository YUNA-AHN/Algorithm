class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean ans1 = x1 || x2;
        boolean ans2 = x3 || x4;
        boolean answer = ans1 && ans2;
        return answer;
    }
}