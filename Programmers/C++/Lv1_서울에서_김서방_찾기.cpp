#include <string>
#include <vector>

using namespace std;

string solution(vector<string> seoul) {
    string answer = "";
    string num = "";
    
    for (int i=0; i<seoul.size(); i++) {
        if (seoul[i] == "Kim")
            num = to_string(i);
    }
    
    answer = "김서방은 " + num + "에 있다";
    return answer;
}