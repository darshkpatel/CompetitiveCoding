#include<iostream>
using namespace::std;

long int factorial(int x){
    if(x<=1){return 1;}
    else{return x*factorial(x-1);}
}

int main(){
    int cases;
    cin >> cases;
    while(cases--){
        int n,k;
        cin >> n >> k;
        cout << "n=" << n << " k=" << k << endl;
        cout << factorial(k-1)/(factorial(n-1)*factorial(k-n-2)) << endl;
    }

    return 0;
}