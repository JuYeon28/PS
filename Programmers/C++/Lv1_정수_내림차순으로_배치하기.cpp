#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    string strn = to_string(n);
    sort(strn.begin(), strn.end(), greater<char>());
    answer = stoll(strn);
    return answer;
}