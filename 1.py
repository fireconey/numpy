#np中数组是数组，矩阵式矩阵，器运行方法不一样。

#由于numpy是用于处理矩阵的pandas是用于处理表格的
#所以numpy所有的数据必须是同类型的。pandas不需要。
import numpy as np
a=np.arange(5)
a.dtype#由于使用的是32Python所以是32

two=np.array([np.arange(100),np.arange(100)])
two
two.shape
two[0,0]
#复数不能转化为有实数，否则出错。

two.dtype
two.dtype.itemsize
