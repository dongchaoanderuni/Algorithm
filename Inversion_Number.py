#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def Inversion(X):
	pass


def Small_Sum_Direct(X):
	Sum = 0
	for t, x in enumerate(X):
		if t > 0 and t < len(X)  :
			for n in X[:t]:
				if n < X[t]:
					print('X[%d] =%d,n= %d,Sun = %d' %(t,X[t],n,Sum))
					Sum += n
	return Sum


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

def Comparator_List(T):
	while T > 0:
		X = np.ndarray.tolist(np.random.randint(10, size=10))
		X_Select, X_Baseline = Inversion(X), Insertion_Sort(X)
		if X_Select != X_Baseline:
			print('When T = %d.it break down.Not the right method, try again.', T)
			break
		T -= 1
	print('Good Work!')



def main():

	X = [1,3,4,2,5]
	print(Small_Sum_Direct(X))

if __name__ == '__main__':
	main()
