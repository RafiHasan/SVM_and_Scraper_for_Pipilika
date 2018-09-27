# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:54:49 2018

@author: Rafi
"""

from sklearn import svm
from sklearn.datasets import load_svmlight_file
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix


#Loading function for loading svmlight_file and convert it to numpyarray for the model
def dataload(str):
    #load_svmlight_file function takes filename feature count and datatype and returns a csvmatrix and an array as x and y 
    data=load_svmlight_file(str,n_features=200,dtype=np.float64)
    #converting csvmatrix into normal 2d array
    x=data[0].toarray()
    y=data[1]
    x=np.array(x)
    y=np.array(y)
    return x,y


#Loading the train and test data
trainx,trainy=dataload("svm_train_input_file.txt")
testx,testy=dataload("svm_test_input_file.txt")

#Parameter for the svm 
C=1.4 #error penalty
Karnel='rbf' #carnel used
Gamma=.0008 #convergence rate .  
Decision='ovo' #one vs one model is used rather then one vs rest or ovr


#Below code is used to find the optimal parameters for the model
"""
accu=0
for i in range(1,10):
    for j in range(1,10):
        for k in range (3):
            for m in range (2):
                    if k==0:
                        karnel='rbf'
                    elif k==1:
                        karnel='linear'
                    elif k==2:
                        karnel='sigmoid'
                    if m==0:
                        decision='ovo'
                    else:
                        decision='ovr'
                    classifier=svm.SVC(C=.2*i,kernel=karnel,gamma=.0002*j,decision_function_shape=decision,verbose=True)
                    classifier.fit(trainx,trainy)
                    z=classifier.predict(testx)
                    Accuracy_Score = accuracy_score(z, testy)  
                    print(Accuracy_Score)
                    if Accuracy_Score > accu :
                        accu=Accuracy_Score
                        C=.2*i
                        Karnel=karnel
                        Gamma=.0002*j
                        Decision=decision
                        
                            
                            



print(C+" "+Karnel+" "+Gamma+" "+Decision)
"""

#Here svm.SVC is used which is a wrapper arround libsvm

classifier=svm.SVC(C=C,kernel=Karnel,gamma=Gamma,decision_function_shape=Decision,verbose=True)

classifier.fit(trainx,trainy)

predic=classifier.predict(testx)

Accuracy_Score = accuracy_score(predic, testy)

Confution_Matrix=confusion_matrix(testy,predic,[1,2,3,4,5,6,7])

print(Accuracy_Score)
print(Confution_Matrix)

