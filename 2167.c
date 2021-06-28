#include <stdio.h>
int main(){
    int sum;                                // 합을 저장할 변수
    short n, m, k, i, j, x, y;              // 사용자에게 입력받을 변수들
    short p=0, q=0, r=0;                    // 반복문 count에 사용할 변수들
    short arr[300][300];
    short (*pa)[300] = arr;
    scanf("%hd %hd", &n, &m);
    while(p<n){
        q = 0;
        while(q<m){
            scanf("%hd", *(pa+p)+q);
            q++;
        }
        p++;
    }
    scanf("%hd", &k);
    while(r<k){
        sum = 0;
        scanf("%hd %hd %hd %hd", &i, &j, &x, &y);
        short itmp = i;
        while(itmp<=x){
            short jtmp = j;
            while(jtmp<=y){
                sum += *(*(pa+itmp-1)+jtmp-1);
                jtmp++;
            }
            itmp++;
        }
        printf("%d\n", sum);
        r++;
    }

    return 0;
}
