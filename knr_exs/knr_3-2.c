/* K&R Exercise 3-2
 * Convert newlines and tabs into visible escapes (using a switch), and also
 * the inverse */

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
