package code_signal.the_journey_begins;

public class CheckPalindrome {

	/**
	 * Given the string, check if it is a palindrome.
	 * 
	 * Example
	 * 
	 * For inputString = "aabaa", the output should be checkPalindrome(inputString)
	 * = true; For inputString = "abac", the output should be
	 * checkPalindrome(inputString) = false; For inputString = "a", the output
	 * should be checkPalindrome(inputString) = true. Input/Output
	 * 
	 * [execution time limit] 3 seconds (java)
	 * 
	 * [input] string inputString
	 * 
	 * A non-empty string consisting of lowercase characters.
	 * 
	 * Guaranteed constraints: 1 ≤ inputString.length ≤ 105.
	 * 
	 * [output] boolean
	 * 
	 * true if inputString is a palindrome, false otherwise.
	 * 
	 * @param inputString
	 * @return boolean
	 */
	static boolean checkPalindrome(String inputString) {
		String toCompare = inputString.trim().toLowerCase();
		return (inputString != null && !inputString.isEmpty()
				&& toCompare.equals(new StringBuffer(toCompare).reverse().toString())) ? true : false;
	}

}
