package code_signal.smooth_sailing;

public class CommonCharacterCount {

	/**
	 * Given two strings, find the number of common characters between them.
	 * 
	 * Example
	 * 
	 * For s1 = "aabcc" and s2 = "adcaa", the output should be
	 * commonCharacterCount(s1, s2) = 3.
	 * 
	 * Strings have 3 common characters - 2 "a"s and 1 "c".
	 * 
	 * Input/Output
	 * 
	 * [execution time limit] 3 seconds (java)
	 * 
	 * [input] string s1
	 * 
	 * A string consisting of lowercase English letters.
	 * 
	 * Guaranteed constraints: 1 ≤ s1.length < 15.
	 * 
	 * [input] string s2
	 * 
	 * A string consisting of lowercase English letters.
	 * 
	 * Guaranteed constraints: 1 ≤ s2.length < 15.
	 * 
	 * [output] integer
	 * 
	 * @param s1 String
	 * @param s2 String
	 * @return int
	 */
	static int commonCharacterCount(String s1, String s2) {
		int count = 0;
		String[] aS2 = s2.split("");
		for (String x : s1.split("")) {
			if (s2.contains(x)) {
				for (int i = 0; i < aS2.length; i++) {
					System.out.println("y = " + aS2[i]);
					if (aS2[i].equals(x)) {
						aS2[i] = "";
						count++;
						break;
					}
				}
			}
		}

		return count;
	}

}
