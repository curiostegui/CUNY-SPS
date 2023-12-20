DATA 621 Final Project - Google Play Store: Using Linear Regression to Predict App Ratings
================
Christian Uriostegui, Vyanna Hill, Jose Rodriguez

-   [**Abstract**](#abstract)
-   [**Introduction**](#introduction)
    -   [**Methodology**](#methodology)
-   [**Data Preprocessing**](#datapreprocessing)
    -   [**Data Subset**](#datasubset)
    -   [**Missing Data**](#missingdata)
    -   [**Distribution of Numeric Variables**](#distributionofnumericvariables)
    -   [**Checking for Multi-Colinearity**](#checkingformulticolinearity)

------------------------------------------------------------------------

# **Abstract**

For app developers, their app performance in the app store accounts for future funding for new projects. This project reviewed linear regression and its accuracy towards its predictions in an app’s rating in the Google App Store. In the first path of the project, the team reviewed the Google App Store data set for its viability in linear regression as the response feature is continuous and not discrete for count regression. After a review of the data set’s non-normality and model performance, the project’s regression scope expanded toward generalized additive modeling (GAM). 

The team created four different GAMs models with various splines on the features. The splines help better fit the highly skewed features of rating count and stars, as the increased knots on the features boosted the R^2 20%+. This exploration of the different types of splines resulted in the third model with the closest fit with an R^2 of 96%, a deviance of 669, and an RSME of 15%. The final model’s performance highlighted a need for smoothing with a non-normal data set with a continuous response.

------------------------------------------------------------------------

# **Introduction**

For app developers, the funding source for the next project depends on the success of their published apps.
The app’s popularity in continuous active users partially depends on the app store. Consumers review
multiple areas of the app’s review page than its volume of downloads: whether the app won any awards, the
average rating, the download price, etc. Apps with quality ratings receive a bonus with their position in the
app store at the highest viewability and attractive banners on their popularity. Data science can inform the
project team of their predicted rating in the app store and re-strategize the next project. For this project,
the team will assess which regression model best fits app rating predictions

------------------------------------------------------------------------

## Methodology

The team created a process for the rating predictions: data pre-processing, exploration, preparation, model
building, model selection, experiment and results.For the project’s data, the team sourced a scraped pull
from the Google App store by Prakash and Koshy (2021) on Kaggle. The data set at first glance need to be
processed before the team can explore the data set’s statistics

# **Data Preprocessing**

## Data Subset

The data was pre-processed using the tidyverse package. First, a column subset was taken which yielded a total of 16 variables: 15 of those being predictors (x) and one target variable (y). We removed App.Name, App.Id, Developer.Id, Developer.Website, Developer.Email, Privacy.Policy, Scraped.Time, Currency from our models. The target variable, also known as the response variable, is 'Rating'. 'This column 'Rating' contains the accumulated average score of a given app between 0 and 5 stars. 

![](https://github.com/curiostegui/CUNY-SPS/blob/main/Data%20621/FinalProject/images/variables.png)<!-- -->

------------------------------------------------------------------------

## Missing Data

Missing data was handled by removing NA values. Two reasons prompted the omission of missing values: 1) removing missing values only removed about 5% of observations, 2) It is not known if the missing data points are missing completely at random (MCAR), hence imputation could introduce bias to the model.

![](https://github.com/curiostegui/CUNY-SPS/blob/main/Data%20621/FinalProject/images/nulls.png)<!-- -->

------------------------------------------------------------------------
## Distribution of Numeric Variables

All numerical variables were found to be highly skewed. Transformations such as box-cox, logarithmic and square-root were explored. However, they did not normalize the data. Consequently, several assumptions are violated: 1) Normality, 2) linearity. Ultimately, this leads to assuming that the data exhibits complex relationships where a Nonparametric Regression could be the best choice. 

![](https://github.com/curiostegui/CUNY-SPS/blob/main/Data%20621/FinalProject/images/distributionofnumericvariables.png)<!-- -->

------------------------------------------------------------------------

## Checking for Multi-Colinearity

'Maximum.Installs' and 'Minimum.Installs' were found to be highly correlated to 'Installs'.

![](https://github.com/curiostegui/CUNY-SPS/blob/main/Data%20621/FinalProject/images/multicolinearity.png)<!-- --> 

------------------------------------------------------------------------

## Key Metrics in Championship Teams

-   **possession** : counted every time a player scores, misses the
    shot, turns the ball over, or gets fouled
-   **pace** = (possessions/minutes) \* 48
-   **injuries** among teams in the finals

For our study we’ll be examining NBA teams in the finals between
2016-2020 and look at key metrics such as: **Possession** which is
counted every time a player scores, misses the shot, turns the ball over
or gets fouled; **Pace** which provides the amount of possessions in a
48 minute period (average NBA game). If tempo is increasing we will also
see this reflected in these two statistics. We will also look at
injuries among teams in the finals.

------------------------------------------------------------------------

# **Analysis**

## Pace

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

The pace by teams is visualized above. Each of the colored dashed lines
represents the pace for each team for seasons 1996-97 to 2020-21. The
black solid line represents the average pace of all teams for each
season.

From the visualization, we see an increase in pace for NBA teams over
time.

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

To further support the previous visualization, the evolution of team
pace from seasons 1996 to 2020 is visualized above. As mentioned
earlier, we see an increase in pace for NBA teams over time.

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

Let’s take a closer look at the pace by teams. Each of the colored
dashed lines is the pace for each team over the years. The dashed black
line represents the average pace for each season, and is the same in
each facet. The solid black line represents the average pace for each
team, and is different in each facet.

From the visualization, we can see that every team has seen an increase
in pace. Also, all teams in the 2020 season have a pace greater than
their team average pace.

------------------------------------------------------------------------

## Possessions

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-8-1.png)<!-- -->

The possessions by teams is visualized above. Each of the colored dashed
lines represents the possessions for each team for seasons 1996-97 to
2020-21. The black solid line represents the average possessions of all
teams for each season.

From the visualization, we see two big dips in 1998 and 2011. The reason
for the dips in 1998 and 2011 is because the games were cut short due to
player negotiations for contracts. We also observe lower possessions for
2019 and 2020. That may be due to COVID-19, since they played less
games. Without the big drops in 1998 and 2011, and in 2019 and 2020, we
can see a small increase in possessions.

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-9-1.png)<!-- -->

In this visualization, we see the evolution of possessions from seasons
1996 to 2018. We didn’t include 2019 and 2020 in this visualization
because there were decreases due to fewer games played due to COVID-19.
As mentioned earlier, we see an overall increase in possessions for NBA
teams.

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-10-1.png)<!-- -->

Here we have a data visualization of the possessions by teams. Each of
the colored dashed lines is the possessions for each team over the
years. The dashed black line represents the average possessions for each
season, and is the same in each facet. The solid black line represents
the average possessions for each team, and is different in each facet.

------------------------------------------------------------------------

## Injuries

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-14-1.png)<!-- -->

Here we have a bar plot of the total number of injured players by teams
for 2016 to 2020. We see that Charlotte Hornets and Oklahoma City
Thunder had the fewest number of injured players, while Milwaukee Bucks,
Brooklyn Nets, and Dallas Mavericks had the highest number of injured
players. 16 of the teams had more than the average number of injured
players. That’s a lot of injuries!

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-15-1.png)<!-- -->

This is a side-by-side box-and-whisker plot, or a box plot of the cash
earned while injured by teams for seasons 2016-17 to 2020-21. Each of
the box plots contains 5 important values: the minimum, first quartile,
median or second quartile, third quartile, and maximum. The rectangle
displays the interquartile range (IQR), and lone points are outliers.

From this visualization, we can see that Brooklyn Nets has the highest
median cash earned while injured. This may be because more injuries
caused more money to be lost. Brooklyn Nets also has a very large
outlier. We also observe that Detroit Pistons have the lowest median
cash earned due to less injuries. We can also see that Golden State
Warriors has the biggest IQR, and Utah Jazz has the smallest IQR.

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-16-1.png)<!-- -->

The cash earned while injured by teams is visualized above. Each of the
colored dashed lines represents the cash earned while injured for each
team for seasons 2016-17 to 2020-21. The black solid line represents the
average cash earned while injured of all teams for each season.

From the visualization, we see an increase in cash earned while injured
over time.

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-17-1.png)<!-- -->

Now, let’s take a closer look at the cash earned while injured by teams.
Each of the colored dashed lines is the cash earned while injured for
each team over the years. The dashed black line represents the average
cash earned while injured for each season, and is the same in each
facet. The solid black line represents the average cash earned while
injured for each team, and is different in each facet.

From the visualization, we can see that even though it is not apparent
for every team, some teams, like Brooklyn Nets and Golden State
Warriors, see an increase in cash earned while injured. It seems like
teams are losing a lot of money because of injuries.

------------------------------------------------------------------------

## Speed

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-20-1.png)<!-- -->

The average speed by teams is visualized above. Each of the colored
dashed lines represents the average speed for each team for seasons
2016-17 to 2020-21. The black solid line represents the average speed of
all teams for each season.

From the visualization, we see the average speed of Cleveland Cavaliers
dropped in 2018 and 2019 because the NBA tracked one player’s speed who
only played one game, causing the team average to drop. Though not big,
we do see a slight increase in average speed over time.

------------------------------------------------------------------------

## Distance

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-23-1.png)<!-- -->

The average distance by teams is visualized above. Each of the colored
dashed lines represents the average distance for each team for seasons
2016-17 to 2020-21. The black solid line represents the average speed of
all teams for each season.

From the visualization, we can see a slight increase in average distance
by teams over time. Speed and distance are not tracked for every game
and every player, so team averages will be skewed.

------------------------------------------------------------------------

## Correlation

![](NBA_Tempo_and_Injuries_files/figure-gfm/unnamed-chunk-25-1.png)<!-- -->

The visualization above is a pair plot. The variable names are displayed
on the outer edges of the matrix. The scatter plot in the lower triangle
shows the relationship between two variables. In the scatter plot, we
have a loess smoother to help us see the relationship between two
variables and foresee trends. The boxes along the diagonal display the
density plot for each variable. A density plot helps us visualize the
distribution of the data. The boxes in the upper right corner display
the Pearson correlation coefficient between two variables. The Pearson
correlation, or r, gives us the magnitude and direction of the linear
relationship between two variables and has a value between -1 and +1.
The higher the absolute value of r, the stronger the correlation. -1
signifies a perfect negative linear correlation. 0 signifies no linear
relationship between the two variables. +1 signifies a perfect positive
linear correlation. There are other types of correlation; however, they
were not used: Spearman and Kendall.

Looking at the scatter plot and loess smoother, the number of games
missed and earned while injured displays a clear positive relationship.
There is also a clear positive relationship between the number of
injured players and number of games missed. There is a slight positive
linear relationship between pace and number of injured players, pace and
earned while injured, pace and average distance, possessions and average
speed, and number of injured players and earned while injured.

Looking at the density plot for possessions, we observe two peaks, which
means it is bimodal. This may be caused by looking at all the teams and
all the seasons at once. For number of games missed and earned while
injured, it looks like they are right skewed, which means that the mean
is greater than the median. For average speed, it looks like it is left
skewed, which means that the mean is less than the median.

