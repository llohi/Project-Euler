/*
By considering the terms in the Fibonacci sequence
whose  values do not exceed four million, find the
sum of the even-valued terms.
*/

public class p2 {
    public static void main(String[] args) {
        int current = 1;
        int next = 1;
        int sum = 0;
        int n;

        while (current + next <= 4000000) {

            n = current + next;
            current = next;
            next = n;

            if (n % 2 == 0) {
                sum += n;
            }
        }
        System.out.println(sum);  // 4613732
    }
}
