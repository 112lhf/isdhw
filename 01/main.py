Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(9,0,-1):
	for j in range(i,0,-1):
	      print(i,"*",j,"=",i*j," ",'\t',end=' ')
	print(end='\n')

	
9 * 9 = 81   	 9 * 8 = 72   	 9 * 7 = 63   	 9 * 6 = 54   	 9 * 5 = 45   	 9 * 4 = 36   	 9 * 3 = 27   	 9 * 2 = 18   	 9 * 1 = 9   	 
8 * 8 = 64   	 8 * 7 = 56   	 8 * 6 = 48   	 8 * 5 = 40   	 8 * 4 = 32   	 8 * 3 = 24   	 8 * 2 = 16   	 8 * 1 = 8   	 
7 * 7 = 49   	 7 * 6 = 42   	 7 * 5 = 35   	 7 * 4 = 28   	 7 * 3 = 21   	 7 * 2 = 14   	 7 * 1 = 7   	 
6 * 6 = 36   	 6 * 5 = 30   	 6 * 4 = 24   	 6 * 3 = 18   	 6 * 2 = 12   	 6 * 1 = 6   	 
5 * 5 = 25   	 5 * 4 = 20   	 5 * 3 = 15   	 5 * 2 = 10   	 5 * 1 = 5   	 
4 * 4 = 16   	 4 * 3 = 12   	 4 * 2 = 8   	 4 * 1 = 4   	 
3 * 3 = 9   	 3 * 2 = 6   	 3 * 1 = 3   	 
2 * 2 = 4   	 2 * 1 = 2   	 
1 * 1 = 1   	 
>>> 
