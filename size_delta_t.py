from numpy import mean
from numpy import std
import pandas as pd
from scipy.spatial import distance

#read data into a dataframe
df = pd.read_csv('dataset207_1.csv', usecols=[1,4])



#printing the whole data
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)

#Putting the data from delta_T into an array using np
Δt_array = df.to_numpy()
print(Δt_array)



#Get the frequency of the values in the dataset
df = df.reset_index()
delta_Occur = df['delta_T'].value_counts()
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
     print('Frequency of occurence of Δt values: \n', delta_Occur)

#Getting the percentage of occurence of the dataset
delta_percent = df['delta_T'].value_counts(normalize=True) * 100
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
     print('Percentages of occurence of Δt values: \n', delta_percent)



#Grouping the bins
bins = [-1, 0.000000, 2.000000, 5.000000, 8.000000, 11.000000]

labels = ['-1-0.000000', '0.000001-2.000000', '2.000001-5.000000', '5.000001-8.000000', '8.000001-11.000000']

bin_spread = pd.cut(df['delta_T'], bins=bins, labels=labels, include_lowest=True)


#Percentage distribution of the bins
delta_val = bin_spread.value_counts(normalize=True)
print(delta_val)

delta_per = bin_spread.value_counts(normalize=True) * 100
print(delta_per)

#Obtaining the mean of the data
delta_average_of_array = mean(Δt_array)
print('Mean = %.3f'% (delta_average_of_array))

#Obtaining the standard deviation of the Δt
std_of_array = std(Δt_array)
print('Standard Deviation = %.3f' %(std_of_array))


#Calculating the euclidean distance by standardisation

euclidean_d = ((Δt_array) - (delta_average_of_array)) / (std_of_array)
print('The standardised array of delta_T is: \n', euclidean_d)

#Obtaining Euclidean Distance for size
eucl_d = distance.euclidean(df['delta_T'], df['GOOSE LENGTH'])

print('Euclidean Distance:', eucl_d)

'''#Obtaining the Euclidean Distance for delta_T

eucl_d = distance.euclidean(df['delta_T'], [0])

print('Euclidean Distance for Change in Time:', eucl_d)
'''

