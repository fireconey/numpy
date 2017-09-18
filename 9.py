#输出文件
import numpy as np
#eye 表示单位矩阵，对角线元素都为1，其余为0
a=np.eye(2)#2x2

a

#保持数据
np.savetxt("eye.txt",a)

#读取csv。delimiter表示使用什么分割的
#csv格式就是使用逗号分隔的，但是可以使用excel打开而已
#usecols表示使用那列的数据，unpack表示分开
#储存数据不是把数据到放在一个地方。分别放在c，b中
c,b=np.loadtxt("ok.csv",delimiter=",",usecols=(6,7),unpack=True)
b


#加权平均averge ,算术平均是mean（）
v=np.average(c,weights=b)
v
