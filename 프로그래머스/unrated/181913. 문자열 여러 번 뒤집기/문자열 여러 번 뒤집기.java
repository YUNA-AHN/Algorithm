class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuffer res = new StringBuffer(my_string);
        for (int i=0; i < queries.length; i++){
            int s = queries[i][0];
            int e = queries[i][1];
            
            String text = res.substring(s, e+1);
            StringBuffer reversed = new StringBuffer(text);
            reversed.reverse();
            res.replace(s, e+1, reversed.toString());
        }
        return res.toString();
    }
}