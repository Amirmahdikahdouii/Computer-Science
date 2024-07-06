#include <iostream>
using namespace std;

int insertionSort(int numbers[])
{
    for (int i = 1; i < 6; i++)
    {
        int key = numbers[i];
        int j = i - 1;
        while (j >= 0 and numbers[j] > key)
        {
            numbers[j+1] = numbers[j];
            j--;
        }
        numbers[j+1] = key;
    }
    for (int i = 0; i < 6; i++)
    {
        cout << numbers[i] << endl;
    }
    return 0;
}

int main()
{
    int l[6] = {5, 4, 2, 3, 1, 6};
    insertionSort(l);
    return 0;
}