/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
*/

public class p5 {
    public static void main(String[] args) {
        int n = 1;
        int m = 1;

        while (m <= 20) {

            if (n % m == 0) {
                m++;
            } else {
                for (int i = 2; i < m + 1; i++) {
                    if ((n * i) % m == 0) {
                        n *= i;
                        m++;
                        break;
                    }
                }
            }
        }
        System.out.println(n);  // 232792560
    }
}
