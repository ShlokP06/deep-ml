import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if new_shape[0]*new_shape[1] != len(a)*len(a[0]):
		return []
	m, n = new_shape
	col = len(a[0])
	res = [[0] * n for _ in range(m)]
	for i in range(m):
		for j in range(n):
			idx = i*n+j
			res[i][j] = a[idx//col][idx%col]
	return res