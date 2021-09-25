#include <string>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

// bool is_prime(int num) {
//     for (int i=2; i<=sqrt(num); i++) {
//         if (num%i == 0)
//             return false;
//     }
//     return true;
// }

int solution(int n) {
    int answer = 0;
    vector<int> arr(n+1);
    
    for (int i=2; i<arr.size(); i++)
        arr[i] = i;
   
    for (int i=2; i<=n; i++) {
        for (int j=2*i; j<=n; j+=i)
            arr[j] = 0;
    }
    
    for (int i=2; i<=n; i++) {
        if (arr[i] != 0)
            answer++;
    }
    return answer;
}