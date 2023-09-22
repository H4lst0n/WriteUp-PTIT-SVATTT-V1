#include <bits/stdc++.h>
using namespace std;

void sw(char *a1, char *a2) {
    char temp = *a1;
    *a1 = *a2;
    *a2 = temp;
}

void ran(char *a1, unsigned int a2) {
    char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    srand(a2);
    strcpy(a1, alphabet);
    for (int i = 25; i > 0; i--) {
        int j = rand() % (i + 1);
        sw(&a1[i], &a1[j]);
    }
}

void decrypt(char *a2, char *a1, char *a3) {
    for (int i = 0; i < strlen(a2); i++) {
        char chr = a2[i];
        if (chr >= 'A' && chr <= 'Z') {
            for (int j = 0; j < 26; j++) {
                if (a3[j] == chr) {
                    a1[i] = 'A' + j;
                    break;
                }
            }
        } 
		else if (chr >= 'a' && chr <= 'z') {
            for (int j = 0; j < 26; j++) {
                if (a3[j] + 'a' - 'A' == chr) {
                    a1[i] = 'a' + j;
                    break;
                }
            }
        } 
		else if (chr >= '0' && chr <= '9') {
            a1[i] = chr - 4;
        } 
		else {
            a1[i] = chr;
        }
    }
    a1[strlen(a2)] = '\0';
}
char flag[37] = "FVHVEVB{9dqIv5vdv54y_e5Fa7x_i4_r8wC}";
int main() {
    char v0[27] = "";
    char v1[37] = "GJEJZJN{n8l7_nr8A_f7fb_jdK_8aCeq!!!}"; 
    char v2[37] = "";
    int i = 0;
    while (true) {
        srand(time(0) + i);
        unsigned int v5 = rand();
        ran(v0, v5 << 5);
        decrypt(flag, v2, v0);
        if (strncmp(v2, "PTITCTF{", 8) == 0) {
            cout << v2 << endl;
            break;
        }
        cout << v2 << endl;
        i++;
    }
    return 0;
}
