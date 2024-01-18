# Assignment 3

## Problem Set 1

```
(1) What is the rank of the matrix A?
\[
A=
  \left[ {\begin{array}{cc}
    1 & 2 & 3 & 4 \\
    -1 & 0 & 1 & 3 \\
    0 & 1 & -2 & 1 \\
    5 & 4 & -2 & -3 \\
  \end{array} } \right]
\]
```

### Christian's Response:

Below I will be transforming the matrix into Row Echelon Form.

```
Operation 1: We perform $R_2+1R_1$

\[ \left[ {\begin{array}{cc}
    1 & 2 & 3 & 4 \\
    -1 & 0 & 1 & 3 \\
    0 & 1 & -2 & 1 \\
    5 & 4 & -2 & -3 \\
  \end{array} } \right]
\rightarrow
\left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 2 & 4 & 7 \\
  0 & 1 & -2 & 1 \\
  5 & 4 & -2 & -3 \\
\end{array} \right]
\]

*Operation 2:* We perform $R_4-5R_1$

\[ \left[ \begin{array}{cc}
   1 & 2 & 3 & 4 \\
   0 & 2 & 4 & 7 \\
   0 & 1 & -2 & 1 \\
   5 & 4 & -2 & -3 \\
\end{array} \right]
\rightarrow
\left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 2 & 4 & 7 \\
  0 & 1 & -2 & 1 \\
  0 & -6 & -17 & -23 \\
\end{array} \right]
\]

*Operation 3:* We perform $R_2*1/2$

\[ \left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 2 & 4 & 7 \\
  0 & 1 & -2 & 1 \\
  0 & -6 & -17 & -23 \\
\end{array} \right]
\rightarrow
\left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 1 & -2 & 1 \\
  0 & -6 & -17 & -23 \\
\end{array} \right]
\]

*Operation 4:* We perform $R_3-1R_2$

\[ \left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 1 & -2 & 1 \\
  0 & -6 & -17 & -23 \\
\end{array} \right]
\rightarrow
\left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 0 & -4 & -5/2 \\
  0 & -6 & -17 & -23 \\
\end{array} \right]
\]

*Operation 5:* We perform $R_4+6R_2$

\[ \left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 0 & -4 & -5/2 \\
  0 & -6 & -17 & -23 \\
\end{array} \right]
\rightarrow
\left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 0 & -4 & -5/2 \\
  0 & 0 & -5 & -2 \\
\end{array} \right]
\]

*Operation 6:* We perform $R_3*-1/4$

\[ \left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 0 & -4 & -5/2 \\
  0 & 0 & -5 & -2 \\
\end{array} \right]
\rightarrow
\left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 0 & 1 & 5/8 \\
  0 & 0 & -5 & -2 \\
\end{array} \right]
\]
```

```
*Operation 7:* We perform $R_4+5R_3$

\[ \left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 0 & 1 & 5/8 \\
  0 & 0 & -5 & -2 \\
\end{array} \right]
\rightarrow
\left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 0 & 1 & 5/8 \\
  0 & 0 & 0 & 9/8 \\
\end{array} \right]
\]

*Operation 8:* We perform $R_4*8/9$

\[ \left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 0 & 1 & 5/8 \\
  0 & 0 & -5 & -2 \\
\end{array} \right]
\rightarrow
\left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 0 & 1 & 5/8 \\
  0 & 0 & 0 & 9/8 \\
\end{array} \right]
\]


The last step is to count the amount of non-zeros in each row. In the final matrix, we can see that there are 4. The rank therefore is 4.

\[ 
\left[ \begin{array}{cc}
  1 & 2 & 3 & 4 \\
  0 & 1 & 2 & 7/2 \\
  0 & 0 & 1 & 5/8 \\
  0 & 0 & 0 & 9/8 \\
\end{array} \right]
\]

We can also solve this problem using the function *rankMatrix()*

#### Solving With R


{r}
B <- matrix(c(1,-1,0,5,2,0,1,4,3,1,-2,-2,4,3,1,-3),nrow=4)
B
rankMatrix(B)[1] #this confirms matrix B has a rank of 4


```

```
(2) Given an mxn matrix where m>n, what can be the maximum rank? The minimum rank, assuming that the matrix is non-zero?
```

### Christian's Response:

Given a matrix where m\>n, the maximum rank can't be greater than the smallest dimension - either the row or column. The minimum rank, assuming the matrix is non-zero, is a 1.

```
(3) What is the rank of matrix B?
\[
B=
  \left[ {\begin{array}{cc}
    1 & 2 & 1 \\
    3 & 6 & 3 \\
    2 & 4 & 2 \\
  \end{array} } \right]
\]
```

### Christian's Response:

Below I will be transforming the matrix into Row Echelon Form.

```
*Operation 1:* We perform $R_2-3R_1$

\[ \left[ {\begin{array}{cc}
    1 & 2 & 1 \\
    3 & 6 & 3 \\
    2 & 4 & 2 \\
  \end{array} } \right]
\rightarrow
\left[ \begin{array}{cc}
  1 & 2 & 1 \\
  0 & 0 & 0 \\
  2 & 4 & 2 \\
\end{array} \right]
\]

*Operation 2:* We perform $R_3-2R_1$

\[ \left[ \begin{array}{cc}
  1 & 2 & 1 \\
  0 & 0 & 0 \\
  2 & 4 & 2 \\
\end{array} \right]
\rightarrow
\left[ \begin{array}{cc}
  1 & 2 & 1 \\
  0 & 0 & 0 \\
  0 & 0 & 0 \\
\end{array} \right]
\]

The last step is to count the amount of non-zeros in each row. In the final matrix, we can see that there is 1. The rank therefore is 1.

\[ \left[ \begin{array}{cc}
  1 & 2 & 1 \\
  0 & 0 & 0 \\
  0 & 0 & 0 \\
\end{array} \right]
\]
```

```
We can also solve this problem using the function *rankMatrix()*

## Solving With R

{r}
C <- matrix(c(1,3,2,2,6,4,1,3,2),nrow=3)
C
rankMatrix(C)[1] #this confirms matrix B has a rank of 1


--------------------------------------------------------------------------------------
```

## Problem Set 2

Compute the eigenvalues and eigenvectors of the matrix A. You'll need to show your work. You'll need to write out the characteristic polynomial and show your solution.

### Christian's Response:

```
\[
A=
  \left[ {\begin{array}{cc}
    1 & 2 & 3 \\
    0 & 4 & 5 \\
    0 & 0 & 6 \\
  \end{array} } \right]
\]

This is the formula for solving for the characteristic polynomials.

$det(A-\lambda\mathit{I}_n)$

Below we calculate the difference betweem $A$ and $\lambda$

\[ \left[ \begin{array}{cc}
  1 & 2 & 1 \\
  0 & 4 & 5 \\
  0 & 0 & 6 \\
\end{array} \right]
\rightarrow
\left[ \begin{array}{cc}
  \lambda & 0 & 0 \\
  0 & \lambda & 0 \\
  0 & 0 & \lambda \\
\end{array} \right]
\]

This is the end result 

\[
A=
  \left[ {\begin{array}{cc}
    1 & 2 & 3 \\
    0 & 4 & 5 \\
    0 & 0 & 6 \\
  \end{array} } \right]
\]


Once we further break it down, we arrive to this cubic polynomial equation

$\lambda^3-11\lambda^2+34\lambda-24$

We can then factorize it to:

$(\lambda-1)(x^2-10x+24)$

We then factorize this portion

$(x^2-10x+24) = (x-4)(x-6)$

The characteristic polynomials are as follows:

$\lambda^3-11\lambda^2+34\lambda-24 = (x-1)(x-4)(x-6)$

Our eigenvalues are:

$\lambda = 1, \lambda = 4, \lambda = 6$

---------------------------------------------

#### Calculate vectorspace


solve for $\lambda = 1$

\[ \left[ {\begin{array}{cc}
    1-1 & 2 & 3 \\
    0 & 4-1 & 5 \\
    0 & 0 & 6-1 \\
  \end{array} } \right]
\]

Result

\[
A=
  \left[ {\begin{array}{cc}
    0 & 2 & 3 \\
    0 & 3 & 5 \\
    0 & 0 & 5 \\
  \end{array} } \right]
\]

Let $x_1 = 1$

Next solve $x_2$ and $x_3$

$5x_3 = 0$

$3x_2 + 5x_3 = 0$

$x_2 = 0 x_3 =0$

Eigenvector for \lambda = 1

\[ \left[ {\begin{array}{cc}
    1 \\
    0 \\
    0 \\
  \end{array} } \right]
\]

-----------------------------------------------------

solve for $\lambda = 4$

\[ \left[ {\begin{array}{cc}
    1-4 & 2 & 3 \\
    0 & 4-4 & 5 \\
    0 & 0 & 6-4 \\
  \end{array} } \right]
\]

Result

\[
A=
  \left[ {\begin{array}{cc}
    -3 & 2 & 3 \\
    0 & 0 & 5 \\
    0 & 0 & 2 \\
  \end{array} } \right]
\]

Let $x_1 = 1$

$-3x_1 + 2x_2 + 3x_3 = 0$

Solve for $x_3$

$3x_3 = 0$

Solve for $x_2$

$-3 + 2x_2 = 0$

$x_2 = 3/2$

The eigenvector for $\lambda = 4$ is

\[ \left[ {\begin{array}{cc}
    1 \\
    3/2 \\
    0 \\
  \end{array} } \right]
\]

-----------------------------------------------------

solve for $\lambda = 6$

\[ \left[ {\begin{array}{cc}
    1-6 & 2 & 3 \\
    0 & 4-6 & 5 \\
    0 & 0 & 6-6 \\
  \end{array} } \right]
\]

Result

\[
A=
  \left[ {\begin{array}{cc}
    -5 & 2 & 3 \\
    0 & -2 & 5 \\
    0 & 0 & 0 \\
  \end{array} } \right]
\]

Let $x_2 = 1$

Solve for x_3

$-2x_2 + 5x_3 = 0 \: \rightarrow \: 2x_2 = 5x_3 \:\rightarrow \: x_3 = 2/5x_2$

Solve for x_2

$-5x_1 + 2x_2 + 3x_3 = 0 \: \rightarrow \: -5x_1 + 2x_2 + 3(2/5)x_2 = 0 \: \rightarrow \: -5x_1 + (16/5)x_2 = 0 \: \rightarrow \: 5x_1 = 16/5x_2 \: \rightarrow \: x_1 = 16/25x_2$ 

The eigenvector for $\lambda = 6$ is

\[ \left[ {\begin{array}{cc}
    16/25 \\
    1 \\
    2/5 \\
  \end{array} } \right]
\]

---------------------------------------------

## Results

To recap, our eigenvalues are:

$\lambda = 1 \:\:\: \lambda = 4 \:\:\: \lambda = 6$


Our eigenvectors are the following:

\[ \left[ {\begin{array}{cc}
    1 \\
    0 \\
    0 \\
  \end{array} } \right]
,
\left[ {\begin{array}{cc}
    1 \\
    3/2 \\
    0 \\
  \end{array} } \right]
,
\left[ {\begin{array}{cc}
    16/25 \\
    1 \\
    2/5 \\
  \end{array} } \right]
\]
```

