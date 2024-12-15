class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        for (int c = (brown - 2) / 2; c >= 3; c--){
            int r = (brown - 2 * (c)) / 2 + 2;
            if ((c - 2) * (r - 2) == yellow){
                answer[0] = c;
                answer[1] = r;
                break;
            }
        }
        return answer;
    }
}