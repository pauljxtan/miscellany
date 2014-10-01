/* K&R Exercise 2-10
 * Rewrite the function lower, which converts upper case letters to lower
 * case, with a conditional expression instead of if-else. */

#include <stdio.h>

int lower(int);

int main() {
    int c = 'J';
    int d = lower(c);
    int e = 'X';
    int f = lower(e);

    printf("%c --> %c\n", c, d);
    printf("%c --> %c\n", e, f);

    return 0;
}

int lower(int c)
{
    return (c >= 'A' && c <= 'Z') ? c + 'a' - 'A' : c;
}
