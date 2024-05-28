import java.util.*;
class Solution {
    public ArrayList<Integer> solution(String[] id_list, String[] report, int k) {
        // 신고한 사람 체크
        HashMap<String, HashSet<String>> reportMap = new HashMap<String, HashSet<String>>();
        // 신고 메일 접수
        HashMap<String, Integer> mailMap = new HashMap<>();
        
        // 순회하면서 들어간 신고 체크
        for (String people:report) {
            String reporter = people.split(" ")[0];
            String reported = people.split(" ")[1];

            reportMap.putIfAbsent(reported, new HashSet<String>());
            reportMap.get(reported).add(reporter);
        }
        
        for (String key:reportMap.keySet()){
            if (reportMap.get(key).size() >= k){
                for (String person:reportMap.get(key)){
                    mailMap.putIfAbsent(person, 0);
                    mailMap.replace(person, mailMap.get(person) + 1);
                }
            }
        }
        ArrayList<Integer> answer = new ArrayList<>();
        for (String id:id_list){
            answer.add(mailMap.getOrDefault(id, 0));
        }
        return answer;
    }
}