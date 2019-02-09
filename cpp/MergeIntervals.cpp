/*

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

*/


#include <iostream>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;


struct Interval {
	int start;
	int end;
	Interval() : start(0), end(0) {}
	Interval(int s, int e) : start(s), end(e) {}
	
};


vector<Interval> merge(vector<Interval>& intervals) {
	if (intervals.empty()) return vector<Interval> {};
	vector<Interval> res;
	sort(intervals.begin(), intervals.end(), [](Interval a, Interval b) { return a.start < b.start; });
	res.push_back(intervals[0]);
	for (int i = 1; i < intervals.size(); i++) {
		if (res.back().end < intervals[i].start) {
			res.push_back(intervals[i]);
		}
		else {
			res.back().end = max(res.back().end, intervals[i].end);
		}
	}

	return res;
}


vector<Interval> online_merge(vector<Interval>& ins) {
	if (ins.empty()) return vector<Interval>{};
	vector<Interval> res;
	sort(ins.begin(), ins.end(), [](Interval a, Interval b) {return a.start < b.start; });
	res.push_back(ins[0]);
	for (int i = 1; i < ins.size(); i++) {
		if (res.back().end < ins[i].start) res.push_back(ins[i]);
		else
			res.back().end = max(res.back().end, ins[i].end);
	}
	return res;
}

int main() {

	Interval A(1, 3);
	Interval B(2, 6);
	Interval C(8, 10);
	Interval D(15, 18);
	vector<Interval> input_intervals;
	input_intervals.push_back(A);
	input_intervals.push_back(C);
	input_intervals.push_back(B);
	input_intervals.push_back(D);
	cout << input_intervals.size() << endl;
	for (auto interval : input_intervals) {
		cout << "[" << interval.start << "," << interval.end << "] ";
	}
	cout << endl;

	vector<Interval> output_intervals = merge(input_intervals);
	cout << output_intervals.size() << endl;
	for (auto interval : output_intervals) {
		cout << "[" << interval.start << "," << interval.end << "] ";
	}
	cout << endl;
	system("pause");

}
