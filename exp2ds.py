# -*- coding: utf-8 -*-
"""exp2ds.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16KQp7Wc1ueGQ8M3W7jnAd5nhCH6Rs1cK
"""

pwd

"""2)write a program for accessing/importing and exporting data"""

import pandas as pd
data=pd.read_excel(r'sample_data/DSUPexp2.xlsx',index_col=0)
print(data)
print('first 5 rows')
print(data.head(5))
data.head(5).to_excel('test.xlsx',index=False)