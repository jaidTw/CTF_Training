#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <signal.h>
#include <unistd.h>

#define MAX 100000000

void handler(int signo) {
    printf("\ntime's up!\n");
    exit(0);
}

int main(void) {
    signal(SIGALRM, handler);
    alarm(30);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    srand(time(NULL));
    int num = rand() % MAX;
    int guess = 0;
    while(num != guess) {
        printf("guess a number (0 ~ %d) > ", MAX);
        scanf("%d", &guess);
        if(num > guess)
            printf("bigger!!\n");
        else if(num < guess)
            printf("smaller!!\n");
    }
    printf("correct!\n");
    printf("FLAG{PwNT0015_15_C00L}");
    return 0;
}

