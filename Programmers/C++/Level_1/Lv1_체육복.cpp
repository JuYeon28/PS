#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> students(n, 1);
    
    for (int i=0; i<reserve.size(); i++)
        students[reserve[i]-1]++;
    for (int i=0; i<lost.size(); i++)
        students[lost[i]-1]--;
    
    for (int i=0; i<n; i++) {
        if (i > 0 && students[i] == 0 && students[i-1] == 2) {
            students[i-1]--;
            students[i]++;
        }
        if (i < n-1 && students[i] == 0 && students[i+1] == 2) {
            students[i+1]--;
            students[i]++;
        }
    }
    for (int s : students) {
        if (s > 0)
            answer++;
    }
    return answer;
}