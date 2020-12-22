# -*- coding: utf-8 -*-
"""
@author: Jin Zitian
@time: 2020-12-21 16:55
"""

import numpy as np     
import time
from lshash.lshash import LSHash
from lshcos import LSHCos
     

#####数据构造100w条数据
xxx = [('v_'+str(i),np.random.randn(8)) for i in range(1000000)]


#####构建hash表
lshcos = LSHCos(2, 6, 8)
for n,v in xxx:
    lshcos.add(v,n)


#####查看分桶构成情况
for i in lshcos.hash_table:
    print('{:<30}{}'.format(i,len(lshcos.hash_table[i])))


#####生成输入向量
yyy = np.random.randn(8)
#####全部计算一遍，得到精确查找结果，计算耗时
start = time.perf_counter()
ddd = [(n,LSHCos.cosine_similar(v,yyy)) for n,v in xxx]
eee = sorted(ddd,key = lambda x:-x[1])[:10]
end = time.perf_counter()
print('total time cost is {}'.format(end-start))
#####lsh快速匹配，得到近似结果，计算耗时
start = time.perf_counter()
fff = [(x,y) for x,y in lshcos.query(yyy,10)]
end = time.perf_counter()
print('total time cost is {}'.format(end-start))




###########与开源的lsh的对比###########
xxx = [('v_'+str(i),np.random.randn(8)) for i in range(100)]
#####自研lsh
def a(b,r,dim,vector):
    lshcos = LSHCos(b, r, dim)
    for n,v in xxx:
        lshcos.add(v,n)
    start = time.perf_counter()
    w = lshcos.query(vector,10)
    end = time.perf_counter()
    if len(w) > 0:
        return w[0][1], end-start
    else:
        return -2, end-start

#####网上开源的lsh
def b(r,dim,vector):
    lsh = LSHash(r, dim)
    for n,v in xxx:
        lsh.index(v.tolist())
    start = time.perf_counter()
    q = lsh.query(vector.tolist(),10,'cosine')  
    end = time.perf_counter()
    qq = [(x,1-y) for x,y in q]      
    if len(qq) > 0:
        return qq[0][1], end-start
    else:
        return -2, end-start

#####效果对比
x=0
s=0
a_cost=0
b_cost=0
for i in range(5000):
    v = np.random.randn(8)
    aa,aa_cost = a(2,6,8,v)
    bb,bb_cost = b(6,8,v)
    if aa != bb:
        s += 1
        a_cost += aa_cost
        b_cost += bb_cost
        if aa > bb:
            x += 1
print('my better than git:{}'.format(x/s))
print('my_cost:{}'.format(a_cost/s))
print('git_cost:{}'.format(b_cost/s))
