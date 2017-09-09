# -*- coding:utf-8 -*-

import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from stepbystep import *
def load_data():
    train_dataset = h5py.File('./datasets/train_catvnoncat.h5', "a")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('./datasets/test_catvnoncat.h5', "a")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

def predict_if_cat(X, y, parameters):
    """
    This function is used to predict the results of a  L-layer neural network.
    
    Arguments:
    X -- data set of examples you would like to label
    parameters -- parameters of the trained model
    
    Returns:
    p -- predictions for the given dataset X
    """
    
    m = X.shape[1]
    n = len(parameters) // 2 # number of layers in the neural network
    p = np.zeros((1,m))
    
    # Forward propagation
    probas, caches = L_model_forward(X, parameters)

    
    # convert probas to 0/1 predictions
    for i in range(0, probas.shape[1]):
        if probas[0,i] > 0.5:
            p[0,i] = 1
        else:
            p[0,i] = 0

    accuracy = float((np.dot(y,p.T) + np.dot(1-y,1-p.T))/float(y.size)*100)
    print ("Accuracy: {} %".format(accuracy))
        
    return p

def print_mislabeled_images(classes, X, y, p):
    """
    Plots images where predictions and truth were different.
    X -- dataset
    y -- true labels
    p -- predictions
    """
    a = p + y
    mislabeled_indices = np.asarray(np.where(a == 1))
    plt.rcParams['figure.figsize'] = (40.0, 40.0) # set default size of plots
    num_images = len(mislabeled_indices[0])
    for i in range(num_images):
        index = mislabeled_indices[1][i]
        
        plt.subplot(2, num_images, i + 1)
        plt.imshow(X[:,index].reshape(64,64,3), interpolation='nearest')
        plt.axis('off')
        plt.title("Prediction: " + classes[int(p[0,index])].decode("utf-8") + " \n Class: " + classes[y[0,index]].decode("utf-8"))
    plt.show()

if __name__ == '__main__':

	train_x_orig, train_y, test_x_orig, test_y, classes = load_data()
	# index = 131
	# # print train_x_orig
	# plt.imshow(train_x_orig[index])
	# plt.show()
	# print ("y = " + str(train_y[0,index]) + ". It's a " + classes[train_y[0,index]].decode("utf-8") +  " picture.")

	m_train = train_x_orig.shape[0]
	num_px = train_x_orig.shape[1]
	m_test = test_x_orig.shape[0]

	train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0], -1).T   # The "-1" makes reshape flatten the remaining dimensions
	test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T

	# Standardize data to have feature values between 0 and 1.
	train_x = train_x_flatten/255.
	test_x = test_x_flatten/255.

	layers_dims = [12288, 60,20, 1] #  5-layer model
	parameters = L_layer_model(train_x, train_y, layers_dims, learning_rate = 0.5, num_iterations = 3000, print_cost = True,plot_cost=True)
	
	predictions_train = predict_if_cat(train_x, train_y, parameters)
	pred_test = predict_if_cat(test_x, test_y, parameters)
	print_mislabeled_images(classes, test_x, test_y, pred_test)