/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/
import java.util.Arrays;
import java.util.Scanner;

public class p7 {
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = Integer.parseInt(s.nextLine());


        System.out.format("The %dth prime is %d", n, getPrime(n));
    }

    // get prime with Sieve of Eratosthenes algorithm
    public static int getPrime(int n) {

        // generate array to represent primes
        int p = 2, i;
        int size = 1000005;
        boolean [] primes = new boolean[size];
        Arrays.fill(primes, (boolean) true);

        // update byte array
        while (p * p <= size) {

            // if prime, update all multiples to false
            if (primes[p]) {
                i = p * p;
                while (i < size) {
                    primes[i] = false;
                    i += p;
                }
            }
            p++;
        }

        int j = 1;
        for (i = 2; i < size; i++) {
            if (primes[i]) {
                j++;
                if (j == n) {
                    return i;
                }
            }
        }
        return -1;
    }
}
