package day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static day1.CompareLists.differenceOfLists;
import static day1.CompareLists.similarityOfLists;

public class Day1 {
    public static void main(String[] args) {
        String fileName = "src/main/resources/day1/input.txt";
        int i = 0;
        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                i += 1;
                String[] parts = line.trim().split("\\s+"); // handle multiple spaces
                if (parts.length == 2) {
                    int[] nums = Arrays.stream(parts)
                            .mapToInt(Integer::parseInt)
                            .toArray();
                    arr1.add(nums[0]);
                    arr2.add(nums[1]);
                }
            }
            long ans1 = differenceOfLists(arr1, arr2);
            System.out.println("Difference of lists: " + ans1);

            long ans2 = similarityOfLists(arr1, arr2);
            System.out.println("Similarity of lists: " + ans2);

        } catch (RuntimeException e) {
            System.out.println("Error found in line: " + i + " -> " + e.getMessage());
        } catch (IOException e) {
            System.out.println("Problem reading file: " + fileName + "-> " + e.getMessage());
        }
    }
}
