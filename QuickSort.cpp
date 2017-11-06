/*

Sort a given array with Quick Sort algorithm.

arr[] = { 12, 14, 15, 32, 31, 30, 45, 4, 5, 3, 6, 7, 8, 10 }

Expected output: 3 4 5 6 7 8 10 12 14 15 30 31 32 45

*/


/* C implementation QuickSort */
#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

// A utility function to swap two elements
void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

/* This function takes last element as pivot, places
the pivot element at its correct position in sorted
array, and places all smaller (smaller than pivot)
to left of pivot and all greater elements to right
of pivot */
int partition(int arr[], int low, int high)
{
	int pivot = arr[high];    // pivot
	int i = (low - 1);  // Index of smaller element

	for (int j = low; j <= high - 1; j++)
	{
		// If current element is smaller than or
		// equal to pivot
		if (arr[j] <= pivot)
		{
			i++;    // increment index of smaller element
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i + 1], &arr[high]);
	return (i + 1);
}

/* The main function that implements QuickSort
arr[] --> Array to be sorted,
low  --> Starting index,
high  --> Ending index */
void quickSort(int arr[], int low, int high)
{
	if (low < high)
	{
		/* pi is partitioning index, arr[p] is now
		at right place */
		int pi = partition(arr, low, high);

		// Separately sort elements before
		// partition and after partition
		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}

/* Function to print an array */
void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		printf("%d ", arr[i]);
	cout << endl;
}

// Driver program to test above functions
int main()
{
	int arr[] = { 12, 14, 15, 32, 31, 30, 45, 4, 5, 3, 6, 7, 8, 10 };
	int sz = sizeof(arr) / sizeof(arr[0]);
	cout << "Size " << sz << endl;
	quickSort(arr, 0, sz - 1);
	printf("Sorted array: ");
	printArray(arr, sz);
	system("pause");
	return 0;
}
