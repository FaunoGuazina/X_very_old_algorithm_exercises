package code_signal.smooth_sailing;

import java.util.Arrays;
import java.util.Comparator;

public class AllLongestStrings {

	/**
	 * Given an array of strings, return another array containing all of its longest
	 * strings.
	 * 
	 * Example
	 * 
	 * For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
	 * allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
	 * 
	 * Input/Output
	 * 
	 * [execution time limit] 3 seconds (java)
	 * 
	 * [input] array.string inputArray
	 * 
	 * A non-empty array.
	 * 
	 * Guaranteed constraints: 1 ≤ inputArray.length ≤ 10, 1 ≤ inputArray[i].length
	 * ≤ 10.
	 * 
	 * [output] array.string
	 * 
	 * Array of the longest strings, stored in the same order as in the inputArray.
	 * 
	 * @param inputArray string[]
	 * @return string[]
	 */
	static String[] allLongestStrings(String[] inputArray) {

		return Arrays.stream(inputArray)
				.filter(x -> x.length() == 
					Arrays.stream(inputArray)
						.map(String::length)
						.sorted(Comparator.reverseOrder())
						.findFirst().get())
				.toArray(String[]::new);
	}

}
