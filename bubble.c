#include <stdio.h>

void swap(a, b)
int *a, *b;
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

void print_array(a, size)
int a[];
int size;
{
  int i;
  for (i = 0; i < size - 1; i++)
    printf("%d,", a[i]);
  printf("%d\n", a[size - 1]);
}

void bubble_sort(array, size)
int array[];
int size;
{
  int i, j;

  for (i = 0; i < size; i++)
    for (j = 0; j < size - 1; j++)
      if (array[j] > array[j + 1])
        swap(&array[j], &array[j + 1]);
}
  
int main()
{
  int a[] = {1, 3, 10, 2, 5, 4, 2};
  int size = sizeof(a) / sizeof(a[0]);
  
  print_array(a, size);
  bubble_sort(a, size);
  print_array(a, size);

  return(0);
}

