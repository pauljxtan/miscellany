/* A C implementation of the count-change procedure in SICP Section 1.2.2 */

#include <stdio.h>

int count_change(int);
int cc(int, int);
int first_denomination(int);

int main(int argc, char *argv[]) {
    printf("%d\n", count_change(100));
}

int count_change(int amount) {
    return cc(amount, 5);
}

int cc(int amount, int kinds_of_coins) {
    if (amount == 0)
        return 1;
    if (amount < 0 || kinds_of_coins == 0)
        return 0;
    return cc(amount, kinds_of_coins - 1) + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins);
}

int first_denomination(int kinds_of_coins) {
    if (kinds_of_coins == 1) return 1;  // penny
    if (kinds_of_coins == 2) return 5;  // nickel
    if (kinds_of_coins == 3) return 10; // dime
    if (kinds_of_coins == 4) return 25; // quarter
    if (kinds_of_coins == 5) return 50; // "half-dollar" (haven't seen one of these in ages here in Canada)
}
