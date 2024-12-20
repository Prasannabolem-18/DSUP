# -*- coding: utf-8 -*-
"""exp5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11CqQyzrI6BMogk-T1wBEE54jXj2pLTJp

5)Apply basic statistical methods on Sample Datasets
"""

import numpy as np

# Sample dataset of heights (in centimeters) of students
heights = [160, 165, 170, 155, 158, 163, 180, 175, 168, 175]
# Sample dataset of exam scores of students
exam_scores = [85, 90, 78, 88, 92, 95, 80, 85, 89, 93]
mean_height = np.mean(heights)
mean_scores = np.mean(exam_scores)

print("Mean height:", mean_height)
print("Mean scores:", mean_scores)
median_height = np.median(heights)
median_scores = np.median(exam_scores)

print("Median height:", median_height)
print("Median scores:", median_scores)

from scipy import stats
mode_height = stats.mode(heights)
mode_scores = stats.mode(exam_scores)

print("Mode height:", mode_height)
print("Mode scores:", mode_scores)
variance_height = np.var(heights)
std_deviation_height = np.std(heights)

variance_scores = np.var(exam_scores)
std_deviation_scores = np.std(exam_scores)

print("Variance of height:", variance_height)
print("Standard deviation of height:", std_deviation_height)
print("Variance of scores:", variance_scores)
print("Standard deviation of scores:", std_deviation_scores)
range_height = np.max(heights) - np.min(heights)
range_scores = np.max(exam_scores) - np.min(exam_scores)

print("Range of height:", range_height)
print("Range of scores:", range_scores)
# Assuming we have another dataset of weights (in kg) of students
weights = [50, 55, 60, 45, 48, 52, 70, 65, 58, 65]
correlation_height_weight = np.corrcoef(heights, weights)[0, 1]
print("Correlation between height and weight:", correlation_height_weight)

import numpy as np

# Sample dataset of heights (in centimeters) of students
heights = [12,17,28,30,58]
# Sample dataset of exam scores of students
exam_scores = [98,97,98,97,100]
mean_height = np.mean(heights)
mean_scores = np.mean(exam_scores)

print("Mean height:", mean_height)
print("Mean scores:", mean_scores)
median_height = np.median(heights)
median_scores = np.median(exam_scores)

print("Median height:", median_height)
print("Median scores:", median_scores)

from scipy import stats
mode_height = stats.mode(heights)
mode_scores = stats.mode(exam_scores)

from statistics import multimode
result=multimode(exam_scores)
for i in result:
  print("Scores Mode:",i,"Count:",exam_scores.count(i))
result1=multimode(heights)
for j in result1:
  print("Height Mode:",j,"Count:",heights.count(j))
print("Mode height:", mode_height)
print("Mode scores:", mode_scores)
variance_height = np.var(heights)
std_deviation_height = np.std(heights)

variance_scores = np.var(exam_scores)
std_deviation_scores = np.std(exam_scores)

print("Variance of height:", variance_height)
print("Standard deviation of height:", std_deviation_height)
print("Variance of scores:", variance_scores)
print("Standard deviation of scores:", std_deviation_scores)
range_height = np.max(heights) - np.min(heights)
range_scores = np.max(exam_scores) - np.min(exam_scores)

print("Range of height:", range_height)
print("Range of scores:", range_scores)
# Assuming we have another dataset of weights (in kg) of students
weights = [60,55,50,45,40]
correlation_height_weight = np.corrcoef(heights, weights)[0, 1]
print("The correlation between height and weight is:",correlation_height_weight)