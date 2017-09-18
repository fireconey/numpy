#数组切片(切片是在一个维度上的切，二维数组在每个维度上切)
import numpy as np
a=np.arange(10)
a
a[3:7]
#指定步长
a[:7:2]

#数据从后开始
a[::-1]

#reshape
three=np.arange(24).reshape(2,4,3)
three

#如果你不不关心具体哪个维度使用：替代
three[0,1,1]
three[0,:,:]
#多个冒号可以使用...替代
three[0,...]

#步长在切片后直接加：所以你看到，中间没有逗号的两个的冒号
three[0,1,::2]
