#include <string>
#include <iostream>
#include <vector>

using namespace std;

int solution(int n, int k) {
    const int yang = 12000;
    const int drink = 2000;

    int answer = 0;
    answer = n * yang + k * drink - (n / 10) * drink;
    
    return answer;
}