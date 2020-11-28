package code_signal.smooth_sailing;

public class IsLucky {

	/**
	 * Ticket numbers usually consist of an even number of digits. A ticket number
	 * is considered lucky if the sum of the first half of the digits is equal to
	 * the sum of the second half.
	 * 
	 * Given a ticket number n, determine if it's lucky or not.
	 * 
	 * Example
	 * 
	 * For n = 1230, the output should be isLucky(n) = true; For n = 239017, the
	 * output should be isLucky(n) = false. Input/Output
	 * 
	 * [execution time limit] 3 seconds (java)
	 * 
	 * [input] integer n
	 * 
	 * A ticket number represented as a positive integer with an even number of
	 * digits.
	 * 
	 * Guaranteed constraints: 10 ≤ n < 106.
	 * 
	 * [output] boolean
	 * 
	 * true if n is a lucky ticket number, false otherwise.
	 * 
	 * @param n
	 * @return
	 */
	static boolean isLucky(int n) {
		String y = Integer.toString(n);
		int x = y.length() / 2;
		String a = y.substring(0, x);
		String b = y.substring(x);
		int A = 0;
		int B = 0;
		for (String s : a.split("")) {
			A += Integer.parseInt(s);
		}
		for (String s : b.split("")) {
			B += Integer.parseInt(s);
		}
		return A == B;
	}

}
