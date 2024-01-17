#include <iostream>
using namespace std;

int binary_search(int numbers_array[], int min, int max, int number){
    while (min <= max)
    {
        int mid = (min+max) / 2;
        if(numbers_array[mid] == number){
            return mid;
        }else if(numbers_array[mid] < number){
            min = mid + 1;
        }else if(numbers_array[mid] > number){
            max = mid - 1;
        }
    }
    return -1;
}


int main()
{
    int numbers[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int numbers_size = sizeof(numbers) / sizeof(numbers[0]);
    cout << binary_search(numbers, 0, numbers_size - 1, 100) << endl;
    return 0;
}