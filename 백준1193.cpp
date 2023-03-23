#include <iostream>

using namespace std;

int main(){
    int x, n = 1;

    cin >> x;

    while(x > n){
        x -= n;
        n++;
    }

    if(n%2==1) cout << n-(x-1) << '/' << x;
    else cout << x << '/' << n-(x-1);

    return 0;
}