from __future__ import print_function
import time
import numpy as np
import Registration
from utils.utils import *
import cv2
import matplotlib.pyplot as plt

#datadir = '/media/yzhq/TOSHIBA/data/Registration/UAVs/'
datadir = '../../data/UAVs/'
matoutdir = datadir + 'matout/'
name1 = '4a'
name2 = '4b'
ext = '.jpg'
IX_path = datadir + name1 + ext
IY_path = datadir + name2 + ext

IX = cv2.imread(IX_path)
IY = cv2.imread(IY_path)
IY = cv2.resize(IY, (IX.shape[1], IX.shape[0]))

fex = Registration.CNN_feature()
stime = time.time()
X, Y = fex.extract(IX, IY)
print(time.time()-stime)
print(X.shape[0])

colors = np.random.rand(X.shape[0])

ks = 3
blurX = cv2.GaussianBlur(IX,(ks,ks),0)
blurY = cv2.GaussianBlur(IY,(ks,ks),0)

plt.imshow(cv2.cvtColor(blurX, cv2.COLOR_BGR2RGB))
plt.scatter(X[:, 1], X[:, 0], s=50, marker='o', c=colors, alpha=0.8)
plt.show()
plt.imshow(cv2.cvtColor(blurY, cv2.COLOR_BGR2RGB))
plt.scatter(Y[:, 1], Y[:, 0], s=50, marker='o', c=colors, alpha=0.8)
plt.show()

# outfile = name1 + '_' + name2 + '.mat'
# sio.savemat(matoutdir+outfile, {'X':X, 'Y':Y})
# print('saved to ' + outfile)