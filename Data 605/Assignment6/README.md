# Assignment 6

## Question 1

A bag contains 5 green and 7 red jellybeans. How many ways can 5 jellybeans be withdrawn from the bag so that the number of green ones withdrawn will be less than 2?

### Christian's Response:

We can solve this problem by first creating a vector with the Jellybeans we have: 5 green and 7 red. Then we calculate the different combination of 5 Jellybeans from our total of 12. Afterwards, we filter specifically for all cases where there is an instance where less than 2 green jellybeans were taken and sum those instances.


```{r}
# create vector of the jellybeans
jellybeans <- c(rep("G", 5), rep("R", 7))

# calculate for all combinations of 5 jellybeans
all_combinations <- combn(jellybeans, 5)

# check number of possible combinations 
dim(all_combinations)[2]
```


```{r}
# filter for combinations of where jellybeans < 2
green_less_than_2 <- apply(all_combinations, 2, function(x) sum(x == "G") < 2)

sum(green_less_than_2)
```


There are 196 possibilities when withdrawing 5 Jellybeans, that we will have less than 2 number of green jellybeans

## Question 2

A certain congressional committee consists of 14 senators and 13 representatives. How many ways can a subcommittee of 5 be formed if at least 4 of the members must be representatives?

### Christian's Response:

To solve this problem, we want to calculate the different subcommittees that can be created given our constrain of having at least 4 representatives in a subcommittee of 5.

There are only two combinations, a subcommittee that is comprised of all representatives and another comprised of 4 representatives and 1 senator. I elected to use the \*choose\* function because it can apply the binomial coefficient formula to get us the answers we need.

After calculating the different combinations for these two scenarios, we can add them to find the ways a subcommittee of 5 can be formed with at least 4 representatives.

```{r}
# calculates ways we can create a subcommittee of 5 representatives
subcomm_5_reps <- choose(13,5)
```

```{r}
# calculates ways we can create a subcommittee of 4 representatives w/ 1 senator
subcomm_4_reps <- choose(13,4) * choose(14,1)
```

```{r}
# calculates ways a subcommittee of 5 can be formed with at least 4 representatives
total <- subcomm_5_reps + subcomm_4_reps
print(total)
```
Our output gives us: 11297

## Question 3

If a coin is tossed 5 times, and then a standard six-sided die is rolled 2 times, and finally a group of three cards are drawn from a standard deck of 52 cards without replacement, how many different outcomes are possible?

### Christian's Response:

To solve this problem we have to solve for the possible outcomes for each case individually and then multiply them together:

1\. Coin toss: We know that a coin has two outcomes, heads or tails, and we are tossing 5 times. We can represent this in the following code

```{r}
# outcomes for a coin tossed 5 times
coin <- 2^5
cat("The total number of outcomes when a coin is tossed 5 times is",coin)
```

2\. Dice rolls: A dice has six outcomes and we are rolling it 2 times. We can represent this in the following code

```{r}
# outcomes for a dice rolled 2 times
dice <- 6^2
cat("The total number of outcomes when a dice is rolled 2 times is",dice)
```

3\. Card drawing: A deck contains 52 cards and we are drawing three cards without replacement. We can represent this in the following code

```{r} 
card <- choose(52,3)
cat("The total number of outcomes when a card is drawn three times without replacement",card)
```

\`\`\`

Finally, we can arrive to our answer by multiplying all three outcomes together

```{r}
answer <- coin*dice*card
cat("The total number outcomes all together is",answer)
```

## Question 4

3 cards are drawn from a standard deck without replacement. What is the probability that at least one of the cards drawn is a 3? Express your answer as a fraction or a decimal number rounded to four decimal places.

### Christian's Answer

The probability of drawing a a 3 from a standard deck of 52 cards is 4/52 - since there are 4 types of cards (clubs, spades, diamonds and hearts). To find the probability of drawing at least in one 3 in three draws without replacement, we can subtract 1 by the possibility of drawing a non 3 card in each draw without replacement. The result will give us then the probability of drawing at least one 3 in three draws without replacement.

```{r}
prob_card <- 1 - (48/52) * (47/51) * (46/50) 
prob_card <- round(prob_card,4)
cat("The answer is",prob_card)
```

## Question 5

Lorenzo is picking out some movies to rent, and he is primarily interested in documentaries and mysteries. He has narrowed down his selections to 17 documentaries and 14 mysteries.

Step 1. How many different combinations of 5 movies can he rent?

### Christian's Answer

To look at the combinations of 5 movies he can rent, we have to apply the combinations formula between 31 (total number of movies he can choose to rent from) and 5 (the number he wants to rent).

```{r}
comb_5movies <- choose(31,5)
cat("The total combination of movies he can rent is", comb_5movies)
```
Step 2. How many different combinations of 5 movies can he rent if he wants at least one mystery

### Christian's Answer:

We can subtract the combination of 5 movies that consists of all documentaries from the total combination of 5 movies we can choose from to get our result.

```{r}
# combination of choosing 5 documentary films
doc_comb <- choose(17,5)

# subtract total combination of 5 movies from combination of choosing all documentaries
myst_comb <- comb_5movies - doc_comb

cat("Our total combination of 5 movies with atleast 1 mystery is", myst_comb)
```

## Question 6

In choosing what music to play at a charity fund raising event, Cory needs to have an equal number of symphonies from Brahms, Haydn, and Mendelssohn. If he is setting up a schedule of the 9 symphonies to be played, and he has 4 Brahms, 104 Haydn, and 17

Mendelssohn symphonies from which to choose, how many different schedules are possible? Express your answer in scientific notation rounding to the hundredths place.

### Christian's Response:

Since Cory needs an equal number of symphonies, we simply look at the possibilities of picking 3 music works from each composer and multiply them to get our answer.

```{r}
# multiplies the different combinations of symphonies from Brahms Haydn and Mendelssohn
symph_comb <- factorial(9)* choose(4,3)*choose(104,3)*choose(17,3)

# format answer to scientific notation
symph_comb <- format(symph_comb, scientific = TRUE, digits = 2)

cat("The total amount of schedules he can create is",symph_comb)
```

## Question 7

An English teacher needs to pick 13 books to put on his reading list for the next school year, and he needs to plan the order in which they should be read. He has narrowed down his choices to 6 novels, 6 plays, 7 poetry books, and 5 nonfiction books.

Step 1. If he wants to include no more than 4 nonfiction books, how many different reading schedules are possible? Express your answer in scientific notation rounding to the hundredths place.

### Christian's Response

First, we want to look at what the number of combinations would be when having 0 nonfiction books all the way up to 4 nonfiction books.

If we have 0 non fiction books, that means that his choice of 13 books will only include 19 books(6 novels, 6 plays, 7 poetry books). We set up our problem as c(5,0)\*c()19,13. We then repeat this for every subsequent combination of nonfiction books.

After solving for this and storing them in objects, we then multiply each combination with 13! and then add them together to get our answer.

```{r}
# find combinations for every arrangement of nonfiction books up to 4
no_nonfiction <- choose(5,0)*choose(19,13)
one_nonfiction <- choose(5,1)*choose(19,12)
two_nonfiction <- choose(5,2)*choose(19,11)
three_nonfiction <- choose(5,3)*choose(19,10)
four_nonfiction <- choose(5,4)*choose(19,9)
```

```
# Calculate the final total combinations
Totals <- factorial(13)*no_nonfiction+factorial(13)*one_nonfiction+factorial(13)*two_nonfiction+factorial(13)*three_nonfiction+factorial(13)*four_nonfiction

# Round to 4 digits
Totals<- round(Totals,4)

cat("The different amount of schedules that can be created is",Totals)
```

Step 2. If he wants to include all 6 plays, how many different reading schedules are possible? Express your answer in scientific notation rounding to the hundredths place.

### Christian's Response:

Since the teacher already selected all 6 plays, this leaves him with 7 remaining choices - since he wants to pick 13 books. This also leaves us with 18 remaining books that he can choose (6 novels + 7 poetry + 5 nonfiction).We then multiply the result by the combination of 6 plays C(6,6) and then the factorial of 13 to show the different ways we can arrange the selection.

```{r}
book_sched <- choose(18,7)*choose(6,6)*factorial(13)

format(book_sched, scientific = TRUE, digits = 2)

cat("The number of reading schedules is",book_sched)
```

## Question 8

Zane is planting trees along his driveway, and he has 5 sycamores and 5 cypress trees to plant in one row. What is the probability that he randomly plants the trees so that all 5 sycamores are next to each other and all 5 cypress trees are next to each other? Express your answer as a fraction or a decimal number rounded to four decimal places.

### Christian's Response

```{r}
# Arrangement of sycamores and cypress trees individually times the 2 ways they can be combined
syca_cyp <- 2*factorial(5)*factorial(5)

# Arrangement of all trees 
all_trees <- factorial(10)

# prob all are next to each other
prob_trees <- syca_cyp/all_trees
```

## Question 9

If you draw a queen or lower from a standard deck of cards, I will pay you \$4. If not, you pay me \$16. (Aces are considered the highest card in the deck.)

Step 1. Find the expected value of the proposition. Round your answer to two decimal places. Losses must be expressed as negative values

### Christian's Response

Looking at our condition, we have a total of 44 cards we can choose from, including: 4 queens, 4 jacks, and 32 cards from 2 to 10 (Diamonds, Hearts, Spades, Clubs).

The probability of choosing a card of queen or lower is therefore = 44/52 = 11/13

The probability of choosing anything higher is 8/52 = 2/13

We can then multiply each probability by the expected earning in either scenario and then subtract the result to get our how many we would expected to win or lose.

```{r}
expected_value <- (11/13*4)-(2/13*16)
expected_value <- round(expected_value,2)
cat("The expected value of the proposition is",expected_value)
```
Step 2. If you played this game 833 times how much would you expect to win or lose? Round your answer to two decimal places. Losses must be expressed as negative values.

### Christian's Response

We can multiply the expected_value of the proposition by the number of games played to calculate our earnings.

```{r}
Gains_833 <- expected_value * 833
print(Gains_833)
```
