class Solution {
    public String solution(String code) {
        String answer = "";
        String ret = "";
        int mode = 0;
        for(int i = 0; i < code.length(); i++){
            // code[i]가 숫자인지 아닌지 체크 - Character의 isDigit 활용
            // 숫자라면 mode 변경, 아니라면 진행 ~
            if (Character.isDigit(code.charAt(i))) {
                if (mode == 0) {
                    mode = 1;
                } else {
                    mode = 0;
                }
            } else {
                // mode가 0인 경우에는 i가 짝수인 경우에만 추가히가
                if (mode == 0 && i % 2 == 0) {
                    ret += code.charAt(i);
                } else if (mode == 1 && i % 2 == 1){
                    // mode가 1인 경우에는 i가 홀수인 경우에만 추가히기
                    ret += code.charAt(i);
                }
            }
        }
        // 모두 진행한 후에 ret에 아무것도 없다면
        if (ret.length() == 0) {
            answer = "EMPTY";
        } else {
            answer = ret;
        }
        return answer;
    }
}