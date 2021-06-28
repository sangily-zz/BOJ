#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    int i = 0;
    while(i < n){
        int j = 0, k = 0;
        while(j < n-i-1){ printf(" "); j++; }
        while(k < i+1) { printf("*"); k++; }
        printf("\n");
        i++;
    }
    return 0;
}
