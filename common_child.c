#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
int mat[5001][5001] = {0};

// Complete the commonChild function below.
int max(int a, int b, int c) {
    int max;
    max = c;
    if (a > b) {
        if (a > c) {
            max = a;
        }
    } else if (b > c) {
        max = b;
    }
    return max;
}

int commonChild(char* s1, char* s2) {
    
    int len;
    int i,j;
    int found;
    len = strlen(s1);
    for (i=1; i< len+1; ++i) {
        for (j = 1; j < len+1; ++j) {
            found = (s1[i-1] == s2[j-1])?1:0;
            
            mat[i][j] = max(mat[i][j-1], mat[i-1][j-1]+found, mat[i-1][j]);
        }
    }

    return mat[len-1][len-1];
}

int main()
{
    FILE* fptr = fopen("out.txt", "w");

    char* s1 = readline();

    char* s2 = readline();

    int result = commonChild(s1, s2);
    printf("\n%d\n",result);
    fprintf(fptr, "%d\n", result);

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}
