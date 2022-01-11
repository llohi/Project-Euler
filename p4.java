/*
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

public class p4 {
    public static void main(String[] args) {
        int p = 0;
        for (int i = 100; i < 1000; i++) {
            for (int j = 100; j < 1000; j++) {
                if (is_palindrome(i, j)) {
                    p = Math.max(i * j, p);
                }
            }
        }
        System.out.println(p);  // 906609
    }

    // Check if integer is palindrome
    public static boolean is_palindrome(int n, int m) {

        String s = Integer.toString(n * m);
        int len = s.length();
        for (int i = 0; i < len; i++) {
            if (s.charAt(i) != s.charAt(len - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}
