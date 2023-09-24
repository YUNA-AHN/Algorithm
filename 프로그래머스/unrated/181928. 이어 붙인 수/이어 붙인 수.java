class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String res_odd = "";
        String res_even = "";
        for (int i=0; i < num_list.length; i ++){
            if (num_list[i] % 2 == 1){
                res_odd += String.valueOf(num_list[i]);
            } else {
                res_even += String.valueOf(num_list[i]);
            }
        }
        answer += Integer.valueOf(res_odd) + Integer.valueOf(res_even);
        return answer;
    }
}