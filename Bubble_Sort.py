#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

'''
冒泡排序
'''
def Bubble_Sort(X):
	for s in range(len(X)):
		n = 0
		while n < len(X) - 1:
			if X[n] > X[n + 1]:
				X[n], X[n + 1] = X[n + 1], X[n]
			else:
				n += 1

	return X

'''
选择排序
'''
def Selection_Sort(X):
	n = len(X)
	S = []
	while n > 0:
		x = min(X)
		X[X.index(x)], X[-1] = X[-1], X[X.index(x)]
		S.append(X[-1])
		X = X[:-1]
		n -= 1

	return S
'''
插入排序
'''
def Insertion_Sort(X):
	for n in range(len(X)):
		while n > 0:
			if X[n] < X[n-1]:
				X[n],X[n-1] = X[n-1],X[n]
			n -= 1
	return X


'''
比较函数
'''
def Comparator_List(T):
	while T > 0:
		X = np.ndarray.tolist(np.random.randint(10, size=10))
		X_Bubble, X_Select, X_Baseline = Bubble_Sort(X),Selection_Sort(X),Insertion_Sort(X)
		if X_Select != X_Baseline or X_Bubble != X_Baseline:
			print('When T = %d.it break down.Not the right method, try again.',T)
			break
		T -= 1
	print('Good Work!')

def main():
	T = 50
	Comparator_List(T)

if __name__ == '__main__':
	main()
