import java.util.*;
class Solution {
    public ArrayList<Integer> solution(String today, String[] terms, String[] privacies) {
        // 약관 입력
        HashMap<String, Integer> condition = new HashMap<String, Integer>();
        for (String term:terms){
            condition.put(term.split(" ")[0], Integer.valueOf(term.split(" ")[1]));
        }
        
        // 개인 정보 순회하면서 체크
        Integer days = 0;
        Integer todays = convert(today);
        
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < privacies.length; i++) {
            days = convert(privacies[i].split(" ")[0]) + condition.get(privacies[i].split(" ")[1] ) * 28 - 1;
            if (days < todays) {
                answer.add(i+1);
            }
        }
        
        return answer;
    }
    
    // 날짜 계산
    public Integer convert(String date) {
        return Integer.valueOf(date.split("\\.")[0]) * 28 * 12 
            + Integer.valueOf(date.split("\\.")[1]) * 28 
            + Integer.valueOf(date.split("\\.")[2]);
    }
    
}