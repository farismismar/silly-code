#include <stdio.h>
#define SIZE 5

void swap(a, b)
int *a, *b;
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

void print_array(a)
int a[];
{
  int i;
  for (i = 0; i < SIZE; i++)
    printf("%d%s", a[i], (i != SIZE - 1) ? ", " : "\n");
}

int main()
{
  int a[] = {1, 3, 2, 5, 4};
  int i, j;

  print_array(a);

  for (i = 0; i < SIZE; i++)
    for (j = 0; j < SIZE - 1; j++)
      if (a[i] > a[j])
        swap(&a[i], &a[j]);
  
  print_array(a);

  return(0);
}

