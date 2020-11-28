package code_signal.edge_of_the_ocean;

import java.util.Arrays;

public class MakeArrayConsecutive2 {

	/**
	 * Ratiorg got statues of different sizes as a present from CodeMaster for his
	 * birthday, each statue having an non-negative integer size. Since he likes to
	 * make things perfect, he wants to arrange them from smallest to largest so
	 * that each statue will be bigger than the previous one exactly by 1. He may
	 * need some additional statues to be able to accomplish that. Help him figure
	 * out the minimum number of additional statues needed.
	 * 
	 * Example
	 * 
	 * For statues = [6, 2, 3, 8], the output should be
	 * makeArrayConsecutive2(statues) = 3.
	 * 
	 * Ratiorg needs statues of sizes 4, 5 and 7.
	 * 
	 * Input/Output
	 * 
	 * [execution time limit] 3 seconds (java)
	 * 
	 * [input] array.integer statues
	 * 
	 * An array of distinct non-negative integers.
	 * 
	 * Guaranteed constraints: 1 ≤ statues.length ≤ 10, 0 ≤ statues[i] ≤ 20.
	 * 
	 * [output] integer
	 * 
	 * The minimal number of statues that need to be added to existing statues such
	 * that it contains every integer size from an interval [L, R] (for some L, R)
	 * and no other sizes.
	 * 
	 * @param statues
	 * @return
	 */
	static int makeArrayConsecutive2(int[] statues) {
		Arrays.sort(statues);
		int count = 0;
		for (int i = 0; i < statues.length - 1; i++) {
			int diference = (statues[i + 1] - statues[i]) - 1;
			count += (diference > 0) ? diference : 0;
		}
		return count;
	}

}
