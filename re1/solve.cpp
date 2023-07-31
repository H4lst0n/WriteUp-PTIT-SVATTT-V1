#include <bits/stdc++.h>

using namespace std;

int check(int a1, int a2){
    int v4 = a1 % a2;
    for (int i = 1; i < a2; ++i )
    {
        if ( i * v4 % a2 == 1 )
        return i;
    }

    return -1;
}

int main(){
    char s[] = "LnxISZ2OSsVBFtBx9sXOOJaueqjOMt";
    int a2 = 5;
    char flag[100];
    int a3 = 8;
    int cnt = strlen(s) + 1;
    int x = 26;
    int v3 = check(a2, x);
    for( int i = 0; i < cnt; i++){
        int v7 = s[i];
        if ( v7 < 65 || v7 > 90 )
        {
        if ( v7 >= 97 && v7 <= 122 )
            v7 = v3 * ((v7 - 97 - a3 + 26) % 26) % 26 + 97;
        }
        else
        {
        v7 = v3 * ((v7 - 65 - a3 + 26) % 26) % 26 + 65;
        }
        flag[i] = v7;
    }
    cout << flag;
    return 0;
}