package day5;

import org.junit.jupiter.api.Test;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

class NiceStringCheckerTest {

    private final NiceStringChecker checker = new NiceStringChecker();

    @Test
    void countNiceStrings_part1() throws IOException {
        String input_path = "src/main/resources/day5/input.txt";
        var ans = checker.countNiceStrings(input_path, NiceStringChecker.Ruleset.SET_ONE);
        assertEquals(238, ans);
    }

    @Test
    void countNiceStrings_part2() throws IOException {
        String input_path = "src/main/resources/day5/input.txt";
        var ans = checker.countNiceStrings(input_path, NiceStringChecker.Ruleset.SET_TWO);
        assertEquals(69, ans);
    }

    @Test
    void testOriginalNiceStrings() {
        assertTrue(checker.isNice("ugknbfddgicrmopn"), "Should be nice");
        assertTrue(checker.isNice("aaa"), "Should be nice");
    }

    @Test
    void testOriginalNaughtyStrings() {
        assertFalse(checker.isNice("jchzalrnumimnmhp"), "Should be naughty (no double letter)");
        assertFalse(checker.isNice("haegwjzuvuyypxyu"), "Should be naughty (contains 'xy')");
        assertFalse(checker.isNice("dvszwmarrgswjxmb"), "Should be naughty (only one vowel)");
    }

    @Test
    void testNewNiceStrings() {
        assertTrue(checker.isNiceNewRules("qjhvhtzxzqqjkmpb"), "Should be nice");
        assertTrue(checker.isNiceNewRules("xxyxx"), "Should be nice");
    }

    @Test
    void testNewNaughtyStrings() {
        assertFalse(checker.isNiceNewRules("uurcxstgmygtbstg"), "Should be naughty (no repeating letter with gap)");
        assertFalse(checker.isNiceNewRules("ieodomkazucvgmuy"), "Should be naughty (pair overlaps itself)");
    }
}