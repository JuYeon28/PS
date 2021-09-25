#include <string>
#include <vector>

using namespace std;

int test1[5] = {1, 2, 3, 4, 5};
int test2[8] = {2, 1, 2, 3, 2, 4, 2, 5};
int test3[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

int max(int a, int b) {
    return a < b ? b : a;
}

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> score(3);
    int maxscore = 0;
    
    for (int i=0; i<answers.size(); i++) {
        if (test1[i%5] == answers[i])
            score[0]++;
        if (test2[i%8] == answers[i])
            score[1]++;
        if (test3[i%10] == answers[i])
            score[2]++;
    }
    
    maxscore = max(max(score[0], score[1]), score[2]);
    
    for (int i=0; i<3; i++) {
        if (score[i] == maxscore)
            answer.push_back(i+1);
    }
    return answer;
}