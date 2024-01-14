# Introduction

I will be looking at the NYPD Complaint Data set from NYC OpenData which examines complaints made to the New York City Police Department for 2022. This includes felony, misdemeanor, and violation crimes. Crime and violence have been a major concern in New York. In this analysis, I will be performing data exploration, wrangling, and presenting my findings.

link to the data: https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Current-Year-To-Date-/5uac-w243

```
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

url = 'https://raw.githubusercontent.com/curiostegui/CUNY-SPS/main/Data%20602/Assignment%207/NYPD_Complaint_Data_Current__Year_To_Date_.csv'
df = pd.read_csv(url)
```

The dataset contains 62999 rows and 36 columns. In briefly looking at the dataset, I'm interested in seeing information on the victim and suspect. This available to us in the form of the following columns: SUS_AGE_GROUP, SUS_RACE, SUS_SEX, VIC_AGE_GROUP, VIC_RACE, VIC_SEX

```
df.head() # previews data

df.shape # tells us the rows and columns in data
```

The summary function doesn't give us useful statistics, since the variables in this events mainly describe characteristics of the crime such as the location and individuals involved. We can also observe, like when we used the head function earlier, that there are null values. This will need to be addressed in order to generate more meaningful observations.

```
# displays summary statistics
df.describe(include='all')
```

We can observe that - with the exception of certain groups - the rank in each column, age, race and sex, is arranged similarly. The bar charts also reveal that there are large amounts of "UKNOWN" values in the age and race columns for both victims and suspects.

```
age_count = df['VIC_AGE_GROUP'].value_counts()
race_count = df['VIC_RACE'].value_counts()
sex_count = df['VIC_SEX'].value_counts()

suspect_age_count = df['SUSP_AGE_GROUP'].value_counts()
suspect_race_count = df['SUSP_RACE'].value_counts()
suspect_sex_count = df['SUSP_SEX'].value_counts()


fig, axs = plt.subplots(2, 3, figsize=(20, 12),gridspec_kw={'hspace': 0.5})

# Plot the age_count object onto the first subplot in the first row
age_count.plot.bar(ax=axs[0, 0])
axs[0, 0].set_xlabel('Age Range')
axs[0, 0].set_ylabel('Count')
axs[0, 0].set_title('Victim Age Range Count')

# Plot the race_count object onto the second subplot in the first row
race_count.plot.bar(ax=axs[0, 1])
axs[0, 1].set_xlabel('Race')
axs[0, 1].set_ylabel('Count')
axs[0, 1].set_title('Victim Race Count')

# Plot the sex_count object onto the third subplot in the first row
sex_count.plot.bar(ax=axs[0, 2])
axs[0, 2].set_xlabel('Sex')
axs[0, 2].set_ylabel('Count')
axs[0, 2].set_title('Victim Sex Count')

# Plot the suspect_age_count object onto the first subplot in the second row
suspect_age_count.plot.bar(ax=axs[1, 0])
axs[1, 0].set_xlabel('Age Range')
axs[1, 0].set_ylabel('Count')
axs[1, 0].set_title('Suspect Age Range Count')

# Plot the suspect_race_count object onto the second subplot in the second row
suspect_race_count.plot.bar(ax=axs[1, 1])
axs[1, 1].set_xlabel('Race')
axs[1, 1].set_ylabel('Count')
axs[1, 1].set_title('Suspect Race Count')

# Plot the suspect_sex_count object onto the third subplot in the second row
suspect_sex_count.plot.bar(ax=axs[1, 2])
axs[1, 2].set_xlabel('Sex')
axs[1, 2].set_ylabel('Count')
axs[1, 2].set_title('Suspect Sex Count')

plt.show()

# Modify column names for columns of interest
df.rename(columns={"CMPLNT_NUM": "ID", "BORO_NM": "boro", "CRM_ATPT_CPTD_CD": "crm_a_c", "LAW_CAT_CD": "lof_cat", "LOC_OF_OCCUR_DESC": "loc_occur", "OFNS_DESC": "off_desc", "RPT_DT": "dt_report", "SUSP_AGE_GROUP": "sus_age_group", "SUSP_RACE": "sus_race", "SUSP_SEX": "sus_sex", "VIC_AGE_GROUP": "vic_age_group", "VIC_RACE": "vic_race", "VIC_SEX": "vic_sex" }, inplace=True)
print(df.columns)

# Look at structure of data
df.info()

# Count invalid values in data
df.isnull().sum()

# Fix missing and invalid values in data
df.fillna("UNKNOWN", inplace=True)

# Create new columns based on existing columns
df['X_Y_COORD_CD'] = '(' + df['X_COORD_CD'].astype(str) + ', ' + df['Y_COORD_CD'].astype(str) + ')'
df.head()

# drop column from data
df = df.drop(['X_COORD_CD', 'Y_COORD_CD'], axis=1)

# drop row from data
df = df.drop(62998,axis=0)

# sort data based on multiple variable
df_sorted = df.sort_values(['dt_report', 'ID'])
print(df_sorted)

# filter based on some condition
vic_fem = df[(df.vic_sex=='F')]
vic_male = df[(df.vic_sex=='M')]

# convert all string values to upper case values
df.columns = df.columns.str.upper()

# Check whether numeric values are present in a column
print(is_numeric_dtype(df['BORO']))

# group dataset by one column and get count
df.groupby('SUS_SEX').size()

# change max display of rows to see the next table fully
pd.set_option('display.max_rows', 1000)

# group dataset by two columns
df.groupby(['SUS_SEX','OFF_DESC']).size()
```

# Conclusion

In my exploratory analysis I found information on both the victims and suspects in the dataset. The highest number of reported suspects are within the age of 25-44, black and male. While the highest number of victims are within the age of 25-44, black and female. This is somewhat misleading especially because there are many "UKNOWN" as well as null values. If I were to do a more thorough investigation, I would want to find a way to deal with nulls, subset a smaller group of columns that are of interest, look into the type of crimes being committed and where.

'''

