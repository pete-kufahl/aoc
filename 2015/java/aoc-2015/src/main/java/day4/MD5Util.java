package day4;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5Util {

    public static String md5ReturnHex(String input) {
        try {
            // compute hash with an MD5 MessageDigest instance
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] hashBytes = md.digest(input.getBytes());

            // Convert bytes to hexadecimal format
            StringBuilder hexString = new StringBuilder();
            for (byte b : hashBytes) {
                hexString.append(String.format("%02x", b));
            }

            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("MD5 algorithm not found", e);
        }
    }

    public static int findNumberWithLeadingZeroes(String input, int zeroes) {
        int num = 0;
        String targetPrefix = "0".repeat(zeroes);

        while (true) {
            String candidate = input + String.format("%0" + zeroes + "d", num);
            String hash = md5ReturnHex(candidate);
            if (hash.startsWith(targetPrefix)) {
                return num;
            }
            num++;
        }
    }
}
