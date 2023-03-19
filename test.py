from matplotlib import pyplot as plt
import numpy as np
randn = np.random.randn
from pandas import *

idx = Index(np.arange(1,11))
df = DataFrame(randn(10, 5), index=idx, columns=['A', 'B', 'C', 'D', 'E'])
df.style.background_gradient(cmap='Greens',axis =1,low=0,high=1)
vals = np.around(df.values,2)
norm = plt.Normalize(vals.min()-1, vals.max()+1)
colours = plt.cm.ScalarMappable(cmap='GnBu', norm=plt.Normalize(vals.min()-1,vals.max()+1))

fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(111, frameon=True, xticks=[], yticks=[])

the_table=plt.table(cellText=vals, rowLabels=df.index, colLabels=df.columns, 
                    colWidths = [0.03]*vals.shape[1], loc='center',
                    cellColours=colours
                    )
plt.show()