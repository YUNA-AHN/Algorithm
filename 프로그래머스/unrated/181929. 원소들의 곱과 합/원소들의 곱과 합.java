class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int res1 = 1;
        int res2 = 0;
        for (int i = 0; i < num_list.length; i++){
            res1 *= num_list[i];
            res2 += num_list[i];
        }
        if (res1 < (int) Math.pow(res2, 2)){
            answer = 1;
        }
        return answer;
    }
}