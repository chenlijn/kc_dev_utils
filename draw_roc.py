
'''draw ROC curve and compute the Area under curve'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

y = np.array([1,1,2,2])
scores = np.array([0.1, 0.4, 0.35, 0.8])

# compute the roc curve
fpr, tpr, thresholds = roc_curve(y, scores, pos_label=2) 

#compute area under curve
area = auc(fpr, tpr)

# print fpr
# print tpr
# print thresholds

plt.figure()
plt.plot(fpr, tpr, color='blue',
                  label='ROC curve (area = %0.2f)' % area)
plt.plot([0, 1], [0, 1], color='navy',  linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic curve')
plt.legend(loc="lower right")
plt.savefig("roc.png")
#plt.show()

