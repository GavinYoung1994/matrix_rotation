def rotate(matrix, n):
	for i in range(0,(n+1)/2):
		for k in range(0,n/2):
			temp = matrix[i][k]
			matrix[i][k] = matrix[n-1-k][i]
			matrix[n-1-k][i] = matrix[n-1-i][n-1-k]
			matrix[n-1-i][n-1-k] = matrix[k][n-1-i]
			matrix[k][n-1-i] = temp
	print(matrix)

matrix_3 = [[1,2,3],[4,5,6],[7,8,9]]
matrix_4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotate(matrix_3,3)
rotate(matrix_4,4)