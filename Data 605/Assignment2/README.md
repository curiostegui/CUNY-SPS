
# Assignment 2

## Problem Set 1

(1) Show that \$A\^TA\$ does not equal \$AA\^T\$. (Proof and demonstration)

### Christian's Response:

When calculating for the transpose of a Matrix, if we have matrix \$A\$, then the transpose \$A\^T\$ will contain the rows of \$A\$ as columns. In the matrix created below, we can see that despite \$A\^TA\$ and \$AA\^T\$ having the same dimensions, they don't have the same elements located in the same exact position as the other.

```
```{r}
set.seed(62) # set seed so we can recreate this sample matrix

A <- matrix(sample(1:25, 16, replace = FALSE), ncol = 4) #creates random 4x4 matrix
AT <- t(A) # calculate transpose of A

AT %*% A == A %*% AT # compare product of both matrices
```

(2) For a special type of square matrix A, we get $A\^TA = AA\^T$. Under what conditions could this be true? (Hint: The Identity matrix I is an example of such a matrix).

### Christian's Response:

In most cases, $A\^TA \\ne AA\^T$. A symmetric matrix however is the exception to this. When inverted, a symmetric matrix produces an identical pattern of elements as it's non-inverted counterpart. When multiplying A with $A\^T$ or $A\^T$ and $A$, both products give the same results.

```
{r}
B <- matrix(c(-6,2,9,2,3,1,9,1,-4),nrow=3) # create a symmetric matrix
BT <- t(B) # calculate transpose of B

BT %*% B == B %*% BT # compare product results
```

## Problem Set 2

Matrix factorization is a very important problem. There are supercomputers built just to do matrix factorizations. Every second you are on an airplane, matrices are being factorized. Radars that track flights use a technique called Kalman filtering. At the heart of Kalman Filtering is a Matrix Factorization operation. Kalman Filters are solving linear systems of equations when they track your flight using radars.

Write an R function to factorize a square matrix A into LU or LDU, whichever you prefer. Please submit your response in an R Markdown document using our class naming convention, E.g. LFulton_Assignment2_PS2.png You don’t have to worry about permuting rows of A and you can assume that A is less than 5x5, if you need to hard-code any variables in your code. If you are doing the entire assignment in R, then please submit only one markdown document for both problems.

### Christian's Response:

In the creation of a function that could perform LU decomposition, I utilized gaussian elimination as a method of row reduction when creating $L$ and $U$ from matrix $A$ (named $C$ in this example). I also included a for loop which would iterate on the rows and columns that I was interested in changing.

```
{r}
C <- matrix(c(5,2,9,2,3,1,9,1,4),nrow=3) # create matrix we will perform LU Decomposition on

print(C)
{r}
LU_decomp <- function(m) {
  N <- nrow(m) # store the number of rows
  L <- diag(N) # used diag function to create our L variable
  U <- m  
  
  for (j in 1:(N-1)){         # looks at columns of interest
    for(i in (j+1):N){        # looks at rows of interest
        if(U[i,j]==0){
        next
        }
        else{
        k <- -(U[i,j] / U[j,j])         # perform gaussian elimantion
        U[i, ] <- k * U[j ,] + U[i, ]
        L[i, j] <- -k
        }
    }
  }
  print(L%*%U) # print results of L muultiplied by U
}
We can see that , the result from , produces a matrix identical to C
{r}
P <- LU_decomp(C)
We confirm this using the  function
{r}
all.equal(C,P)
```
