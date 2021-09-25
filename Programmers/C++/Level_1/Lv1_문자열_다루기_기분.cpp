#include <string>
#include <vector>

using namespace std;

bool solution(string s) {
    bool answer = true;
    
    if (s.size() != 4 and s.size() != 6)
        answer = false;
    else {
        for (int i=0; i<s.size(); i++) {
            if (!isdigit(s[i])) {
                answer = false;
                break;
            }
        }
    }
    return answer;
}