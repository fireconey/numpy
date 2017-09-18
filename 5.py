#数组的组合
import numpy as np
a=np.arange(9).reshape(3,3)
a
b=a*2
b
#水平组合
np.hstack((a,b))

#使用concatenate是一样的
np.concatenate((a,b),axis=0)

#垂直组合
np.vstack((a,b))


#深度组合,每个数组的对应位置组合为一组。
np.dstack((a,b))


#行组合和列组合都是同行或同列的为一组
np.row_stack((a,b))
a
