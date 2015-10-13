/* K&R Exercise 1-8
 * Count blanks, tabs, newlines from stdin */

#include <stdio.h>

int main() {
    int c;
    int nb = 0;    /* blanks (presumably whitespace?) */
    int nt = 0;    /* tabs */
    int nl = 0;    /* newlines */

    while ((c = getchar()) != EOF) {
        if (c == ' ')
            ++nb;
        else if (c == '\t')
            ++nt;
        else if (c == '\n')
            ++nl;
    }
    printf("Blanks:   %d\n", nb);
    printf("Tabs:     %d\n", nt);
    printf("Newlines: %d\n", nl);

    return 0;
}
