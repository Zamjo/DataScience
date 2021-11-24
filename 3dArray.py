# -*- coding: utf-8 -*-
import numpy as np
arr = np.arange(1, 28, 1).reshape(3,3,3)
arr2 = arr.astype(np.float32)
print(arr2)
print(arr2.dtype)
