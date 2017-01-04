# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
# import numpy as np
# import matplotlib.pyplot as plt
# t = np.arange(0.0,4.0,0.1)
# plt.plot(t,t**2,'go--')
# plt.figure()
# plt.plot(t,t,'rD')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x = np.arange(0, 5,2)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
t = pd.DataFrame(y, index = x)
print t
t.to_csv("123.csv",mode='a+')
# t.plot()
# plt.show()
