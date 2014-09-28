/* K&R Exercise 1-9
 * Write a program to copy its input to its output, replacing each string of
 * one or more blanks by a single blank. */

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


