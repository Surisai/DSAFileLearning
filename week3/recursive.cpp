#include <iostream>
#include <vector>

class X {
    unsigned int rc = 1;    // 1 operation (assignment)
        if(n > 1) {             // 1 operation (comparison)
        rc = n * factorial(n - 1); // 3 operations:
                                //   - multiplication
                                //   - subtraction
                                //   - assignment
                                // PLUS all operations from factorial(n-1)
    }
    return rc;              // 1 operation


};
/*Recursive analysis 
3 operation. for unsigned int rc =1; , if(n> 1), return rc ; 
 T(0) == 3  even all F so 
 T(1) == 3 
 
 
 so 
 T(n) is O(n)
 T(n)     = 6 + T(n-1)
         = 6 + (6 + T(n-2))
         = 6 + (6 + (6 + T(n-3)))
         ...
         = 6(n - 1) + T(1)
         = 6(n - 1) + 3
         = 6n - 3


*/


int main(){
    return 0 ;
}