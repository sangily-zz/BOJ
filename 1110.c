#include <stdio.h>
int main(){
    int a;
    int cycle = 0;
    scanf("%d", &a);
    int b = a;
    do{
        b = (b%10)*10 + ((b/10)+(b%10))%10;
        cycle++;
    }while(b!=a);
    printf("%d\n", cycle);
    return 0;
}
