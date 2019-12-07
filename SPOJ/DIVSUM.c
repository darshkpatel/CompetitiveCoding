#include <stdio.h>
int main(){
    long int cases=0;
    scanf("%ld",&cases);
    for(long int i=0;i<cases;i++){
        long int num=0;
        long int sum=0;
        scanf("%ld",&num);
        for(long int x=1;x<num;x++){
            if(num%x==0){
                sum+=x;
            }
        }
        printf("%ld",sum);
    }
    return 0;
}