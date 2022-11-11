#!/usr/bin/env python
# coding: utf-8


""" the necessary packages for preprocessing and visualization are imported """

import pandas as pd
import matplotlib.pyplot as plt

""" I import the package for retrieving a zipfile via the url command """

from urllib.request import urlretrieve
happiness_zip = 'https://storage.googleapis.com/kaggle-data-sets/894/813759/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221110%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221110T233311Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=17247f959a2ccd89399d365bd4dd3276aa7ebe5d98a78b2a397565a3428cd9a688f263679aef7eea38213e4e1a77adc9556263154bbe7d0ed42ef7a37e798a10695f5aa1a90594827467d83e4857206617d89a122edcf30a504d92b1b80bf77255be324afc02c6b13452d1bb93e3bc6f42560142e4c6aa2e0f893c9b8ab787ba9c6aad67ebb8e6714a6d641b2d3c48de7a03545640f271448364dd87142837e3a1f3a03e8bed81635cc6901fbf09ce64167911c5787947666fabae56713d12a3c60c9983d4b17821de78507d9b5617a29399bab3752a25f1b85fd210ac310a4f5f77900787fe9e26e43fe6ae3a9c74337bb34f76f63441656a0294e2b0623593'
# I used kaggle as my data source and the above zip link might have expired by the time you access the dataset, therefore the link to the page is uploaded below for easy access.

#Below is the page link to the data source
page_link = 'https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2019.csv'

#the url is then passed to the url retrieve command and also a specified name is given to the retrieved file in csv.zip format
urlretrieve(happiness_zip, 'world_happiness_report.csv.zip')


""" I used the zipfile package is to extract the zip world_happiness_report.csv.zip """
import zipfile as zf
zip_happy = zf.ZipFile('world_happiness_report.csv.zip')


#Here the files extracted are displayed via the namelist function
zip_happy.namelist()


#the extracted file I'm working with is read using the pandas method and the first 5 rows are displayed 
data_happiness = pd.read_csv(zip_happy.open('2019.csv'))
data_happiness.head()


#the numerical data is described using its command and it is displayed below
data_happiness.describe()


#the data is checked for presence of null values 
data_happiness.isnull().sum()

#Since there are no null values, the data is ready for visualization

#I sliced the first 15 rows using the iloc command. The sliced rows are what I am using for visualization
data_plot = data_happiness.iloc[:15, :]
data_plot

# Here I sliced the first 5 countries for pie chart visualization
data_pie = data_happiness.iloc[:5, :]
data_pie

"""
A function is defined for the multiple line plots and it take the variables for the x-axis and y-axis as parameters.
It also take the title, labels and colors of the plots as input parameters
"""
def multiple_line_plots(country, happiness_factors, title, my_label, my_color):
    plt.figure(figsize=(16,9), dpi=300)
    plt.title(title)
    
    for i in range(len(happiness_factors)):
        plt.plot(country, happiness_factors[i], label=my_label[i], color=my_color[i])
    plt.legend()
    plt.show()
    
    return

""" Another function is defined for the histogram subplots and it takes the columns, title, colors and alpha as parameters """
def histogram_subplot(datasets, title, color, alpha):   
    plt.figure(figsize=(12,8), dpi=100)
    
    for i in range(4):
        plt.subplot(2,2,i+1).set_title(title[i])
        plt.hist(datasets[i], alpha=alpha[i], color=color[i])   
    plt.show() 
    
    return

""" Here a function is defined for the boxplot and it takes columns, title, label and the ylabel as parameters """
def boxplot(attributes, title, label, ylabel):
    plt.figure(figsize=(8,6), dpi=100)
    plt.title(title)
    plt.boxplot(attributes, labels=label)
    plt.ylabel(ylabel)
    plt.show()
        
    return
    
""" Here I defined a function for a pie chart which accept pie_data, explode, label, title and color as parameters """
def pie_chart(pie_data, explode, label, title, color):
    plt.figure(figsize=(10,8))
    plt.title(title)
    plt.pie(pie_data, explode = explode, labels=label, colors=color, autopct='%0.2f%%')
    plt.show()
    
    return
    
""" After defining the functions, the functions are then called for visualization """

# arrays and strings are created for the input parameters for the multiple line plot function
happiness_factors = [data_plot['GDP per capita'], data_plot['Social support'], data_plot['Healthy life expectancy'], data_plot['Freedom to make life choices']]
my_label = ['GDP', 'Social support', 'Healthy life expectancy', 'Freedom']
my_color = ['blue', 'green', 'red', 'orange']
country = data_plot['Country or region']
title = 'A plot showing some factors for determining happiness in the world'

# The created inputs variables are passed into the multiple plot function and the plots are displayed below
multiple_line_plots(country, happiness_factors, title, my_label, my_color)


# Arrays are created for the defined function of the histogram subplots
datasets = [data_plot['Score'], data_plot['GDP per capita'], data_plot['Social support'], data_plot['Healthy life expectancy']]
title = ['Score', 'GDP per capita', 'Social support', 'Healthy life expectancy']
color = ['red', 'green', 'blue', 'violet']
alpha = [0.5, 0.3, 0.7, 0.4]


# The arrays are passed as input parameters into the defined function and the output is displayed below
histogram_subplot(datasets, title, color, alpha)


# The arrays and strings are created for the boxplot function
attributes = [data_happiness['Healthy life expectancy'], data_happiness['Generosity'], data_happiness['Perceptions of corruption']]
title = 'Boxplot of 3 factors that affect world happiness'
label = ['Healthy life', 'Generosity', 'Perceptions of corruption']
ylabel = 'Descriptive values'

# Here the created arrays and strings are passed into the function and the boxplot is displayed below
boxplot(attributes, title, label, ylabel)

#The parameters to be passed for the pie chart function are declared as arrays, strings and tuple below
pie_data = data_pie['Perceptions of corruption']
label = data_pie['Country or region']
title = 'Perceptions of corruption'
color = ['blue', 'red', 'yellow', 'indigo', 'green']
explode = (0, 0.2, 0, 0 , 0)

#The defined pie chart function is then passed for visualization
pie_chart(pie_data, explode, label, title, color)



