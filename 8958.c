#include <stdio.h>
int main(){
    int times;
    char answer[80];
    int score = 0, count = 0, continuous = 0, ref = 0;
    scanf("%d\n", &times);
    while(count != times){
        scanf("%s", &answer);
        while(answer[ref]!='\0'){
            if(answer[ref]=='O') continuous++;
            else continuous = 0;
            score += continuous;
            ref++;
            if(ref==81) break;
        }
        printf("%d\n", score);
        continuous = score = ref = 0; 
        count++;
    }
    return 0;
}
