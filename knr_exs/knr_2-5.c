/* K&R Exercise 2-5
 * Return location of first character in a string matching a character in
 * another string */

#include <stdio.h>

int any(char [], char []);

int main() {
    char str1[] = "abcdefg";
    char str2[] = "hijeklm";

    int idx = any(str1, str2);
    printf("%d\n", idx);

    return 1;
}

int any(char s1[], char s2[]) {
    int i, j;

    // iterate over s1
    for (i = 0; s1[i] != '\0'; i++) {
        // iterate over s2
        for (j = 0; s2[j] != '\0'; j++) {
            if (s1[i] == s2[j])
                return i;
        }
    }
    // no matches found
    return -1;
}
