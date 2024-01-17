#include <iostream>

using namespace std;

int main()
{
    int numbers[5] = {5, 1, 2, 3, 4};
    for (int i = 0;   i < 5; i++){
        for (int j = i; j<5; j++){
            if(numbers[j] < numbers[i]){
                int temp = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = temp;
            }
        }
    }
    for (int i = 0; i < 5; i++){
        cout << numbers[i] << endl;
    }
        return 0;
}