#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int sum_ = 0;
    int x_ori = x;
        
    while (x > 0) {
        sum_ += x % 10;
        x /= 10;
    }
    
    if (x_ori % sum_ != 0)
        answer = false;
    
    return answer;
}