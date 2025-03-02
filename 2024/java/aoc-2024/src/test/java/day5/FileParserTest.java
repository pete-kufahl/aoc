package day5;

import org.junit.jupiter.api.Test;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.*;

public class FileParserTest {

    @Test
    void testParseFile_ValidInput() throws IOException {
        String content = "1|2\n3|4\n\n5,6,7\n8,9,10\n";
        Path tempFile = Files.createTempFile("test", ".txt");
        Files.write(tempFile, content.getBytes());

        FileParser.ParsedData result = FileParser.parseFile(tempFile.toString());

        assertEquals(2, result.rules().size());
        assertArrayEquals(new int[]{1, 2}, result.rules().get(0));
        assertArrayEquals(new int[]{3, 4}, result.rules().get(1));

        assertEquals(2, result.updates().size());
        assertArrayEquals(new int[]{5, 6, 7}, result.updates().get(0));
        assertArrayEquals(new int[]{8, 9, 10}, result.updates().get(1));

        Files.deleteIfExists(tempFile);
    }

    @Test
    void testParseFile_EmptyFile() throws IOException {
        Path tempFile = Files.createTempFile("empty", ".txt");
        Files.write(tempFile, "".getBytes());

        FileParser.ParsedData result = FileParser.parseFile(tempFile.toString());

        assertTrue(result.rules().isEmpty());
        assertTrue(result.updates().isEmpty());

        Files.deleteIfExists(tempFile);
    }

    @Test
    void testParseFile_NoUpdatesSection() throws IOException {
        String content = "1|2\n3|4\n";
        Path tempFile = Files.createTempFile("test", ".txt");
        Files.write(tempFile, content.getBytes());

        FileParser.ParsedData result = FileParser.parseFile(tempFile.toString());

        assertEquals(2, result.rules().size());
        assertTrue(result.updates().isEmpty());

        Files.deleteIfExists(tempFile);
    }

    @Test
    void testParseFile_NoRulesSection() throws IOException {
        String content = "\n5,6,7\n8,9,10\n";
        Path tempFile = Files.createTempFile("test", ".txt");
        Files.write(tempFile, content.getBytes());

        FileParser.ParsedData result = FileParser.parseFile(tempFile.toString());

        assertTrue(result.rules().isEmpty());
        assertEquals(2, result.updates().size());
        assertArrayEquals(new int[]{5, 6, 7}, result.updates().get(0));
        assertArrayEquals(new int[]{8, 9, 10}, result.updates().get(1));

        Files.deleteIfExists(tempFile);
    }
}
