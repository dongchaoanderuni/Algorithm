#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

import sys

sys.setrecursionlimit(1000000)

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
递归函数

Return the max value of the function
'''
def RecurMax_Fun(X):
	L = 0
	R = len(X)  - 1

	def GetMax(X,L,R):
		if L == R:
			return X[L]

		Mid = (L + R)//2
		L_Max = GetMax(X, L, Mid)
		R_Max = GetMax(X, Mid + 1, R)
		return max(L_Max, R_Max)
	return GetMax(X, L, R)

'''
归并排序
'''
def Recursive_Sort(X):
	# T = []
	# def MaxRecurs(X,L,R):
	# 	if len(X):
	# 		return X[L]
	#
	# 	Mid = (L + R)//2
	# 	L_Max = MaxRecurs(X, L, Mid)
	# 	R_Max = MaxRecurs(X, Mid + 1, R)
	# 	X[X.index(L_Max)], X[X.index(R_Max)] = X[X.index(max(L_Max,R_Max))], X[X.index(max(R_Max,L_Max))]
	# 	return Merge(T, L, Mid, R)
	#
	#
	# if len(X) / 2 != 0:
	# 	X = X[:-1]
	# 	TL = X[-1]
	# 	L = 0
	# 	R = len(X) - 1
	# 	Mid = (L + R) //2
	# 	return Merge(MaxRecurs(X, L, R).append(TL),L,Mid,R)
	# else:
	# 	L = 0
	# 	R = len(X) - 1
	# 	return MaxRecurs(X, L, R)
	if len(X) <= 1:
		return X
	Mid = len(X)//2
	L = Recursive_Sort(X[:Mid])
	R = Recursive_Sort(X[Mid:])
	return Merge(L,R)


def Merge(L, R):
	# T = []
	# Thres = Mid
	# point = Mid + 1
	# n = L
	# print('X= ', X)
	# print('L,Mid,R =%d,%d,%d'%(L,Mid,R))
	# while n <= Thres and point <= R:
	# 	print('n = %d, point = %d' %(n, point))
	# 	if X[n] < X[point]:
	# 		T.append(X[n])
	# 		n += 1
	# 		if n > Thres:
	# 			T = T + X[point:]
	# 	else:
	# 		T.append(X[point])
	# 		point += 1
	# 		if point > len(X):
	# 			# print('Mid', X)
	# 			T = T + X[n:]
	# return T
	T = []
	i, j = 0, 0
	while i <len(L) and j <len(R):
		if L[i] <= R[j]:
			T.append(L[i])
			i += 1
		else:
			T.append(R[j])
			j += 1

	'''
	Marvelous
	'''
	T += L[i:]
	T += R[j:]
	return T

'''
比较函数
'''
def Comparator_List(T):
	while T > 0:
		X = np.ndarray.tolist(np.random.randint(10, size=10))
		X_Select, X_Baseline = Recursive_Sort(X),Insertion_Sort(X)
		if X_Select != X_Baseline:
			print('When T = %d.it break down.Not the right method, try again.',T)
			break
		T -= 1
	print('Good Work!')

def main():
	T = 5000
	Comparator_List(T)
	# X = [0,4,2,5,1]
	# # Mid = (L + R)//2
	# print(Recursive_Sort(X))


if __name__ == '__main__':
	main()
