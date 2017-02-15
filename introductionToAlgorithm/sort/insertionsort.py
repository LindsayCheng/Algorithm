#encoding:utf-8

import numpy as np

def insertionsort(numlist):
    """
    numlist大小为n.从j=1起构造已排好序和待排序列表.
    将待排序数值插入左边已排好序的列表,直到待排序列表为空.
    时间复杂度 n的2次方.
    :param numlist:
    :return:
    """
    if numlist is None or len(numlist)==0:
        return None
    length=len(numlist)
    sortedlist=np.array([np.NaN]*length).tolist()
    sortedlist[0]=numlist[0]

    for i in range(length-1):
        j=i+1
        num=numlist[j]
        for k in range(j)[::-1]:
            if sortedlist[k]>num:
                sortedlist[k+1]=sortedlist[k]
                sortedlist[k]=num
            else:
                sortedlist[k+1]=num
                break

    return sortedlist


if __name__ == "__main__":
    numlist=[23,1,32,4,23,56,22,25,7,45,8]
    sortedlist=insertionsort(numlist)
    print numlist
    print sortedlist




