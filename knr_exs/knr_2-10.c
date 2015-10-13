/* K&R Exercise 2-10
 * Convert upper-case to lower-case (using conditional exp) */

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
