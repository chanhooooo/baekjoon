#include <stdio.h>
#include <stdlib.h>

void swap(int *pa, int *pb);

int main(void)
{
    // 1 ~ N까지 바구니에 
    // 1 ~ N번호가 적힌 공이 들어 있다!!
    int N;
    scanf("%d", &N);
    int *array = (int *)malloc(N * sizeof(int));
    if (array == NULL) exit(1);
    // N개 만큼 동적 할당!!
    // 동적 할당한 곳에 1 ~ N까지 대입

    // index i번 바구니에 i + 1을 넣자
    for (int i = 0; i < N; i++) array[i] = i + 1;

    int M;
    scanf("%d", &M);
    for (int a = 0; a < M; a++)
    {
        // 공 바꾸기
        int i, j;
        scanf("%d %d", &i, &j);
        swap(&(array[i - 1]), &(array[j - 1]));
    }

    for (int i = 0; i < N; i++) printf("%d ", array[i]);
    printf("\n");


    free(array);
    return 0;
}
void swap(int *pa, int *pb)
{
    int temp;
    temp = *pa;
    *pa = *pb;
    *pb = temp;
}