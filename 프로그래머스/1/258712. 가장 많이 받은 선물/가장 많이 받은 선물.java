import java.util.*;
class Solution {
    public int solution(String[] friends, String[] gifts) {
        HashMap<String, ArrayList<String>> give = new HashMap<String, ArrayList<String>>();
        HashMap<String, ArrayList<String>> take = new HashMap<String, ArrayList<String>>();
        HashMap<String, Integer> present = new HashMap<>();
        
        for (String gift:gifts){
            String giver = gift.split(" ")[0];
            String taker = gift.split(" ")[1];
            // key가 선물 준 사람
            give.putIfAbsent(giver, new ArrayList<>());
            give.get(giver).add(taker);
            // key가 선물 받은 사람
            take.putIfAbsent(taker, new ArrayList<>());
            take.get(taker).add(giver);
        }
        
        // 순회하면서 ??
        for (int i = 0; i < friends.length; i++) {
            for (int j = i + 1; j < friends.length; j++) {
                String a = friends[i];
                String b = friends[j];
                // a가 b에게 선물 몇번 ? : 배열 null인 경우 체크
                int fromA = Collections.frequency(give.getOrDefault(a, new ArrayList<>()), b);
                // b가 a한테 선물 몇번??
                int fromB = Collections.frequency(give.getOrDefault(b, new ArrayList<>()), a);
                // if문 비교 a가 크다면, b가 크다면, 둘이 동일하다면 => 선물 지수
                if (fromA > fromB) {
                    present.putIfAbsent(a, 0);
                    present.replace(a, present.get(a) + 1);
                } else if (fromA < fromB) {
                    present.putIfAbsent(b, 0);
                    present.replace(b, present.get(b) + 1);
                } else {
                    // 선물 지수 : 준 선물 - 받은 선물
                    int presA = give.getOrDefault(a, new ArrayList<>()).size() - take.getOrDefault(a, new ArrayList<>()).size();
                    int presB = give.getOrDefault(b, new ArrayList<>()).size() - take.getOrDefault(b, new ArrayList<>()).size();
                    if (presA < presB) {
                        present.putIfAbsent(b, 0);
                        present.replace(b, present.get(b) + 1);
                    } else if (presA > presB) {
                        present.putIfAbsent(a, 0);
                        present.replace(a, present.get(a) + 1);
                    }
                }
            }
        }
        
        int answer = (!present.isEmpty()) ? Collections.max(present.values()): 0;
        return answer;
    }
}