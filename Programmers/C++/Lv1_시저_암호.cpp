#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    
    for (int i=0; i<s.size(); i++) {
        if (s[i] != ' ') {
            if (s[i] >= 'A' && s[i] <= 'Z')
                answer += (s[i] - 'A' + n) % 26 + 'A';
            else
                answer += (s[i] - 'a' + n) % 26 + 'a';
        }
        else
            answer += ' ';
    }    
    return answer;
}