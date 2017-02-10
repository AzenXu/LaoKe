#include <stdio.h>

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0
#define MAXSIZE 20 /* 存储空间初始分配量 */

typedef int Status; 
typedef int SElemType; /* SElemType类型根据实际情况而定，这里假设为int */

typedef struct {
	SElemType data;
	struct StackNode *next;
} StackNode, *LinkStackPtr;

typedef struct {
	LinkStackPtr top;
	int count;
} LinkStack;

Status Push(LinkStack *S, SElemType e)
{
	//	将数据生成一个结点
	LinkStackPtr s = (LinkStackPtr) malloc (sizeof(StackNode));
	s->data = e;
	s->next = S->top;
	S->top = s;
	count++;
	return OK;
}

Status Pop(LinkStack *S, SElemType *e)
{
	LinkStackPtr p;
	if(StackEmpty(*S)) return ERROR;
	*e = S->top->data;
	p = S->top;
	S->top = S->top->next;
	free(p);
	S->count--;
	return OK;
}

 main(void)
{
	printf("OK\n");
	return 0;
}
