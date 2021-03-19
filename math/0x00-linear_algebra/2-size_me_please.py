#!/usr/bin/env python3
def matrix_shape(matrix):
	# shape = []
	# for l in matrix :
		# if type(l) is list :
			# shape.append(len(l))
		# else : 
			# shape.append(len(matrix[0]))
			# shape.append(len(l[0]))
		
	# return shape
    if type(matrix[0]) is list:
        return [len(matrix)] + matrix_shape(matrix[0])
    else:
        return [len(matrix)] 

