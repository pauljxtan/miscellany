/* K&R Exercise 3-2
 * Write a function escape(s,t) that converts characters like newline and tab into visible
 * escape sequences like \n and \t as it copies the string t to s. Use a switch. Write a
 * function for the other direction as well, converting escape sequences into the real
 * characters. */

#include <stdio.h>

void escape(char [], char []);

int main() {
    char w[] = "This\tis\ta\ntest\tstring\n";
    char x[50];

    escape(w, x);

    printf("Unescaped: %s\n", w);
    printf("Escaped: %s\n", x);

    return 0;
}

void escape(char s[], char t[]) {
    int i, j;

    j = 0;
    for (i = 0; s[i] != '\0'; i++) {
        switch (s[i]) {
            case '\n':
                t[j++] = '\\';
                t[j++] = 'n';
                break;
            case '\t':
                t[j++] = '\\';
                t[j++] = 't';
                break;
            default:
                t[j++] = s[i];
                break;
        }
    }
    t[j] = '\0';
}
