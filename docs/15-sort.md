# Sort algorithms

## Bubble Sort

## Insertion Sort

## Quick Sort

QuickSort is a fast sorting algorithm, which is used not only for educational purposes, but widely applied in practice. On the average, it has ```O(nlogn)``` complexity, making quicksort suitable for sorting big data volumes. The idea of the algorithm is quite simple. The divide-and-conquer strategy is used in quicksort. Below the recursion step is described.
1. Choosing a pivot value. We take the value of the middle element as the pivot value, but it can be any value, which is in range of sorted values.
2. Partition. Rearrange elements in such a way that all elements which less than the pivot go to the left part of the array and all elements greater than the pivot go to the right part of the array. Values equal to the pivot can stay in any part of the array and note that the array may be divided in non-equal parts.
3. Sort both parts. Apply quicksort algorithm recursively to the left and the right parts.


[reference](http://www.algolist.net/Algorithms/Sorting/Quicksort)