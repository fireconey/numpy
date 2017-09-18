#矩阵变成 Python中的数据类型
import numpy as np
a=np.arange(24).reshape(6,4)
a


#已经变成了list但由于是二维矩阵所以变成了二维list
a.tolist()


#转变成指定的数据类型
a.astype(float)
