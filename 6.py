#数据的分割
import numpy as np
a=np.arange(27).reshape(3,3,3)
a

#水平分割(不是到切割的方向，而是走的方向)
np.hsplit(a,3)

#深度分割(矩阵必须是3维度以上)
np.dsplit(a,3)
a
