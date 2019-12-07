#include <stdio.h>
int main(){
    int a=0;
    while (1==1){
        scanf("%d",&a);
        if(a!=42){
            printf("%d",a);
        }
        else{
            break;
        }
    }
}