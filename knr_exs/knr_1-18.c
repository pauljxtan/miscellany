/* K&R Exercise 1-18
 * Remove trailing blanks/tabs from stdin */

#include <stdio.h>

static const int MAX_LINE_LEN = 1000;

// Reads a line into s and returns the length.
int getline1(char s[]) {
    int c, i;

    for (i = 0; i < MAX_LINE_LEN - 1 && (c = getchar()) != EOF && c != '\n';
         i++)
        s[i] = c;
    if (c == '\n')
        s[i++] = c;
    
    return i;
}

int main() {
    int i, j, strlen;
    char line[MAX_LINE_LEN]; // stores each line

    while ((strlen = getline1(line)) > 0) {
        i = strlen - 2;
        // i stops decrementing at beginning of trailing spaces/tabs
        while (line[i] == ' ' || line[i] == '\t')
            i--;

        // print line
        for (j = 0; j < i + 1; j++)
            putchar(line[j]);
        putchar('\n');
    }

    return 0;
}
