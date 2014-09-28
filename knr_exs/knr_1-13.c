/* K&R Exercise 1-13
 * Write a program to print a histogram of the lengths of words in its input.
 * It is easy to draw the histogram with the bars horizontal; a vertical
 * orientation is more challenging. */

#include <stdio.h>

int main() {
    int c;
    int i;
    int j;
    int counts[10];

    // Initialize the counts to zero
    for (i = 0; i < 10; i++)
        counts[i] = 0;

    i = 0;
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            counts[i]++;
            i = 0;
        }
        else
            i++;
    }

    // Print the histogram
    for (i = 0; i < 10; i++) {
        printf("%d: ", i);
        for (j = 0; j < counts[i]; j++)
            printf("|");
        printf("\n");
    }

    return 0;
}
