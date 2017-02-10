/*
 ADT 栈(stack)
 Data
	同线性表。元素具有相同的类型，相邻元素具有前驱和后继关系
 Operation
	InitStack(*S):初始化操作，建立一个空栈S
	DestoryStack(*S):若栈存在，则销毁它
	ClearStack(*S):将栈清空
	StackEmpty(S):若为空栈，则返回true，否则返回false
	GetTop(S,*e):若栈存在且非空，用e返回S的栈顶元素
	Push(*S,e):若栈存在，插入新元素e到栈S中，并成为栈顶元素
	Pop(*S,*e):删除栈S中栈顶元素，并用e返回其值
	StackLength(S):返回栈S的元素个数
 endADT
 */
#include <stdio.h>

#define OK 1
#define ERROR 0
#define TRUE 1
#define MAX_SIZE 20
#define FALSE 0

typedef int Status;
//	栈元素定义
typedef int StackElementType;
typedef struct {
	StackElementType data[MAX_SIZE];
	int top;	// 指示栈顶位置
}Stack;

Status visit(StackElementType c);

Status InitStack(Stack *S)
{ 
	/* S.data=(SElemType *)malloc(MAXSIZE*sizeof(SElemType)); */
	S->top=-1;
	return OK;
}

/* 把S置为空栈 */
Status ClearStack(Stack *S)
{ 
	S->top=-1;
	return OK;
}

/* 若栈S为空栈，则返回TRUE，否则返回FALSE */
Status StackEmpty(Stack S)
{ 
	if (S.top==-1)
		return TRUE;
	else
		return FALSE;
}

/* 返回S的元素个数，即栈的长度 */
int StackLength(Stack S)
{ 
	return S.top+1;
}

/* 若栈不空，则用e返回S的栈顶元素，并返回OK；否则返回ERROR */
Status GetTop(Stack S,StackElementType *e)
{
	if (S.top==-1)
		return ERROR;
	else
		*e=S.data[S.top];
	return OK;
}

Status Push(Stack *s, StackElementType e)
{
	if(s->top + 1 >= MAX_SIZE) return ERROR;
	s->top += 1;
	s->data[s->top] = e;
	return OK;
}

Status Pop(Stack *s, StackElementType *e)
{
	if(s->top == -1) return ERROR;

	*e = s->data[s->top];
	s->top -= 1;
	return OK;
}

void pushTest(void)
{
	Stack stack;
	InitStack(&stack);
	printf("top = %d",stack.top);
	Push(&stack, 100);
	printf("top = %d, first element = %d\n",stack.top,stack.data[stack.top]);
	StackElementType element;
	Pop(&stack, &element);
	printf("top = %d, first element = %d\n",stack.top,stack.data[stack.top]);
	printf("pop element is %d\n", element);
}

int main(void) 
{
	printf("OK，continue please~\n");
	printf("max size is %d\n",MAX_SIZE);
	visit(88);
	pushTest();
	return 0;
}

/************* Operactions ************/

Status visit(StackElementType c)
{
	printf("%d ",c);
	return OK;
}

