# Assignment 8

## Introduction

The dataset that will be used is from Kaggle. The original source will be linked below. The data contains the results of a survey conducted on undergraduate students which asked for their opinion on the role of A.I. in education. The survey uses a variety of rating scales, and likert scale questions.

I chose this dataset because Chat GPT and other forms of AI models have been very polarizing in the education field. Being that students in an undergrad program may have some exposure to this technology, I'm curious about their perception of these tools. In my study, I will perform basic data exploration and visualization using both matplotlib and seaborn library.

link to the data: https://www.kaggle.com/datasets/gianinamariapetrascu/survey-on-students-perceptions-of-ai-in-education

## Data Exploration

```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/curiostegui/CUNY-SPS/main/Data%20602/Assignment%208/Survey_AI.csv'
df = pd.read_csv(url)
```

In my exploration of the data, I noted that there are 91 survey respondents. I also noted that there are no null values in the dataset. There also wasn't any significant information in looking at the statistic summary of each column.

```
df.head()

# checks if each column has Nulls
df.isnull().any()

for col in df.columns:
    unique_values = df[col].unique()
    print(f"Unique values for {col}): {unique_values}")
    
df.shape

df.columns    

# Data Wrangling

'''
in the exploration phase I found that some of the column names had white space and hashtag symbols. I opted to remove them for data cleaning purposes.    
'''

df.rename(columns=lambda x: x.replace('#', '.'), inplace=True)
df.rename(columns=lambda x: x.replace(' ', ''), inplace=True)
df.columns

# Visualizations
```

### Part 1:

In the visualizations below, I will be looking at AI knowledge among participants comparison, as well as A.I. sentiment by year of study (1 = Year 2, 2 = Year 3). I opted to use a histogram for the analysis on AI knowledge among participants and a barplot to look at sentiment by year of study.

In addition to creating the visuals, I will be practicing modifying certain properties of the visuals including:

\* Using and changing a legend position

\* Change a legend font size

\* Create a single legend for all subplots

\* Change the title and x/y labels

\* Change colors

```
# Plot 1: Distribution of AI knowledge among participants
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(df['Q1.AI_knowledge'], bins=10, edgecolor='black')
ax.set_title('Distribution of AI Knowledge')
ax.set_xlabel('AI Knowledge Level')
ax.set_ylabel('Frequency')
ax.tick_params(axis='both', which='major', labelsize=12)
plt.show()

# Plot 2: Proportion of participants who feel positively about AI by year of study
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))
for i, year in enumerate(df['Q13.Year_of_study'].unique()):
    data = df[df['Q13.Year_of_study'] == year]
    ax = axs[i]
    ax.bar(['Positive', 'Negative'], 
           [data['Q5.Feelings'].value_counts(normalize=True)[1], data['Q5.Feelings'].value_counts(normalize=True)[2]], 
           color=['#43A047', '#E53935'], width=0.5)
    ax.set_title(f'Year {year}')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Proportion')
    ax.set_ylim(0, 1)
    ax.tick_params(axis='both', which='major', labelsize=12)
    
plt.suptitle('Proportion of Participants with Positive and Negative Feelings about AI by Year of Study')
plt.show()    
```

We can see in the visuals that survey participants from this university scored above 4 in A.I knowledge - meaning they have exposure to A.I. We can also see there isn't much of a change in sentiment about A.I from Year 2 (labeled 1) to Year 3 (labeled 2), though there is a slight increase positive sentiment.

### Part 2:

In this section, I will be re-creating the visualizations I created in Matplotlib, in Seaborn.

```
# Plot 1: Distribution of AI knowledge among participants
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df['Q1.AI_knowledge'], bins=10, edgecolor='black', ax=ax)
ax.set_title('Distribution of AI Knowledge')
ax.set_xlabel('AI Knowledge Level')
ax.set_ylabel('Frequency')
ax.tick_params(axis='both', which='major', labelsize=12)
plt.show()

# Plot 2: Proportion of participants who feel positively about AI by year of study
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))
for i, year in enumerate(df['Q13.Year_of_study'].unique()):
    data = df[df['Q13.Year_of_study'] == year]
    ax = axs[i]
    sns.barplot(x=['Positive', 'Negative'], 
                y=[data['Q5.Feelings'].value_counts(normalize=True)[1], data['Q5.Feelings'].value_counts(normalize=True)[2]], 
                palette=['#43A047', '#E53935'], ax=ax)
    ax.set_title(f'Year {year}')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Proportion')
    ax.set_ylim(0, 1)
    ax.tick_params(axis='both', which='major', labelsize=12)
    
plt.suptitle('Proportion of Participants with Positive and Negative Feelings about AI by Year of Study')
plt.show()
```

### Part 3

When we compare the visuals in both Matplotlib and Seaborn, at first glance we can see that there weren't many differences in syntax. Seaborn is built on top of Matplotlib and so there are many similarities. It does overall offer many more visualizations such as the violin plot and swarm plots. In the charts we do see very small differences in the colors. We do also see the \`palette\` parameter in Seaborn versus the \`color\` parameter in Matplotlib.

### Conclusion

We can see overall that not is only is there some knowledge in A.I, but there is overwhelming positive sentiment about the tool. Something I would like to further explore is in what areas do respondents feel that A. I might be more useful or more harmful.

