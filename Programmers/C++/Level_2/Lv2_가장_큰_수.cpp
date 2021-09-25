#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool bigger(string a, string b) {
    if (a+b > b+a)
        return true;
    return false;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> v;
    
    for (int i=0; i<numbers.size(); i++)
        v.push_back(to_string(numbers[i]));
    sort(v.begin(), v.end(), bigger);
    
    for (int i=0; i<v.size(); i++){
        answer = answer + v[i];
    }
    if (answer[0] == '0')
        answer = "0";
    return answer;
}