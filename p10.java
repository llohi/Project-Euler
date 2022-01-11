// Find the sum of all the primes below two million.

import java.util.Arrays;

public class p10 {
    public static void main(String[] args) {
        System.out.println(calcSum(2000000));
    }
    public static long calcSum(int n) {

        int size = 10000005;
        boolean[] arr = new boolean[size];
        Arrays.fill(arr, true);
        int p = 2, i;

        while (p * p < size) {

            if (arr[p]) {
                i = p * p;
                while (i < size) {

                    arr[i] = false;
                    i += p;
                }
            }
            p++;
        }

        long sum = 0;
        for (i = 1; i < n; i++) {
            if (arr[i]) {
                sum += i;
            }
        }
        return sum;
    }
}
