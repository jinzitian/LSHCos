# -*- coding: utf-8 -*-
"""
@author: Jin Zitian
@time: 2020-12-21 16:55
"""

import numpy as np

class LSHCos(object):
    def __init__(self, bucket_num, row_num, v_dim):
        self.bucket_num = bucket_num
        self.row_num = row_num
        self.hash_table = {}
        self.vector_idmap = {}
        self.R = self.generate_R(bucket_num, row_num, v_dim)
        
    def generate_R(self, bucket_num, row_num, v_dim):
        return np.random.randn(bucket_num * row_num, v_dim)
    
    @classmethod
    def cosine_similar(cls, a, b):
        return np.dot(a, b) / ((np.dot(a, a) * np.dot(b, b)) ** 0.5)

    def cosine_distance(self, a, b):
        return 1 - self.cosine_similar(a,b)

    def cosine_lsh_hash_signature(self, vector):
        r_product = np.dot(self.R, vector)
        a = np.where(r_product > 0, 1, r_product)
        b = np.where(a >= 0, a, -1)
        return b
    
    def get_hash_buckets(self, signature):
        buckets = []
        for i in range(self.bucket_num):
            b = ','.join([str(int(j)) for j in signature[i*self.row_num : (i+1)*self.row_num]])
            buckets.append(str(i) + '_' + b)
        return buckets
    
    def add(self, vector, name):
        if isinstance(vector, (list, np.ndarray)):
            array_v = np.array(vector)
            self.vector_idmap[name] = array_v
            signature = self.cosine_lsh_hash_signature(array_v)
            buckets = self.get_hash_buckets(signature)
            for b in buckets:
                if b in self.hash_table:
                    value = self.hash_table.get(b)    
                    value.append(name)
                else:
                    self.hash_table[b] = [name]
        else:
            raise TypeError("only list or ndarray is support")
              
    def query(self, vector, top_k=None):
        if isinstance(vector, (list, np.ndarray)):
            array_v = np.array(vector)
            signature = self.cosine_lsh_hash_signature(array_v)
            buckets = self.get_hash_buckets(signature)
            all_candidates = []
            for b in buckets:
                datas = self.hash_table.get(b,[])
                all_candidates.append((datas,len(datas)))
            top2_candidates = sorted(all_candidates, key = lambda x:-x[1])[:2]
            candidates = set()
            for t in top2_candidates:
                candidates.update(t[0])
            query_result = [(t, self.cosine_similar(array_v, self.vector_idmap[t])) for t in candidates]
            sort_result = sorted(query_result, key = lambda x:-x[1])
            return sort_result[:top_k] if top_k else sort_result
        else:
            raise TypeError("only list or ndarray is support")
        

if __name__ == '__main__':
    
    ###方式一：
    lshcos = LSHCos(2, 6, 8)
    lshcos.add([1,2,3,4,5,6,7,8],'v_1')
    lshcos.add([2,3,4,5,6,7,8,9],'v_2')
    lshcos.add([10,12,99,1,5,31,2,3],'v_3')
    lshcos.query([1,2,3,4,5,6,7,7])
    
    ###方式二：
    lshcos = LSHCos(2, 6, 8)
    xxx = [('v_'+str(i),np.random.randn(8)) for i in range(100)]
    yyy = np.random.randn(8)
    for name,v in xxx:
        lshcos.add(v,name)
    lshcos.query(yyy)
