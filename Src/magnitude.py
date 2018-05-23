#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:31:28 2018

@author: isabellepolizzi
"""

import pandas as pd
import matplotlib.pyplot as plt

data  = pd.read_csv('/Users/isabellepolizzi/Desktop/UPC/AIS/Earthquake_study/Data/earthquake_dataset.csv')
mag = data.groupby('Magnitude').size()

plt.plot(mag, linestyle='--')
#plt.title('Number of earthquake against magnitude')
plt.xlabel('Magnitude')
plt.ylabel('Earthquake frequency')
plt.axvline(2, color='red')
plt.savefig('/Users/isabellepolizzi/Desktop/UPC/AIS/Earthquake_study/images/earthquake-magnitude.png')
plot.show()
