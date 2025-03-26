package day9;
import java.io.*;
import java.util.*;

public class DiskBuilder {

    public static class FileInfo {
        int fileId;
        int fileSize;

        public FileInfo(int fileId, int fileSize) {
            this.fileId = fileId;
            this.fileSize = fileSize;
        }

        @Override
        public String toString() {
            return "(" + fileId + ", " + fileSize + ")";
        }
    }

    public static class DiskData {
        Map<Integer, FileInfo> diskMap;
        Map<Integer, Integer> gapMap;
        int lastIndex;

        public DiskData(Map<Integer, FileInfo> diskMap, Map<Integer, Integer> gapMap, int lastIndex) {
            this.diskMap = diskMap;
            this.gapMap = gapMap;
            this.lastIndex = lastIndex;
        }
    }

    public static DiskData buildFilesAndGaps(String filepath) {
        Map<Integer, FileInfo> diskMap = new HashMap<>();
        Map<Integer, Integer> gapMap = new HashMap<>();

        int inputIdx = -1;
        int mapIdx = 0;
        int fileID = 0;
        int filesize, space;

        try (BufferedReader reader = new BufferedReader(new FileReader(filepath))) {
            int charRead;
            while ((charRead = reader.read()) != -1) {
                char c = (char) charRead;
                if (c == '\n') break;

                inputIdx++;
                int value = Character.getNumericValue(c); // Convert char to int

                if (inputIdx % 2 == 1) {
                    space = value;
                    gapMap.put(mapIdx, space);
                    mapIdx += space;
                } else {
                    filesize = value;
                    diskMap.put(mapIdx, new FileInfo(fileID, filesize));
                    fileID++;
                    mapIdx += filesize;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return new DiskData(diskMap, gapMap, mapIdx);
    }

    public static long computeChecksumOfCompacted(String filepath, boolean debug) {
        DiskData data = buildFilesAndGaps(filepath);
        Map<Integer, FileInfo> diskMap = data.diskMap;
        Map<Integer, Integer> gapMap = data.gapMap;
        int mapIdx = data.lastIndex;

        if (debug) {
            System.out.println("Map index at start of compression = " + mapIdx);
            printDisk(diskMap, mapIdx);
        }

        List<Integer> uncompressed = new ArrayList<>(diskMap.keySet());
        Collections.sort(uncompressed);

        long checksum = 0;
        int cidx = 0;
        int end = mapIdx;

        while (cidx < end) {
            if (diskMap.containsKey(cidx)) {
                FileInfo file = diskMap.get(cidx);
                for (int i = 0; i < file.fileSize; i++) {
                    if (debug)
                        System.out.println("File content at " + cidx + ", fid = " + file.fileId + ", size = " + file.fileSize + ", end index: " + end);
                    checksum += (long) cidx * file.fileId;
                    cidx++;
                }
            } else if (gapMap.containsKey(cidx)) {
                int lastFileIdx = uncompressed.get(uncompressed.size() - 1);
                int firstGapIdx = cidx;
                FileInfo file = diskMap.get(lastFileIdx);
                int gapSize = gapMap.get(firstGapIdx);

                while (gapSize > 0 && file.fileSize > 0) {
                    if (debug)
                        System.out.println("Gap at " + cidx + " (size=" + gapSize + "), moving file " + file.fileId + " from " + lastFileIdx + " (size=" + file.fileSize + "), end index: " + end + " -> " + (end - 1));
                    gapSize--;
                    file.fileSize--;
                    checksum += (long) cidx * file.fileId;
                    end--;
                    cidx++;
                }

                if (gapSize > 0) {
                    gapMap.remove(firstGapIdx);
                    gapMap.put(cidx, gapSize);
                    if (debug) System.out.println("New GAP of " + gapSize + " starting at " + cidx);
                    diskMap.remove(uncompressed.remove(uncompressed.size() - 1));
                } else if (file.fileSize > 0) {
                    gapMap.remove(firstGapIdx);
                    diskMap.put(lastFileIdx, new FileInfo(file.fileId, file.fileSize));
                    if (debug) System.out.println("Leftover FILE id=" + file.fileId + ", size=" + file.fileSize);
                } else {
                    if (debug) System.out.println("File perfectly filled gap at " + (cidx - 1));
                    gapMap.remove(firstGapIdx);
                    diskMap.remove(uncompressed.remove(uncompressed.size() - 1));
                }
            } else {
                System.out.println("Index " + cidx + " not registered in diskMap or gapMap, I don't know what to do!");
                cidx++;
            }

            if (debug) printDisk(diskMap, end);

            if (!uncompressed.isEmpty()) {
                FileInfo lastFile = diskMap.get(uncompressed.get(uncompressed.size() - 1));
                while ((end - 1) > (uncompressed.get(uncompressed.size() - 1) + lastFile.fileSize - 1)) {
                    if (debug) System.out.println("Leftover gap at end! Adjusting ...");
                    end--;
                    if (debug) printDisk(diskMap, end);
                }
            }
        }
        return checksum;
    }

    public static long computeChecksumOfIntegrated(String filepath, boolean debug) {
        DiskData data = buildFilesAndGaps(filepath);
        Map<Integer, FileInfo> diskMap = data.diskMap;
        Map<Integer, Integer> gapMap = data.gapMap;
        int mapIdx = data.lastIndex;

        if (debug) {
            System.out.println("Map index at start of compression = " + mapIdx);
            printDisk(diskMap, mapIdx);
        }

        // Step 1: Sort files by location (also sorts by file ID)
        List<Integer> filesToMove = new ArrayList<>(diskMap.keySet());
        Collections.sort(filesToMove, Collections.reverseOrder()); // Process in decreasing file ID

        // Step 2: Sort gaps by location
        List<Integer> gapsToFill = new ArrayList<>(gapMap.keySet());
        Collections.sort(gapsToFill);

        // Step 3: Move whole files to the leftmost suitable gap
        Map<Integer, FileInfo> compressedMap = new HashMap<>();
        for (int loc : filesToMove) {
            boolean moved = false;
            FileInfo file = diskMap.get(loc);
            int fileSize = file.fileSize;
            int targetGap = -1;

            for (int gloc : gapsToFill) {
                if (gloc >= loc) break; // Only look left
                int gapSize = gapMap.get(gloc);

                if (gapSize >= fileSize) {
                    compressedMap.put(gloc, file);
                    moved = true;
                    targetGap = gloc;

                    // Update gaps
                    gapSize -= fileSize;
                    gapMap.remove(gloc);
                    if (gapSize > 0) {
                        gapMap.put(gloc + fileSize, gapSize);
                    }
                    break;
                }
            }

            if (moved) {
                gapsToFill = new ArrayList<>(gapMap.keySet()); // Refresh gaps list
                Collections.sort(gapsToFill);
            } else {
                compressedMap.put(loc, file); // Keep file in place
            }

            if (debug) {
                System.out.println("Checked file " + file.fileId + " (original location " + loc + "), placed in " + (moved ? targetGap : loc));
                printDisk(compressedMap, mapIdx);
            }
        }

        // Step 4: Compute checksum
        long checksum = 0;
        List<Integer> compressedFiles = new ArrayList<>(compressedMap.keySet());
        Collections.sort(compressedFiles);

        int cidx = 0;
        int end = compressedFiles.get(compressedFiles.size() - 1)
                + compressedMap.get(compressedFiles.get(compressedFiles.size() - 1)).fileSize;

        while (cidx < end) {
            if (compressedMap.containsKey(cidx)) {
                FileInfo file = compressedMap.get(cidx);
                for (int i = 0; i < file.fileSize; i++) {
                    checksum += (long) cidx * file.fileId;
                    cidx++;
                }
            } else {
                cidx++;
            }
        }
        return checksum;
    }

    private static void printDisk(Map<Integer, FileInfo> diskMap, int mapIdx) {
        System.out.println("Current Disk State:");
        for (int i = 0; i < mapIdx; i++) {
            if (diskMap.containsKey(i)) {
                FileInfo file = diskMap.get(i);
                System.out.println("Index " + i + " -> File ID: " + file.fileId + ", Size: " + file.fileSize);
            }
        }
        System.out.println("---------------------");
    }

    public static void main(String[] args) {
        String filepath = "src/main/resources/day9/example.txt";
        DiskData result = buildFilesAndGaps(filepath);

        System.out.println("Disk Map: " + result.diskMap);
        System.out.println("Gap Map: " + result.gapMap);
        System.out.println("Final Map Index: " + result.lastIndex);
    }
}
