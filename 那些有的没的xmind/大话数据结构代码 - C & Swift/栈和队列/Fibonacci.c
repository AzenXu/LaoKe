#include <stdio.h>

void FiboFirst(void)
{
	int a[40];
	a[0] = 0;
	a[1] = 1;
	for(int i = 2;i < 40;i++)
	{
		a[i] = a[i - 1] + a[i - 2];
		printf("i = %d , element = %d\n",i, a[i]);
	}
}

int Fibo(int index)
{
	if (index < 0) return 0;
	if (index == 0) return 0;
	else if (index == 1) return 1;
	else
	{
		int result = Fibo(index - 1) + Fibo(index - 2);
		printf("index = %d, result = %d", index, result);
		return result;
	}
}

void FiboScend(void)
{
	Fibo(3);	
}

int main(void)
{
	FiboFirst();
	FiboScend();
	printf("OK\n");
	return 0;
}
