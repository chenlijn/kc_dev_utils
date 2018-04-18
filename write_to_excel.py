
import numpy as np
from pandas import DataFrame


a = np.array([[1,2,3], [4,5,6]])

df = DataFrame(a)

rows = range(5)
df.to_excel('test.xls', sheet_name='confusion_matrix', index=rows, columns=rows)

