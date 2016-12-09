print('请输入汉诺塔圆盘个数')
n = int(input())
def move(n,a,b,c):
	if n==1 :
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)#将前n-1个盘子从a移动到b上
		move(1,a,b,c)#将最底下的最后一个盘子从a移动到c上
		move(n-1,b,a,c)#将b上的n-1个盘子移动到c上
move(n,'a','b','c')