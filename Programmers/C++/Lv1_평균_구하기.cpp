#include <string>
#include <vector>

using namespace std;

double solution(vector<int> arr) {
    double answer = 0;
    for(int i; i < arr.size(); i++) {
        answer += arr[i];
    }
    return answer/arr.size();
}