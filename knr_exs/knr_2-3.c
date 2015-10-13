/* K&R Exercise 2-3
 * Convert hexadecimal string to integer */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// (The decimal conversion of a hex string of length 8 starting with 'a' would
//  be too big to store in an int.)
static const int MAX_HEX_LEN = 7;
static const int MAX_INPUT_LEN = 1000;

int htoi(char *);
int hdtoid(char);

int main() {
    char c, hex[MAX_INPUT_LEN];
    int i = 0;

    while ((c = getc(stdin)) != '\n')
        hex[i++] = c;
        
    //char hex[] = "1A2b3C";
    printf("%d\n", htoi(hex));
    return 0;
}

// Converts a string of hexadecimal digits to its equivalent integer value.
// (The program terminates if the hex string is too long, i.e. the decimal
//  conversion is too big to store in an int.)
int htoi(char *s) {
    int i;
    int start = 0;
    int dec = 0;

    int len = strlen(s);
    if (len > MAX_HEX_LEN) {
        printf("Hexadecimal string is too long; terminating\n");
        exit(1);
    }

    // check for optional '0x' or '0X'
    if (s[0] == '0' && (s[1] == 'x' || s[1] == 'X'))
        start = 2;
    
    for (i = start; i < len; i++) {
        // show the calculations
        printf("%d * 16^%d = %d\n", hdtoid(s[i]), len - 1 - i + start, hdtoid(s[i]) * (int) pow(16, len - 1 - i + start));
        dec += hdtoid(s[i]) * (int) pow(16, len - 1 - i + start);
    }

    return dec;
}

// Converts a hexadecimal digit c to the corresponding integer digit.
// (Program terminates if c doesn't lie within 1-9, A-F or a-f.)
int hdtoid(char c) {
    if (c >= '0' && c <= '9')
        return c - 48;
    if (c >= 'A' && c <= 'F')
        return c - 55;
    if (c >= 'a' && c <= 'f')
        return c - 87;
    printf("Invalid character specified (%c); terminating\n", c);
    exit(1);
}





