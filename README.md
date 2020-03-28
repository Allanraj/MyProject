# cebd1160: Analysis on Tesla Stocks for the last 10 years


| Name | Date |
|:-------|:---------------|
|Allan Raj | March 27, 2020|

-----

### Resources
Your repository should include the following:

- Python script for your analysis: Mypythonproject.py
- Results figure/saved file: Plots/
- Dockerfile for your experiment: N/A
- runtime-instructions in a file named N/A

-----

## Research Question

Analysis on Tesla Stocks for the last 10 years. 

### Abstract

I am analysing the Tesla stocks and the growth of its stocks over the years. It is a simple data analysis which will help us understand the worth of this company that has raised over the years. My goal that intrests me to handle this dataset is to know the growth/rise curve of this happening car company. Finally, I can use this analysis as a module to study on any company stocks and with detail analysis we can even predict the future growth. 


### Introduction

The dataset of Tesla stocks value are taken from Kaggle(https://www.kaggle.com/timoboz/tesla-stock-data-from-2010-to-2020#TSLA.csv) which will give an overview of rise of TESLA stock values. My study involves the stock value of their openning price, closing price, highest price, lowest price and Volume for each day from 2010-06-29 to 2020-02-03.

### Methods

I have used Matlob plotting, plotly for viewing the data for easy understanding. The reason why I chose plotting is because the data consists of date range for past 10 years and plotting the values would be more practical to visualize the data. The source or its function can be found here https://matplotlib.org/tutorials/introductory/pyplot.html 

[<img src="https://github.com/Allanraj/MyProject/blob/master/plots/TSLA-Stocks_Analysis/TSLA_plotly.png">](https://github.com/Allanraj/MyProject/blob/master/plots/TSLA-Stocks_Analysis/)

### Results

The plotting results are shown below:

The first image is a Pie chart which explains the total volume of the stock for each year. It also gives the total number for each year.
 
[<img src="https://github.com/Allanraj/MyProject/blob/master/plots/TSLA-Stocks_Analysis/TSLA_total_volume.png">](https://github.com/Allanraj/MyProject/blob/master/plots/TSLA-Stocks_Analysis/)

The second image is a total understanding of the highest price, lowest price and closing price for last 10 years. This image gives an understanding about the Stock rise over the years even though there was dip in the year Q2 of the year 2019. 
 
[<img src="https://github.com/Allanraj/MyProject/blob/master/plots/TSLA-Stocks_Analysis/Stocks_comparision.png">](https://github.com/Allanraj/MyProject/blob/master/plots/TSLA-Stocks_Analysis/)

### Discussion

I have used two methods to analyse my data, the first one is a pie chart using Matplotlib. The reason I used pie chart is to find the quantitative value of stocks volume for each year.

The other plotting using plotly/scatterchart gives me a visual representation of steady Stocks growth over the year. 

The next step I would love to see is the Bar chart for each year on different field by concatenating each year data.


### References
https://www.kaggle.com/timoboz/tesla-stock-data-from-2010-to-2020#TSLA.csv
