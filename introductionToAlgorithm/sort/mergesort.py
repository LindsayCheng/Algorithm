#encoding:utf-8

"""

"""


def mergesort(numlist):
    """
    归并排序.分而治之.
    1 如果待排序列表个数为1,则直接返回.
    2 将待排序列表分解为两个子列表
    3 将排序好的两列表合并.
    时间复杂度:nlgn
    树高度为:分解的次数lgn. 树宽度为合并时间复杂度n
    :param numlist:
    :retur n:
    """
    if numlist is None or len(numlist)==0:
        return None

    length=len(numlist)
    if length == 1:
        return numlist
    midindex=length/2
    alist=mergesort(numlist[:midindex])
    blist=mergesort(numlist[midindex:])
    return merge(alist,blist)


def merge(alist,blist):
    """
    归并排序中的合并算法.
    分别从底部取值比较,并存入结果列表
    :param alist: 已排好序的列表1
    :param blist: 已排好序的列表2
    :return:
    """
    sortedlist=[]
    alength=len(alist)
    blength=len(blist)
    aindex,bindex=0,0
    for i in xrange(alength+blength):
        if aindex==alength:
            sortedlist.extend(blist[bindex:])
            break

        if bindex==blength:
            sortedlist.extend(alist[aindex:])
            break

        if alist[aindex]<=blist[bindex]:
            sortedlist.append(alist[aindex])
            aindex+=1
        else:
            sortedlist.append(blist[bindex])
            bindex+=1

    return sortedlist


if __name__ == "__main__":
    numlist=[23,1,32,4,23,56,22,25,7,45,8]
    sortedlist=mergesort(numlist)
    print numlist
    print sortedlist



