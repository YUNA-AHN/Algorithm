// 영문자, 대소문자 구분 X  : 다 소문자로 저장
// 11 16 19 20
import java.util.*;
class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        ArrayList<String> pages = new ArrayList<>();
        for (String city:cities){
            String cityName = city.toLowerCase();
            // 포함 여부 체크 -> 지우고 맨 뒤로 보내기
            if(pages.contains(cityName)) {
                pages.remove(cityName);
                pages.add(cityName);
                answer += 1;
            } else {
                // 포함하지 않는다면 -> 캐시 사이즈를 채우지 않은 경우 / 채운 경우
                if (pages.size() < cacheSize) {
                    pages.add(cityName);
                    answer += 5;
                } else if (cacheSize == 0){
                    answer += 5;
                } else {
                    pages.remove(0);
                    pages.add(cityName);
                    answer += 5;
                }
            }
        }
        return answer;
    }
}