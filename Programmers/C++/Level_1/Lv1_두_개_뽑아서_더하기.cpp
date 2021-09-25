#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    vector<int> tmp;
    
    for (int i=0; i<numbers.size(); i++) {
        for (int j=i+1; j<numbers.size(); j++) {
            tmp.push_back(numbers[i]+numbers[j]);
        }
    }
    sort(tmp.begin(), tmp.end());
    answer.push_back(tmp[0]);
    
    for (int i=1; i<tmp.size(); i++) {
        if (tmp[i-1] != tmp[i])
            answer.push_back(tmp[i]);
    }
    return answer;
}