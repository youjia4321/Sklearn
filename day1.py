import numpy as np
from sklearn import preprocessing  # 数据预处理
input_data = np.array([[2.1, -1.9, 5.5],
                      [-1.5, 2.4, 3.5],
                      [0.5, -7.9, 5.6],
                      [5.9, 2.3, -5.8]])

# 这是当需要将数值转换为布尔值时使用的预处理技术。我们可以用一种内置的方法来二值化输入数据，比如说用0.5作为阈值，方法如下 (所有高于0.5(阈值)的值将被转换为1，并且所有低于0.5的值将被转换为0。)

data_binarized = preprocessing.Binarizer(threshold = 0.5).transform(input_data)
print("\nBinarized data:\n", data_binarized)

# 平均值和标准偏差 - (axis=0为列)

print("Mean = ", input_data.mean(axis = 0))
print("Std deviation = ", input_data.std(axis = 0))

# 删除输入数据的平均值和标准偏差 -(scale 零均值单位方差)

data_scaled = preprocessing.scale(input_data)
print(data_scaled)
print("Mean =", data_scaled.mean(axis=0))
print("Std deviation =", data_scaled.std(axis = 0))