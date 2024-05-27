import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> runner = new HashMap<>();
        for (int i = 0; i < players.length; i++ ) {
            runner.put(players[i], i);
        }
        
        for (String call:callings) {
            int index = runner.get(call);
            String change = players[index - 1];
            players[index] = change;
            players[index - 1] = call;
            
            runner.replace(call, index-1);
            runner.replace(change, index);
        }
        return players;
    }
}