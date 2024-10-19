import java.util.Scanner;

public class BogoSort {
    void bogoSort(int[] a) {
        while (!isSorted(a)) {
            shuffle(a);
        }
    }

    void shuffle(int[] a) {
        for (int i = 0; i < a.length; i++) { // Start from 0 to include the first element
            swap(a, i, (int)(Math.random() * (i + 1))); // Generate a random index from 0 to i
        }
    }

    void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    boolean isSorted(int[] a) {
        for (int i = 1; i < a.length; i++) {
            if (a[i] < a[i - 1]) {
                return false;
            }
        }
        return true;
    }

    void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();
        int[] a = new int[n];

        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }

        BogoSort ob = new BogoSort();
        ob.bogoSort(a);

        System.out.print("Sorted array: ");
        ob.printArray(a);

        scanner.close(); // Close the scanner to prevent resource leaks
    }
}
