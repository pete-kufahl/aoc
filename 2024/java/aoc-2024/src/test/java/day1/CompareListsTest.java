package day1;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class CompareListsTest {

    @Test
    void testDifferenceOfLists_SameLists() {
        List<Integer> list1 = Arrays.asList(1, 2, 3);
        List<Integer> list2 = Arrays.asList(1, 2, 3);
        assertEquals(0, CompareLists.differenceOfLists(list1, list2));
    }

    @Test
    void testDifferenceOfLists_DifferentLists() {
        List<Integer> list1 = Arrays.asList(1, 3, 5);
        List<Integer> list2 = Arrays.asList(2, 4, 6);
        assertEquals(3, CompareLists.differenceOfLists(list1, list2));
    }

    @Test
    void testDifferenceOfLists_EmptyLists() {
        List<Integer> list1 = Collections.emptyList();
        List<Integer> list2 = Collections.emptyList();
        assertEquals(0, CompareLists.differenceOfLists(list1, list2));
    }

    @Test
    void testSimilarityOfLists_SameLists() {
        List<Integer> list1 = Arrays.asList(1, 2, 3);
        List<Integer> list2 = Arrays.asList(1, 2, 3);
        assertEquals(1 + 2 + 3, CompareLists.similarityOfLists(list1, list2));
    }

    @Test
    void testSimilarityOfLists_PartialOverlap() {
        List<Integer> list1 = Arrays.asList(1, 2, 3, 4);
        List<Integer> list2 = Arrays.asList(2, 3, 5, 6);
        assertEquals((2) + (3), CompareLists.similarityOfLists(list1, list2));
    }

    @Test
    void testSimilarityOfLists_NoOverlap() {
        List<Integer> list1 = Arrays.asList(1, 2, 3);
        List<Integer> list2 = Arrays.asList(4, 5, 6);
        assertEquals(0, CompareLists.similarityOfLists(list1, list2));
    }

    @Test
    void testSimilarityOfLists_EmptyLists() {
        List<Integer> list1 = Collections.emptyList();
        List<Integer> list2 = Collections.emptyList();
        assertEquals(0, CompareLists.similarityOfLists(list1, list2));
    }
}