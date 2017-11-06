/*

Given a random array, the specified number of sorted elements should be returned.

For example, if array is {1,7,6,5,4,3,2}
When input 5, only first five elements should be sorted and returned, which is {1,2,3,4,5}

Hint: Merge sort (nlogn)

*/


#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void merge(int low, int mid, int high, int a[])
{
	int h = low, i = low, j = mid + 1, b[50], k;
	// Two pointers: h & j
	// Array b is to store values temporarily
	while ((h <= mid) && (j <= high)){
		if (a[h] <= a[j]){
			b[i] = a[h];
			h++;
		}else{
			b[i] = a[j];
			j++;
		}
		i++;
	} // Two pointers are located on both sides (stage 1)
	if (h > mid){
		for (k = j; k <= high; k++){
			b[i] = a[k];
			i++;
		}
	}else{
		for (k = h; k <= mid; k++){
			b[i] = a[k];
			i++;
		}
	} // When stage 1 over, pointer h is on each side and assign values
	for (k = low; k <= high; k++) a[k] = b[k];
	// Assign values in b array to a array
}

void merge_sort(int low, int high, int a[])
{
	int mid;
	if (low < high) {
		mid = (low + high) / 2;
		merge_sort(low, mid, a);
		merge_sort(mid + 1, high, a);
		merge(low, mid, high, a);
	} // Recusively merge_sort array on two sides and merge them together
}

int main() {
	int ar[50] = { 2,42,2,1,5,9,8,7,12,32,45,20,11,21,100,13,14,50,56,3,23,44,91,19 };
	cout << "Enter the target: ";
	int tagt;	cin >> tagt;
	merge_sort(0, tagt, ar);
	cout << "Sorted array: ";
	for (int i = 0; i <= tagt; i++) {
		cout << ar[i] << " ";
	}
	cout << endl;
	system("pause");
}
