
'''
In this assignment, you will practice loading data into your python environment. It is
recommended that you use either google colab or juypter notebook, however, you may
use any environment you prefer as long as you are using the pandas library.
From the following link, choose two files to answer the questions below.
https://github.com/data602sps/datasetspractice

In addition, you will also search the internet to find two datasets to answer the
questions below.

Websites to find data:
● https://opendata.cityofnewyork.us/
● https://datasetsearch.research.google.com/
● https://www.kaggle.com/datasets
● http://archive.ics.uci.edu/ml/index.php
● https://data.gov/

Q1. Load your dataset into python using the pandas library and save data into a
dataframe named dfi (where i is one of your datasets, for a total of 4).
Q2. Preview your data by calling your dataframe’s name. How many columns and rows
do you see?
Q3. Examine the shape of your data using the .shape command and the data types of
your columns using .dtypes.
Q4. Use .describe() on your data. What do you notice about your data? What does this
command return?
Q5. Use the .head() and .tail() command - what does this do?

Extra Credit (3 pts)
1. Choose one of your datasets and remove the header information. (Can delete
the row in excel, etc..)
2. Import the data into your environment using pandas. Display the .head() of your
data showing no header information.
3. Using pandas, update the dataset to include the header information. Display the
updated data using .head().

Extra Credit (3 pts)
1. Import a “dirty” dataset from the internet into your environment. (Missing values,
improper coding of columns, etc.)
2. Clean or “tidy” the data when loading into python using pandas


'''

import pandas as pd

url1 = 'https://raw.githubusercontent.com/data602sps/datasetspractice/main/nba.csv'
url2 = 'https://raw.githubusercontent.com/data602sps/datasetspractice/main/salarydata.csv'
url3 = 'https://raw.githubusercontent.com/curiostegui/CUNY-SPS/main/Data%20602/Assignment%206/honda_sell_data.csv'
url4 = 'https://raw.githubusercontent.com/curiostegui/CUNY-SPS/main/Data%20602/Assignment%206/ditry_data_sample.csv'

dfi = pd.read_csv(url1) 
dfi2 = pd.read_csv(url2)
dfi3 = pd.read_csv(url3)
dfi4 = pd.read_csv(url4)

#--- First dataset ---#

'''
Christian's Response:
dfi contains 458 rows and 9 columns. This is also shown via the .shape function. 
The .types function tell us that the df has no attribute types.
The .describe function shows us the top 5 and bottom 5 rows of the dataframe. 
It also includes the name of the columns, and the rows and columns.
The .head function returns only the top 5 rows of the df and some of the columns. 
The .tail function returns the bottom 5 rows of the df and some of the columns.
'''

# print df
dfi

# examine shape & type
print(dfi.shape)
print(dfi.types)

# use describe
dfi.describe

# use .head and .tail 
dfi.head()  
dfi.tail()  

#--- Second dataset ---#

'''
Christian's Response:
dfi2 contains 51 rows and 9 columns. This is also shown via the .shape function. 
The .types function tell us that the df has no attribute types.
The .describe function shows us the top 5 and bottom 5 rows of the dataframe. 
It also includes the name of the columns, and the rows and columns.
The .head function returns only the top 5 rows of the df and some of the columns. 
The .tail function returns the bottom 5 rows of the df and some of the columns.
'''

# print df
dfi2

# examine shape & type
print(dfi2.shape)
print(dfi2.types)

# use describe
dfi2.describe

# use .head and .tail 
dfi2.head()  
dfi2.tail()  


#--- Third dataset ---#

'''
Christian's Response:
dfi3 contains 49 rows and 25 columns. This is also shown via the .shape function. 
The .types function tell us that the df has no attribute types.
The .describe function shows us the top 5 and bottom 5 rows of the dataframe. 
It also includes the name of the columns, and the rows and columns.
The .head function returns only the top 5 rows of the df and some of the columns. 
The .tail function returns the bottom 5 rows of the df and some of the columns.
'''


# print df
dfi3

# examine shape & type
print(dfi3.shape)
print(dfi3.types)

# use describe
dfi3.describe

# use .head and .tail 
dfi3.head()  
dfi3.tail()  

### Extra Credit ###

# remove header
dfi3_nohead = pd.read_csv(url3, header=None)

# use .head function on no header df
dfi3_nohead.head()

# add header
dfi3_nohead.columns = dfi3.columns

dfi3_nohead.head()
   
#--- Fourth dataset ---#

'''
Christian's Response:
dfi contains 19 rows and 16 columns. This is also shown via the .shape function. 
The .types function tell us that the df has no attribute types.
The .describe function shows us the top 5 and bottom 5 rows of the dataframe. 
It also includes the name of the columns, and the rows and columns.
The .head function returns only the top 5 rows of the df and some of the columns. 
The .tail function returns the bottom 5 rows of the df and some of the columns.
'''

# print df
dfi4

# examine shape & type
print(dfi4.shape)
print(dfi4.types)

# use describe
dfi4.describe

# use .head and .tail 
dfi4.head()  
dfi4.tail()  

### Extra Credit ###

### clean dirty dataset

# seperate by segment type: consumer, corporation, home office

dfi4_cons = dfi4.iloc[:, 0:6]
dfi4_corp = dfi4.iloc[:, [0] + list(range(6,11))]
dfi4_home = dfi4.iloc[:, [0] + list(range(11,16))]

# add column which uniquely lables segment type

dfi4_cons['Segment'] = 'Consumer' 
dfi4_corp['Segment'] = 'Corporate'
dfi4_home['Segment'] = 'Home Office'

# rename columns

dfi4_cons.columns = ['OrderID', 'FirstClass', 'SameDay', 'SecondClass', 'StandardClass','Sales','Segment']
dfi4_corp.columns = ['OrderID', 'FirstClass', 'SameDay', 'SecondClass', 'StandardClass','Sales','Segment']
dfi4_home.columns = ['OrderID', 'FirstClass', 'SameDay', 'SecondClass', 'StandardClass','Sales','Segment']

# remove rows that contain information not of interest

dfi4_cons = dfi4_cons.drop(dfi4_cons.index[0:2])
dfi4_corp = dfi4_corp.drop(dfi4_corp.index[0:2]) 
dfi4_home = dfi4_home.drop(dfi4_home.index[0:2]) 

# merge all shipping type purchases column named Shipmode

dfi4_cons = pd.melt(dfi4_cons, id_vars=['OrderID', 'Sales', 'Segment'], 
                    var_name='ShipMode', value_name='SalesValue')
dfi4_corp = pd.melt(dfi4_corp, id_vars=['OrderID', 'Sales', 'Segment'], 
                    var_name='ShipMode', value_name='SalesValue')
dfi4_home = pd.melt(dfi4_home, id_vars=['OrderID', 'Sales', 'Segment'], 
                    var_name='ShipMode', value_name='SalesValue')

# drop Sales column, which contains duplicate values

dfi4_cons = dfi4_cons.drop('Sales', axis=1)
dfi4_corp = dfi4_corp.drop('Sales', axis=1)
dfi4_home = dfi4_home.drop('Sales', axis=1)


# remove null values

dfi4_cons = dfi4_cons.dropna(subset=['SalesValue'])
dfi4_corp = dfi4_corp.dropna(subset=['SalesValue'])
dfi4_home = dfi4_home.dropna(subset=['SalesValue'])

# merge columns row wise

clean_data = pd.concat([dfi4_cons, dfi4_corp, dfi4_home], axis=0)

# print clean data set

clean_data





























