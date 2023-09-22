#include <bits/stdc++.h>

using namespace std;
int main(){
    srand(time(0));
    for(int i = 0; i < 10; i++){
        int x = rand();
        cout << x << endl;
        cout << (x << 5) << endl;
    }
    return 0;
}