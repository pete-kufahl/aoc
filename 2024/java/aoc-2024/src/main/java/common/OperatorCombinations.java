package common;

import java.util.ArrayList;
import java.util.List;

public class OperatorCombinations {
    public static List<char[]> generate(int length, char[] operators) {
        int totalCombinations = (int) Math.pow(operators.length, length);
        List<char[]> combinations = new ArrayList<>(totalCombinations);

        for (int i = 0; i < totalCombinations; i++) {       // i: combination index
            char[] ops = new char[length];
            int temp = i;
            for (int j = 0; j < length; j++) {
                // extract the current digit in base operators.length, map it to an operator
                ops[j] = operators[temp % operators.length];
                // move to the next "digit" by dividing temp by operators.length
                temp /= operators.length;
            }
            combinations.add(ops);
        }
        return combinations;
    }
}