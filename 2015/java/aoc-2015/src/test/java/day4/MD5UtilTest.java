package day4;

import org.junit.jupiter.api.Test;

import static day4.MD5Util.findNumberWithLeadingZeroes;
import static day4.MD5Util.md5ReturnHex;
import static org.junit.jupiter.api.Assertions.*;

class MD5UtilTest {

    private static final String INPUT = "ckczppom";

    @Test
    void PART_ONE() {
        final int ZEROES = 5;

        int result = findNumberWithLeadingZeroes(INPUT, ZEROES);

        // Compute MD5 hash of the found result
        String md5Hash = md5ReturnHex(INPUT + String.format("%0" + ZEROES + "d", result));

        System.out.println("PART ONE --> testing " + result + " ....");
        // Check if the hash starts with the required number of zeroes
        assertTrue(md5Hash.startsWith("0".repeat(ZEROES)),
                "Hash " + md5Hash + " does not start with " + ZEROES + " zeroes");
    }

    @Test
    void PART_TWO() {
        final int ZEROES = 6;

        int result = findNumberWithLeadingZeroes(INPUT, ZEROES);

        // Compute MD5 hash of the found result
        String md5Hash = md5ReturnHex(INPUT + String.format("%0" + ZEROES + "d", result));

        System.out.println("PART TWO --> testing " + result + " ....");
        // Check if the hash starts with the required number of zeroes
        assertTrue(md5Hash.startsWith("0".repeat(ZEROES)),
                "Hash " + md5Hash + " does not start with " + ZEROES + " zeroes");
    }
}