import java.util.Scanner;

public class PalindromeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a string: ");
        String input = scanner.nextLine().trim(); // Trim whitespace
        
        if (input.isEmpty()) {
            System.out.println("Input cannot be empty.");
        } else {
            if (isPalindrome(input)) {
                System.out.println("\"" + input + "\" is a palindrome.");
            } else {
                System.out.println("\"" + input + "\" is not a palindrome.");
            }
        }
        
        scanner.close();
    }

    public static boolean isPalindrome(String str) {
        StringBuilder cleanedStr = new StringBuilder();
        
        // Build a cleaned version of the string
        for (char c : str.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                cleanedStr.append(Character.toLowerCase(c));
            }
        }
        
        // Check for palindrome
        int left = 0;
        int right = cleanedStr.length() - 1;
        
        while (left < right) {
            if (cleanedStr.charAt(left) != cleanedStr.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
}
