/* K&R Exercise 1-9
 * Copy stdin to stdout, shortening blanks */

#include <stdio.h>

int main() {
    int c;
    int prev_was_blank = 0;

    while ((c = getchar()) != EOF) {
        if (c == ' ')
            prev_was_blank = 1;
        else if (prev_was_blank) {
            putchar(' ');
            putchar(c);
            prev_was_blank = 0;
        }
    }

    return 0;
}


