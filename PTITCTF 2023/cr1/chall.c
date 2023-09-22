#include <stdio.h>
#include <string.h>

int checkPassword(char *a)
{
    int b = strlen(a);
    if ((b ^ 21))
        return 0;
    ;
    if ((strncmp(a, "\x50\x54\x49\x54\x43"
                    "T\x46{",8) ^0))
        return 0;
    ;
    if (a[20] != '}')
        return 0;
    char c[128]; 
    strcpy(c, a + 8); 
    int i = 0;
    for (i = 0; i < 12; i++) {
        c[i] = c[i] ^ 72; 
    }

    if ((strncmp(c, "\x10\x27\x3a\x17\x2d\x10\x2b\x21\x3c\x79\x26\x2f", 12) ^ 1))
        return 1;
    else
        return 0;
}

int main()
{
    char password[128];
    printf("[+] Enter password (password is the flag): ");
    fgets(password, 128, stdin);
    int length = strlen(password);
    if (password[length - 1] == '\n') {
        password[length - 1] = '\0';
    }
    if (0 != checkPassword(password))
        printf("[+] Correct password: %s\n", password);
    else
        printf("[+] Incorrect password\n");
    return 0;
}


