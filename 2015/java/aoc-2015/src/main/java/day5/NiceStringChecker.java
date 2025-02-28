package day5;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class NiceStringChecker {

    private static final Set<Character> VERBOTEN_VOWELS = Set.of('a', 'e', 'i', 'o', 'u');
    private static final Set<String> VERBOTEN_COMBOS = Set.of("ab", "cd", "pq", "xy");

    public int countNiceStrings(String fileName, Ruleset rules) throws IOException {
        int niceStrings = 0;
        int totalStrings = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                totalStrings++;
                if (rules == Ruleset.SET_ONE) {
                    if (isNice(line.strip())) {
                        niceStrings++;
                    }
                } else if (isNiceNewRules(line.strip())) {
                    niceStrings++;
                }
            }
        }

        System.out.println("Out of " + totalStrings + " strings, found " + niceStrings + " nice strings");
        return niceStrings;
    }

    public enum Ruleset {
            SET_ONE,
            SET_TWO
    }

    public boolean isNice(String str) {

        int vowelCount = VERBOTEN_VOWELS.contains(str.charAt(0)) ? 1 : 0;
        boolean hasDoubleLetter = false;
        boolean isDisqualified = false;

        for (int i = 1; i < str.length(); i++) {
            String pair = str.substring(i - 1, i + 1);
            if (VERBOTEN_COMBOS.contains(pair)) {
                isDisqualified = true;
                break;
            }
            if (str.charAt(i) == str.charAt(i - 1)) {
                hasDoubleLetter = true;
            }
            if (VERBOTEN_VOWELS.contains(str.charAt(i))) {
                vowelCount++;
            }
        }
        return !isDisqualified && hasDoubleLetter && vowelCount > 2;
    }

    public boolean isNiceNewRules(String str) {
        if (str.length() < 2) return false;

        boolean rule1 = false;
        boolean rule2 = false;
        Map<String, Integer> charPairs = new HashMap<>();

        for (int i = 0; i < str.length() - 1; i++) {
            // Rule 1: A pair of two letters appears at least twice in the string without overlapping
            if (!rule1) {
                String pair = str.substring(i, i + 2);
                if (charPairs.containsKey(pair) && i > charPairs.get(pair)) {
                    rule1 = true;
                } else if (!charPairs.containsKey(pair)) {
                    charPairs.put(pair, i + 1);
                }
            }

            // Rule 2: At least one letter repeats with exactly one letter between them (xyx pattern)
            if (!rule2 && i < str.length() - 2 && str.charAt(i) == str.charAt(i + 2)) {
                rule2 = true;
            }
        }

        return rule1 && rule2;
    }
}
