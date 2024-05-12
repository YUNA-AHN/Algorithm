class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int plus = 0;
        int check = 0;    
        for (int lotto : lottos) {
            if (lotto == 0){
                plus += 1;
            } else {
                for (int num : win_nums) {
                    if (num == lotto) {
                        check += 1;
                    }
                }
            }
        }
        int[] answer = {winning(check + plus), winning(check)};
        return answer;
    }
    
    public int winning(int n) {
        switch (n) {
            case 6:
                return 1;
            case 5:
                return 2;
            case 4:
                return 3;
            case 3:
                return 4;
            case 2:
                return 5;
            default:
                return 6;
        }
    }
}