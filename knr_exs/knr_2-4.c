/* K&R Exercise 2-4
 * Write an alternative version of squeece(s1,s2) that deletes each character
 * in s1 that matches any character in the string s2. */

#include <stdio.h>

void squeeze(char [], char []);

int main() {
    int i;
    char str1[] = "abcdefghijklmnopqrstuvwxyz";
    char str2[] = "bdfhjlnprtvxz";

    squeeze(str1, str2);

    printf("%s\n", str1);

    return 0;
}
// Deletes all each character in s1 that matches any character in s2.
void squeeze(char s1[], char s2[]) {
    int i, j, k;

    // iterate over chars in s2
    for (i = 0; s2[i] != '\0'; i++) {
        // iterate over chars in s1
        for (j = k = 0; s1[j] != '\0'; j++)
            if (s1[j] != s2[i])
                s1[k++] = s1[j];
        s1[k] = '\0';
    }
}
