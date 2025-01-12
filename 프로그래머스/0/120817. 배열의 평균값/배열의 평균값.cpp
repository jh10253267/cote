#include <string>
#include <iostream>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    double answer = 0;
    int sum = 0;
    int length = numbers.size();
    for (int i = 0; i < length; i++) {
        sum += numbers[i];
    }
    
    answer = static_cast<double>(sum) / length;
    return answer;
}