/* K&R Exercise 3-1
 * Our binary search makes two tests inside the loop, when one would suffice (at the price of
 * more tests outside.) Write a version with only one test inside the loop and measure the
 * difference in run-time. */

#include <stdio.h>

int binsearch1(int, int [], int);
int binsearch2(int, int [], int);

int main() {
    int w[] = {0, 1, 3, 6, 10, 15, 21, 28, 36};
    int m = sizeof(w) / sizeof(int);

    int i1, i2;
    int j1, j2;
    int k1, k2;

    i1 = binsearch1(3, w, m);
    printf("%d\n", i1);
    i2 = binsearch2(3, w, m);
    printf("%d\n", i2);
    
    j1 = binsearch1(21, w, m);
    printf("%d\n", j1);
    j2 = binsearch2(21, w, m);
    printf("%d\n", j2);

    k1 = binsearch1(5, w, m);
    printf("%d\n", k1);
    k2 = binsearch2(5, w, m);
    printf("%d\n", k2);

    return 0;
}

int binsearch1(int x, int v[], int n) {
    int low, high, mid;

    low = 0;
    high = n - 1;
    while (low <= high) {
        mid = (low + high) / 2;
        printf("%d %d %d\n", low, high, mid);
        if (x < v[mid])
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else
            return mid;
    }
    return -1;
}

int binsearch2(int x, int v[], int n) {
    int low, high, mid;
    
    low = 0;
    high = n - 1;
    while (low < high - 1) {
        mid = (low + high) / 2;
        printf("%d %d %d\n", low, high, mid);
        if (x < v[mid])
            high = mid - 1;
        else 
            low = mid;
    }
    /*
    if (x == v[low])
        return low;
    else
        return -1;
    */
    return x == v[low] ? low : -1;
}

