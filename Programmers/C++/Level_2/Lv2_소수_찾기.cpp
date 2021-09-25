#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

bool is_prime(int num) {
    if (num < 2)
        return false;
    for (int i=2; i<=sqrt(num); i++) {
        if (num%i == 0)
            return false;
    }
    return true;
}

int solution(string numbers) {
    int answer = 0;
    vector<int> v;
    
    for (int i=0; i<numbers.size(); i++) {
        v.push_back(numbers[i] - '0');
    }
    
    sort(v.begin(), v.end());
    vector<int> ans;
    
    do {
        for (int i=0; i<=v.size(); i++) {
            int tmp = 0;
            for (int j=0; j<i; j++) {
                tmp = (tmp * 10) + v[j];
                ans.push_back(tmp);
            }
        }
    } while (next_permutation(v.begin(), v.end()));
    
    sort(ans.begin(), ans.end());
    ans.erase(unique(ans.begin(), ans.end()), ans.end());
    
    for (int i=0; i<ans.size(); i++) {
        if (is_prime(ans[i]))
            answer++;
    }
    return answer;
}