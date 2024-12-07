# -*- coding: utf-8 -*-
"""exp3ds.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dubyZEkaArKGYlIVzUF2KrVBIDKTyLzS

3)**Expt:3**

The following table gives the size of the floor area (ha) and the price ($A000) for 15 houses sold in the Canberra (Australia) suburban of Aranda in 1999.


![expt3.png](data:image/png;base64,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)



ii.Explore with different formats of data and describe the procedure of storing of data?

Type these data into a data frame with column names area, sale and Price.

a. Plot sale. Price versus area.

b. Use the hist () command to plot a histogram of the sale prices.

c. Repeat (a) and (b) after taking logarithms of sale prices.

d. The two histograms emphasize different parts of the range of sale prices.

e. Describe the differences.
"""

import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Area (ha)': [694, 905, 802, 1366, 716, 963, 821, 714, 1018, 887, 790, 696, 771, 1006, 1191],
    'Sale Price ($A000)': [192.0, 215.0, 215.0, 274.0, 112.7, 185.0, 212.0, 220.0, 276.0, 260.0, 221.5, 255.0, 260.0, 293.0, 375.0]
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Rename the columns to remove spaces
df.columns = ['Area', 'Sale Price']
print(df)
plt.scatter(df['Area'], df['Sale Price'])
plt.xlabel('Area (ha)')
plt.ylabel('Sale Price')
plt.title('Sale Price vs. Area')
plt.grid(True)
plt.show()
plt.hist(df['Sale Price'], bins=10, edgecolor='yellow')
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.title('Histogram of Sale Prices')
plt.grid(True)
plt.show()

import numpy as np

df['Log Sale Price'] = np.log(df['Sale Price'])
print(df)
# Repeat scatter plot
plt.scatter(df['Area'], df['Log Sale Price'])
plt.xlabel('Area (ha)')
plt.ylabel('Log Sale Price')
plt.title('Log Sale Price vs. Area')
plt.grid(True)
plt.show()

# Repeat histogram
plt.hist(df['Log Sale Price'], bins=10, edgecolor='black')
plt.xlabel('Log Sale Price')
plt.ylabel('Frequency')
plt.title('Histogram of Log Sale Prices')
plt.grid(True)
plt.show()