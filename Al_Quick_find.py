#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = 10
X = [x for x in range(N)]


'''
二元数组的Uni-find 算法, 时间复杂度为O^2
'''

# M = ((1,2),(2,7),(3,4),(4,8),(8,9),(0,5),(5,6))
#
# for m in M:
# 	for n, x in enumerate(X):
# 		if x == X[m[0]]:
# 			X[n] = X[m[-1]]
# 	print(X)



'''
对于不定项element的Uni-find算法, 时间复杂度为O^2
'''

# M = ((1,2,7),(0,5,6),(3,4,8,9))
#
# for m in M:
# 	for ele_m in m:
# 		for n, x in enumerate(X):
# 			if x == X[ele_m]:
# 				X[n] = X[m[-1]]
# 	print(X)

'''
Weighted quick-union analysis
'''

