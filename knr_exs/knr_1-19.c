/* K&R Exercise 1-19
 * Reverse lines from stdin */

#include <stdio.h>

static const int MAX_LINE_LEN = 100;

void reverse(char *, int);
int getline1(char *);

int main() {
    int i, line_len;
    char line[MAX_LINE_LEN];

    // read in each line
    while ((line_len = getline1(line)) > 0) {
        reverse(line, line_len);
        // line[0] is '\n' so skip it
        for (i = 1; i < line_len; i++)
            printf("%c", line[i]);
        printf("\n");
    }

    return 0;
}

// Reverses the character string s of length len.
void reverse(char *s, int len) {
    int i;
    char tmp;

    for (i = 0; i < len / 2; i++) {
        tmp = s[i];
        s[i] = s[len - 1 - i];
        s[len - 1 - i] = tmp;
    }
}

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
