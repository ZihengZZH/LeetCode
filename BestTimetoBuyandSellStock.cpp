/*

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

*/


#include <iostream>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>


using namespace std;

// 0.045s
int maxProfit_online(vector<int>& prices) {
	int maxPro = 0;
	int minPrice = INT_MAX;
	for (int i = 0; i < prices.size(); i++) {
		minPrice = min(minPrice, prices[i]);
		maxPro = max(maxPro, prices[i] - minPrice);
	}
	return maxPro;
}

// 1.00s
int maxProfit(vector<int>& prices) {
	int output = 0;
	for (int i = 0; i < prices.size(); ++i) {
		int j = prices.size() - 1;
		while (i < j) {
			if ((prices[j] - prices[i]) > output) {
				output = prices[j] - prices[i];
			}
			j--;
		}
	}
	return output;
}


static void random_vec(vector<int>& temp) {
	srand((unsigned)time(0));
	for (auto i = 0; i < 100; ++i) {
		temp.push_back ((rand() % 100) + 1);
	}
}


static void display_vec(vector<int>& temp) {
	for (auto t : temp) {
		cout << t << "\t";
	}
}


int main() {

	//vector<int> input{ 7,10,5,3,6,4,2,5,15 };
	vector<int> input;
	random_vec(input);

	int output1, output2;
	/*COMPARISON OF TWO APPOARCHES*/

	clock_t begin = clock();
	for (int index = 0; index < 500; index++) {
		output1 = maxProfit(input);
	}
	clock_t end = clock();
	double elapased_secs = double(end - begin) / CLOCKS_PER_SEC;
	cout << "RUNNING TIME " << elapased_secs << endl;

	begin = clock();
	for (int index = 0; index < 500; index++) {
		output2 = maxProfit_online(input);
	}
	end = clock();
	elapased_secs = double(end - begin) / CLOCKS_PER_SEC;
	cout << "RUNNING TIME " << elapased_secs << endl;
	
	display_vec(input);
	if (output1 == output2)
		cout << "OUTPUT " << output1 << endl;

	getchar();
	return 0;
	
}