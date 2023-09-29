import java.util.List;
import java.util.ArrayList;

class Solution {
    // 출력할 자료형으로 변경해주었습니다..
    public List solution(int l, int r) {
        List <Integer> answer = new ArrayList<>();
        // i이상 r 이하의 정수 순회
        for (int i = l; i <= r; i++){
            // 0이나 5로 이루어지려면 일단 5의 배수여야함
            if (i % 5 == 0){
                // 숫자 순회하면서 5와 0인지 체크
                String num = Integer.toString(i); // 문자열로 변경
                Boolean condition = true; // 5와 0으로만 이루어져 있는지 체크
                // num 길이만큼 순회
                for (int j = 0; j < num.length(); j++){
                    // 뽑아온 수자가 5나 0인가요?
                    if (num.charAt(j) == '5' || num.charAt(j) == '0'){
                        condition = true; // 맞으면 true
                    } else {
                        condition = false; // 아니면 false 후 break
                        break;
                    }
                }
                // condtiion이 참이면 i를 추가하기
                if (condition == true){
                    answer.add(i);
                }
            }
            }
        // 배열이 비었다면 -1 입력
            if (answer.isEmpty()){
                answer.add(-1);
        }
        return answer;
    }
}