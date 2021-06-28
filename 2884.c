#include <stdio.h>

int main(){
    int H, M;
    scanf("%d %d",&H,&M);
    if(M<45){
         printf("%d %d", (H+24-1)%24, M+15);
    }
    else printf("%d %d", H, M-45);
    return 0;
}
