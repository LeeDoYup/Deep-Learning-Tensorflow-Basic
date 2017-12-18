import numpy as np


#Suffle data for Dataset (before dividing train, validation, test data set)
#Input type is numpy
def shuffle_data(x_train,y_train):
    temp_index = np.arange(len(x_train))

    #Random suffle index
    np.random.shuffle(temp_index)
    
    #Re-arrange x and y data with random shuffle index
    x_temp = np.zeros(x_train.shape)
    y_temp = np.zeros(y_train.shape)
    x_temp = x_train[temp_index]
    y_temp = y_train[temp_index]        

    return x_temp, y_temp

def read_numpy(X_numpy_data, Y_numpy_data=None):
	if Y_numpy_data == None:
		x_data = np.load(X_numpy_data)
		return x_data
	else:
		x_data = np.load(X_numpy_data)
		y_data = np.load(Y_numpy_data)
		return x_data, y_data

def binary_2_onehot(binary_data):
	file_len = len(binary_data)
	temp = np.zeros([file_len,2])
	for i in range(file_len):
		if binary_data[i] == 0:
			temp[i,0] = 1
		else:
			temp[i,1] = 1
	return temp

