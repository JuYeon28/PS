#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int k;

bool compare(string a, string b) {
    if (a[k] != b[k]) {
//        cout << a << b << endl;
        return a[k] < b[k];
    }
    else
        return a < b;
}

vector<string> solution(vector<string> strings, int n) {
    k = n;
    sort(strings.begin(), strings.end(), compare);
    return strings;
}