//linear

#include <iostream>
#include <vector>
#include <string>


using namespace std;
// int add(int n){
//     int s = 0 ;
//     for(int i ; i<= n; i ++){///if  i = i + 2;  1 +n/2 ; T (n) = 
//                             //  i = i+1 ; 1+(1+n)
//          s += i;
//     }
//     return -1 ;
// }

///linear analysis funetion cure
template <class TYPE>
int linearSearch(const vector<TYPE>& arr, const TYPE& key){
    int rc=-1;
    for(int i=0;i<arr.size()&& rc==-1;i++){
        if(arr[i]==key){
            rc=i;
        }
    }
    return rc;
}

int main(){

    
//       vector<int> numbers = {4, 7, 1, 3, 9,10,22,11};

// int index = linearSearch(numbers, 11);  // should return 3
//     cout << "Index of 11: " << index << endl;

//     index = linearSearch(numbers, 10);  // should return -1
//     cout << "Index of 10: " << index << endl;

cout << endl;
cout << " Test with String type data"<< endl;
    vector<string> fruits = {"apple", "banana", "cherry", "date"};

    int index = linearSearch(fruits, string("cherry"));  // should return 2
    cout << "Index of 'cherry': " << index << endl;

    index = linearSearch(fruits, string("kiwi"));  // should return -1
    cout << "Index of 'kiwi': " << index << endl;


    return 0;