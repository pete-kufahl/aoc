package day7;

import common.OperatorCombinations;

import java.util.List;

public class TestSequences {

    public static boolean testAddMult(long testValue, int[] operands) {
        int n = operands.length;
        if (n == 1) {
            return operands[0] == testValue;
        }
        char[] operators = new char[]{'+', '*'};
        List<char[]> operatorCombinations = OperatorCombinations.generate(n - 1, operators);

        for (char[] ops : operatorCombinations) {
            long result = operands[0];
            for (int i = 0; i < n - 1; i++) {
                if (ops[i] == '+') {
                    result += operands[i + 1];
                } else if (ops[i] == '*') {
                    result *= operands[i + 1];
                }
            }
            if (result == testValue) {
                return true;
            }
        }
        return false;
    }

    public static boolean testAddMultConcat(long testValue, int[] operands) {
        int n = operands.length;
        if (n == 1) {
            return operands[0] == testValue;
        }
        char[] operators = new char[]{'+', '*', '|'};
        List<char[]> operatorCombinations = OperatorCombinations.generate(n - 1, operators);

        for (char[] ops : operatorCombinations) {
            long result = operands[0];
            for (int i = 0; i < n - 1; i++) {
                if (ops[i] == '+') {
                    result += operands[i + 1];
                } else if (ops[i] == '*') {
                    result *= operands[i + 1];
                } else if (ops[i] == '|') {
                    result = Long.parseLong(Long.toString(result) + Integer.toString(operands[i + 1]));
                }
            }
            if (result == testValue) {
                return true;
            }
        }
        return false;
    }
}
