==========
LSHCos
==========

A fast Python implementation of locality sensitive hashing with cosine distance

Quickstart
==========
To create band 2 row 6 hashes for input data of 8 dimensions:

.. code-block:: python

    import numpy as np
    from lsh import LSHCos
    
    ###方式一：
    lshcos = LSHCos(2, 6, 8)
    lshcos.add([1,2,3,4,5,6,7,8],'v_1')
    lshcos.add([2,3,4,5,6,7,8,9],'v_2')
    lshcos.add([10,12,99,1,5,31,2,3],'v_3')
    lshcos.query([1,2,3,4,5,6,7,7],2)
    
    ###方式二：
    lshcos = LSHCos(2, 6, 8)
    xxx = [('v_'+str(i),np.random.randn(8)) for i in range(100)]
    yyy = np.random.randn(8)
    for name,v in xxx:
        lshcos.add(v,name)
    lshcos.query(yyy)

