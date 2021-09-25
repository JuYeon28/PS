#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for (int n=0; n<commands.size(); n++) {
        int i = commands[n][0];
        int j = commands[n][1];
        int k = commands[n][2];
        
        vector<int> tmp;
        for (int m=i-1; m<j; m++)
            tmp.push_back(array[m]);
        sort(tmp.begin(), tmp.end());
        answer.push_back(tmp[k-1]);
    }
    return answer;
}