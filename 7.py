#矩阵的属性
import numpy as np
a=np.arange(24).reshape(4,6)
a

#维度
a.ndim
#元素的个数
a.size
#元素所在字节
a.itemsize

#虚数
k=np.array([1.j+1])
k

#找虚数位的实数部分
k.real
#找虚数部分
k.imag
