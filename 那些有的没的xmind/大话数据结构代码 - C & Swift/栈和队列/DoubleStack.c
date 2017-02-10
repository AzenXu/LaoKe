#include <stdio.h>

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0
#define MAXSIZE 20 /* 存储空间初始分配量 */

typedef int Status; 

typedef int StackElementType; /* SElemType类型根据实际情况而定，这里假设为int */

typedef struct {
	StackElementType data[MAXSIZE];
	int topGround;
	int topSky;
} StackDouble;

Status visit(SElemType c)
{
	printf("%d ",c);
	return OK;
}

/*  构造一个空栈S */
Status InitStack(StackDouble *S)
{ 
	S->top1=-1;
	S->top2=MAXSIZE;
	return OK;
}

/* 把S置为空栈 */
Status ClearStack(StackDouble *S)
{ 
	S->top1=-1;
	S->top2=MAXSIZE;
	return OK;
}

/* 若栈S为空栈，则返回TRUE，否则返回FALSE */
Status StackEmpty(StackDouble S)
{ 
	if (S.top1==-1 && S.top2==MAXSIZE)
		return TRUE;
	else
		return FALSE;
}

/* 返回S的元素个数，即栈的长度 */
int StackLength(StackDouble S)
{ 
	return (S.top1+1)+(MAXSIZE-S.top2);
}

Status Push(StackDouble *Stack, Int StackNum, StackElementType element)
{
	if(Stack->topGround + 1 >= Stack->topSky) return ERROR;
	if(StackNum == 0)
	{
		Stack->data[++Stack->topGround] = element;
		return OK;
	}
	else if(StackNum == 1)
	{
		Stack->data[--Stack->topSky] = element;
		return OK:
	}
	else 
	{
		return ERROR;
	}
}

int main(void)
{
	StackDouble
	printf("OK\n");
	return 0;
}
