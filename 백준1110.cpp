#include <iostream>

using namespace std;

int main(){
    int n, ans, cnt = 0;

    cin >> n;
    ans = n;

    while(true){
        n = ((n%10)+(n/10))%10 + (n%10)*10;
        cnt++;
        if(n==ans) break;
    }

    cout << cnt;
}
