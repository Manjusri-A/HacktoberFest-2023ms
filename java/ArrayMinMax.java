import java.util.Arrays;
import java.util.Scanner;

public class ArrayMinMax {
    static void getMinMax(long a[], long n) {
        long maxNo = Long.MIN_VALUE; // Corrected to Long.MIN_VALUE
        long minNo = Long.MAX_VALUE; // Corrected to Long.MAX_VALUE
        for (int i = 0; i < n; i++) {
            if (a[i] > maxNo) {
                maxNo = a[i];
            }
            if (a[i] < minNo) {
                minNo = a[i];
            }
        }
        System.out.println("min = " + minNo);
        System.out.println("max = " + maxNo);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long a[] = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextLong(); // Use nextLong() for long input
        }
        getMinMax(a, n);
        Arrays.sort(a);
        if (n > 3) { // Check if n is greater than 3
            System.out.println("The fourth smallest element is: " + a[3]);
        } else {
            System.out.println("Array does not have enough elements to find the fourth smallest.");
        }
        sc.close(); // Close the scanner to avoid resource leaks
    }
}
