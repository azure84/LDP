import glmnet_python
from glmnet import glmnet
from sklearn import linear_model
import numpy as np
x = np.zeros((3,2))
y = np.zeros((3))
x = x.tolist()
y = y.tolist()

a = [[0.0,0.0],[0.0,0.0],[0.0,0.0]]
b = [0.0,0.0,0.0]
fit = glmnet(x=a.copy(),b=b.copy())

