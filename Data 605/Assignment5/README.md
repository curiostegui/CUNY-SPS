# Assignment 5

## Question 1

A new test for multinucleoside-resistant (MNR) human immunodeficiency virus type 1 (HIV-1) variants was recently developed. The test maintains 96% sensitivity, meaning that, for those with the disease, it will correctly report “positive” for 96% of them. The test is also 98% specific, meaning that, for those without the disease, 98% will be correctly reported as “negative.” MNR HIV-1 is considered to be rare (albeit emerging), with about a .1% or .001 prevalence rate.

Given the prevalence rate, sensitivity, and specificity estimates, what is the probability that an individual who isreported as positive by the new test actually has the disease? If the median cost (consider this the best point estimate) is about \$100,000 per positive case total and the test itself costs \$1000 per administration, what is the total first-year cost for treating 100,000 individuals?

### Christian's Response

```
We can solve this problem using the Bayes' theorem. In this case we're going to solve for the probability of having the disease given that they test positive:

$$P(A|B) = {P(B|A) \times P(A)}/{P(B|A) \times P(A)+(B|not A) \times P(notA)}$$
$$P(A|B) = {0.96 \times 0.001}/{0.96 \times 0.001 + 0.02 \times 0.999}$$
$$P(A|B) = 0.045 $$

To calculate the first-year cost for treating 100,000 individuals, we'll look at the amount who will test positive in the population of 100,000.

First we'll multiply the prevalence rate by the population. If we perform 100,000 $\times$ 0.001 = 100 individuals will be expected to have the disease. Because of the test sensitivity of 96%, we know that 96 out of the 100 will test positive. 

Next, we have to look at the remainder of our population. Since we have a test specificity of 98%, that means we will have to calculate those individuals who don't have the disease that will test positive. If we calculate, 99,900 (rest of individuals who don't have the disease) * (1-0.98) = 1,998 individuals will have a positive result. This means 96 + 1,998 = 2,094 is our final population of positive individuals.

We can calculate the costs for treating positive cases by multiplying the median cost for treating a positive case with the population of positive individuals $100,000 \times 2,094 = $209,400,000

To calculate the total cost of administering the test to 100,000 individuals we multiply it by cost of administering the test: $1,000 * 100,000 = $100,000,000.

The total first-year cost for treating 100,000 individuals is $100,000,000 + $209,400,000 = $309,400,000.
```

## Question 2

The probability of your organization receiving a Joint Commission inspection in any given month is .05. What is the probability that, after 24 months, you received exactly 2 inspections? What is the probability that, after 24 months, you received 2 or more inspections? What is the probability that your received fewer than 2 inspections? What is the expected number of inspections you should have received? What is the standard deviation?

## Christian's Response

```
For some of the problems, we're going to utilize the binomial distribution formula:
P(k) = (n choose k) * p^k * (1-p)^(n-k)


Probability you receive exactly 2 inspections:

P(2) = (24 choose 2) * 0.05^2 * (1 - 0.05)^(24 - 2)
= (24! / (2! * 22!)) * 0.05^2 * 0.95^22
= 0.2619
--------------------------------------------------------------------------------------------------------------------------------------------------------

Probability that after 24 months you received 2 or more inspections:

To calculate, we're going to first find the probability is that we receive 0 or 1 inspections and then subtract it from 1 to get the probability of receiving 2 or more inspections.

P(0) = (24 choose 0) * 0.05^0 * (1 - 0.05)^(24 - 0)
= 0.95^24

P(1) = (24 choose 1) * 0.05^1 * (1 - 0.05)^(24 - 1)
= 24 * 0.05 * 0.95^23

The probability is approximately 0.289

P(2 or more) = 1 - P(0) - P(1)
= 1 - 0.95^24 - 24 * 0.05 * 0.95^23
≈ 0.289
------------------------------------------------------------------------------------------------------------------------------------------------------

What is the probability that your received fewer than 2 inspections:

For this problem we're going to add the probability that we receive of receiving 0 and 1 inspections.

=0.95^24 + 24 * 0.05 * 0.95^23
=0.704

-------------------------------------------------------------------------------------------------------------------------------------------------------

Expected number of inspections you should have received:

We can find this by finding the mean of the binomial distribution:

$\mu$ = n*p

n is the number of trails and p is our success rate or chance of inspection.

24*0.05
= 1.2

The expected number of inspections in 24 hours is 1.2.

--------------------------------------------------------------------------------------------------------------------------------------------------------

The standard deviation of the number of inspections in 24 months:

We're going to use this formula to reach this number:

$\sigma$ = sqrt(n*p*(1-p))


Upon plugging in the numbers, we reach our answer:

$\sigma$ = sqrt(24*0.05*(1-0.05))
= 1.08
```

## Question 3

You are modeling the family practice clinic and notice that patients arrive at a rate of 10 per hour. What is the probability that exactly 3 arrive in one hour? What is the probability that more than 10 arrive in one hour?

How many would you expect to arrive in 8 hours? What is the standard deviation of the appropriate probability distribution? If there are three family practice providers that can see 24 templated patients each day, what is the percent utilization and what are your recommendations?

### Christian's Response

```
Probability of exactly 3 patients arriving in one hour:

We're going to use the Poisson probability mass function to solve the problem
P(X = k) = (e^(-$\lambda$) $\times$ $\lambda$^k) / k!

After plugging in the numbers, we find the probability of 3 patients arriving is 0.8%
P(X=3) = (e^(-10) * 10^3) / 3!
= 0.008


-----------------------------------------------------------------------------------------------------------------------

Probability of more than 10 patients arriving in one hour:
We can utilize the Poisson cumulative distribution function to calculate this.

P(X > 10) = 1 - P(X ≤ 10)

We arrive to our answer. The probability of more than 10 patients arriving in one hour is 2.2%
= 1 - $\Sigma$(i=0 to 10) [ (e^(-10) * 10^i) / i! ]
≈ 0.022

------------------------------------------------------------------------------------------------------------------------

Number of patients expected to arrive in 8 hours:
We calculate this number in a simple product problem. We multiply the avg arrival rate by the amount of hours:

Expected number of patients = 10 * 8 = 80

-----------------------------------------------------------------------------------------------------------------------

Standard deviation of the appropriate probability distribution:
We can find the standard deviation of a Poisson distribution by finding the square root of its rate parameter.
σ = sqrt(10) = 3.16

-----------------------------------------------------------------------------------------------------------------------

Percent Utilization and recommendations

To get the utilization we're going to divide the expected number of patients per day by the maximum number of patients they can receive:

80/72 * 100% = 111.1%

This number tell us we are over capacity. Some recommendations would be to add additional providers or have a priority patient system, where they make sure the most urgent cases are seen first.
```

## Question 4

Your subordinate with 30 supervisors was recently accused of favoring nurses. 15 of the subordinate’s workers are nurses and 15 are other than nurses. As evidence of malfeasance, the accuser stated that there were 6 company-paid trips to Disney World for which everyone was eligible.

The supervisor sent 5 nurses and 1 non-nurse. If your subordinate acted innocently, what was the probability he/she would have selected five nurses for the trips? How many nurses would we have expected your subordinate to send? How many non-nurses would we have expected your subordinate to send.

### Christian's Response

```
To solve this we're going to use the hypergeometric distribution formula:

P(X = k) = (C(N1, k) * C(N2, n-k)) / C(N, n)



P(X = k) = probability of selecting k nurses
N1 = the number of nurses (15)
N2 = the number of non-nurses (15)
N = total number of workers (30)
n = the number of people selected for the Disney World trips (6)
k = the number of nurses selected for the trips (5)

When plugging in the numbers we discover that the probability that the subordinate innocently chose 5 nurses is 7.6%
P(X = 5) = (C(15, 5) * C(15, 1)) / C(30, 6)
= (3003 * 15) / 593775
= 0.076

-----------------------------------------------------------------------------------------------------------------------

Expected number of nurses and non-nurses we would've expected to be sent:

To find this I decided to find the proportion of nurses to total workers 15/30 = 50% is the ratio of Nurses to Total workers.

If we get 50% of the 6 that were sent on the trip, we get 3. Since it's evenly split, we would expect there to be an
even division of nurses (3) and non-nurse (3) staff sent on the tip.
```

## Question 5

The probability of being seriously injured in a car crash in an unspecified location is about .1% per hour. A driver is required to traverse this area for 1200 hours in the course of a year. What is the probability that the driver will be seriously injured during the course of the year? In the course of 15 months? What is the expected number of hours that a driver will drive before being seriously injured?

Given that a driver has driven 1200 hours, what is the probability that he or she will be injured in the next 100 hours?

### Christian's Response

```
The probability a driver will be injured during the course of a year:

First we calculate the the probability that a driver won't be injured in a car accident.

1 - 0.001 = 0.999

Then we use that number to calculate the percent of not being injured for the year. 

0.999^1200 = 0.8187

Lastly we subtract this number by 1 to get the percentage of being serious injured for the year.
1 - 0.8187 = %18.13
----------------------------------------------------------------------------------------------------------------------------------

The probability a driver will be injured in the course of 15 months:

We take the same approach as above to find this number

First we calculate the the probability that a driver won't be injured in a car accident.

1 - 0.1 = 0.999

Then we use that number to calculate the percent of not being injured for the year. 

0.999^1500 = 0.7988

Lastly we subtract this number by 1 to get the percentage of being serious injured during the course of 15 months.
1 - 0.7988 = %20.12

--------------------------------------------------------------------------------------------------------------------------------

Expected number of hours that a driver will drive before being seriously injured? 

We expect a driver to get seriously hurt within 1000 hours
1/0.0001 (prob of getting injured) = 1000 hours
--------------------------------------------------------------------------------------------------------------------------------

A driver has driven 1200 hours, what is the probability that he or she will be injured in the 
next 100 hours:

Using the Poisson distribution, we can plug in the our variables to solve for this

P(X = 1) = ($\lambda$^k * e^$\lambda$) / k! 

First we calculate lambda

lambda = (0.1% per hour) * (100 hours) = 0.1

Then we plug it in our equation. We find out that the probability is 9.05%

P(X = 1) = (0.1^1 * e^-0.1) / 1! = 0.0905
```

## Question 6

You are working in a hospital that is running off of a primary generator which fails about once in 1000 hours. What is the probability that the generator will fail more than twice in 1000 hours? What is the expected value?

### Christian's Response

```
```{r}
print((1 - (pbinom (2, size = 1000, prob = 0.001))))
```

Using this calculation, we can see that the expected value is around 0.001.

## Question 7

A surgical patient arrives for surgery precisely at a given time. Based on previous analysis (or a lack of knowledge assumption), you know that the waiting time is uniformly distributed from 0 to 30 minutes.

What is the probability that this patient will wait more than 10 minutes? If the patient has already waited 10 minutes, what is the probability that he/she will wait at least another 5 minutes prior to being seen? What is the expected waiting time?

### Christian's Response

```
Probability that the patient will wait more than 10 minutes:
= (30 - 10) * 1/30 = 2/3 = 67%

-------------------------------------------------------------------------------------------------------------

Probability that the patient will wait at least another 5 minutes given that they have already waited for 10 minutes
= (20 - 5) * 1/20 = 3/4 = 75%

-------------------------------------------------------------------------------------------------------------

What is the expected waiting time:
= (30 + 0) / 2 = 15 minutes
```

## Question 8

Your hospital owns an old MRI, which has a manufacturer’s lifetime of about 10 years (expected value). Based on previous studies, we know that the failure of most MRIs obeys an exponential distribution.

What is the expected failure time? What is the standard deviation? What is the probability that your MRI will fail after 8 years? Now assume that you have owned the machine for 8 years. Given that you already owned the machine 8 years, what is the probability that it will fail in the next two years?

### Christian's Response

```
Failure time & Standard Deviation:
The expected failure time and standard deviation is found by finding the reciprocal of the lambda parameter
=  1/lambda = 1/0.1 = 10 years

------------------------------------------------------------------------------------------------------------------
Probability of failure after 8 years:

```{r}
round((1-pexp(8, 0.1)), 4)
```

------------------------------------------------------------

Probability of failure after in the next 2 years:

```{r}
round(pexp(2, 0.1), 4)
```
