#数据展开
import numpy as np
b=np.arange(20)
b.reshape(4,5)

b.ravel()
b.flatten()

#可以给数组的形状赋值来改变维度
b.shape=(4,5)
b
#矩阵转置
b.T
b.transpose()
b
#reshape是返回一个修改后的数组，原来的不修改
#resize()是把原来的数组修改后进行的返回。
b.reshape(2,10)
b

b.resize(2,10)
b
