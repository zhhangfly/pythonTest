import numpy as np
import pandas as pd

#两者有不同的一位数组表示方式，numpy.array以及pandas的series


def test():
    #numpy的一维数组
    exampleNumpyOne = np.array([0,1,2,3,4])
    #进行一个随机访问
    print("np第一个元素:",exampleNumpyOne[0])
    #numpy二维数组
    exampleNumpyTwo = np.array([[1,2,3,4],[5,6,7,8]])
    #获取第一行
    print("np第一行：",exampleNumpyTwo[0,:])

    #pandas的一维数组
    examplePandasOne = pd.Series([1,2,3,4],index=['a','b','c','d'])
    #pandas一维数组第一个元素的访问
    print("pd第一个元素:",examplePandasOne.loc['a'])
    print("pd第一个元素:",examplePandasOne.iloc[0])

    # pandas的二维数组（每一列的元素类型都可以不相同，适合导入excel）
    #创建字典
    pandasDict = {
        '第一项':['1.1','1.2','1.3'],
        '第二项':['2.1','2.2','2.3'],
        '第三项':['3.1','3.2','3.3']
    }
    examplePandasTwo = pd.DataFrame(pandasDict,index=['第一行','第二行','第三行'])
    print(examplePandasTwo.loc['第一行','第一项'])#注意此处由于上防语句修改了默认的index，所以若使用examplePandasTwo.loc[0,'第一项']将会出错
    #度第一列
    print(examplePandasTwo.loc[:, '第一项'])


    #关于从excel中读取数据的相关操作
    fileNameStr = ('D:\\test.xlsx')#注意此处的两个反斜杠，不然\t会导致地址错误
    xls = pd.ExcelFile(fileNameStr)
    examplePandas = xls.parse('Sheet1')

    #打印前五行
    print(examplePandas.head())

    #查看列的数据类型
    print(examplePandas.loc[:,'时间'].dtype)

    #判断行和列数
    print(examplePandas.shape)#shape而不是shape()


if __name__ == '__main__':
    test()