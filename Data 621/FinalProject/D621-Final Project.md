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

# **Model Building**

Because our variables weren’t found to be linear or normal, this violates the linearity and normality assumptions for traditional regression models like MLR/GLS/Robost regression. The only regression technique that can be modeled without parametric assumptions is (GAM General Additive Model). Thus, making it our choice when looking at different models.

------------------------------------------------------------------------

From the data exploration, the team is aware of the non-linearity of the features in the data set. The current features may not have a linear fit, but its best fit shape can be a polynomial. Using splines, its adjusting the the line with penalties towards mse; which makes the shape more linear. In order to capture the majority of the points in the data set, the best fit line may take the shape of different curves to better fit the response 'Rating'. The team used shrinking smoothed in the features provided as it lessens the penalty.
