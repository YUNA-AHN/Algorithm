// 교집합 크기 / 합집합 크기
// 대소문자 차이 무시. 두 글자씩 끊어 다중 집합의 원소, 영문으로만 이루어지지 않는 경우 버림
// 자카드 유사도에 * 65536 소수점 아래 버림
import java.util.*;
class Solution {
    public int solution(String str1, String str2) {
        float n = 0, u = 0; // 교집합, 합집합 크기
        Map<String, Integer> map1 = new HashMap<>(); // 첫 번째 문자열 조합
        Map<String, Integer> map2 = new HashMap<>(); // 두 번째 문자열 조합
        // str1 순회
        for (int i = 0; i < str1.length() - 1; i++){
            if (str1.substring(i, i+2).matches("^[a-zA-Z]*$")) {
                String word = str1.substring(i, i+2).toLowerCase();
                map1.putIfAbsent(word, 0);
                map1.replace(word, map1.get(word) + 1);
            }
        }
        // str2 순회
        for (int j = 0; j < str2.length() - 1; j++){
            if (str2.substring(j, j+2).matches("^[a-zA-Z]*$")) {
                String word = str2.substring(j, j+2).toLowerCase();
                map2.putIfAbsent(word, 0);
                map2.replace(word, map2.get(word) + 1);
            }
        }
        // key 순회
        for (String key : map1.keySet()){
            // 둘 모두에 포함된다면 교집합++, 아니라면 합집합++
            if(map2.keySet().contains(key)) {
                u += Math.max(map1.get(key), map2.get(key));
                n += Math.min(map1.get(key), map2.get(key));
            } else {
                u += map1.get(key);
            }
        }
        for (String key : map2.keySet()){
            if(!map1.keySet().contains(key)) {
                u += map2.get(key);
            }
        }
        
        if (u == 0) {
            return 65536;
        } else {
            return (int) Math.floor(n / u * 65536);
        }
    }
}