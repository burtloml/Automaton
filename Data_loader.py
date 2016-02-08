# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 05:36:44 2016

@author: rafae_000
"""

import pandas as pd
import csv

file_name = './newdata/accthist.csv'
new_data_list = []


csv_data = open(file_name, 'rb')
new_data = csv.reader(csv_data)

for row in new_data:
    new_data_list.append(row)
    
csv_data.close()



new_dataframe = pd.DataFrame(new_data_list[13:], columns=new_data_list[12])