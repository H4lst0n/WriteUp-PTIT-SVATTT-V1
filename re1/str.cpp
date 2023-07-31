#include <bits/stdc++.h>

using namespace std;

int main(){

  signed int v0; // [esp+0h] [ebp-2Ch]
  signed int i; // [esp+4h] [ebp-28h]
  char v2[28]; // [esp+8h] [ebp-24h]
  char Str[] = "LcKUC8JBInrfjVzdeb8qCHE8ozXSMt";
  v2[0] = 0;
  v2[1] = 13;
  v2[2] = 51;
  v2[3] = 28;
  v2[4] = 16;
  v2[5] = 98;
  v2[6] = 120;
  v2[7] = 13;
  v2[8] = 26;
  v2[9] = 29;
  v2[10] = 36;
  v2[11] = 36;
  v2[12] = 44;
  v2[13] = 34;
  v2[14] = 56;
  v2[15] = 28;
  v2[16] = 92;
  v2[17] = 17;
  v2[18] = 96;
  v2[19] = 62;
  v2[20] = 12;
  v2[21] = 2;
  v2[22] = 36;
  v2[23] = 77;
  v2[24] = 10;
  v2[25] = 11;
  v2[26] = 50;
  v2[27] = 28;
  v0 = strlen(Str);
  for ( i = 0; i < v0; ++i )
    Str[i] ^= v2[i];

  cout << Str;

    return 0;
}
 Halston    \Downloads\7FBB625F8793198942C61A50F3D0B49C  ﮫ 53ms   10:25 AM  
 ⚡ndinh ❯❯ cd "c:\Users\ndinh\Downloads\7FBB625F8793198942C61A50F3D0B49C\" ; if ($?) { g++ t.cpp -o t } ; if ($?) { .\t }
LnxISZ2OSsVBFtBx9sXOOJaueqjOMt