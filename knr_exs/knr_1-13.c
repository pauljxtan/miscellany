/* K&R Exercise 1-13
 * Print histogram of word lengths in stdin
 * (Did the easier horizontal version) */

/* TODO: 
 *     Vertical version */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// Largest word length in histogram bins
const int HISTO_BIN_CUTOFF = 10;
// Maximum word length
const int MAX_WORD_LEN = 1024;

// Returns the number of digits in an integer (w/out leading zeros)
int get_n_digits(int);

int main() {
    int c;
    int i, j;
    int counts[MAX_WORD_LEN + 1];
    int spacing = 0;

    // Initialize the counts to zero
    for (i = 0; i <= MAX_WORD_LEN; i++)
        counts[i] = 0;

    i = 0;
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            // Ignore words longer than maximum
            if (i <= MAX_WORD_LEN)
                counts[i]++;
            i = 0;
        }
        else
            i++;
    }

    // Set spacing depending on histogram bin cutoff
    spacing += get_n_digits(HISTO_BIN_CUTOFF);

    // Print the histogram
    for (i = 1; i < HISTO_BIN_CUTOFF; i++) {
        printf("%d:", i);
        for (j = 0; j < spacing - get_n_digits(i); j++)
            printf(" ");
        for (j = 0; j < counts[i]; j++)
            printf("|");
        printf("\n");
    }
    
    // All lengths > cutoff are put in the same bin
    printf("%d:", HISTO_BIN_CUTOFF);
    for (i = HISTO_BIN_CUTOFF; i <= MAX_WORD_LEN; i++) {
        for (j = 0; j < counts[i]; j++)
            printf("|");
    }
    printf("\n");

    return 0;
}

int get_n_digits(int x) {
    if (x == 0)
        return 0;
    // Include minus sign if negative
    return floor(log10(abs(x))) + 1 + (x < 0);
}
