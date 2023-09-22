#include <bits/stdc++.h>
using namespace std;

int main(){
    char a[9];
    char b[1] = {'}'};
    
    strncpy(a, "\x50\x54\x49\x54\x43"
                "T\x46{", 8);
    a[8] = '\0';
    
    char s[13] = "\x10\x27\x3a\x17\x2d\x10\x2b\x21\x3c\x79\x26\x2f";
    
    for (int i = 0; i < 12; i++) 
        s[i] = s[i] ^ 72; 
    s[12] = '}';
    cout << a << s;
    return 0;
}
