class Solution {
    public String minWindow(String s, String t) {
        if (s.length()==0||t.length()==0||s.length()<t.length()){
            return new String();
        }
        int[] map = new int[128];
        int count=t.length();
        int start=0,end=0,mini=Integer.MAX_VALUE,startind=0;

        for (char c:t.toCharArray())
            map[c]++;
        
        char[] s1=s.toCharArray();

        while(end<s1.length){
            if(map[s1[end++]]-- > 0)
                count--;
            while (count==0){
                if(end-start<mini){
                    startind=start;
                    mini=end-start;
                }
                if(map[s1[start++]]++ == 0)
                    count++;
            }
        }

        return mini==Integer.MAX_VALUE ? new String(): new String(s1,startind,mini);

    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.print("Enter string s: ");
        String s = new java.util.Scanner(System.in).nextLine();
        System.out.print("Enter string t: ");
        String t = new java.util.Scanner(System.in).nextLine();

        String result = solution.minWindow(s, t);
        if (result.isEmpty()) {
            System.out.println("No such window exists.");
        } else {
            System.out.println("Minimum window substring: " + result);
        }
    }
}
