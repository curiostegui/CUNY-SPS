# Assignment 1

## Problem

One of the most useful applications for linear algebra in data science is image manipulation. We often need to compress, expand, warp, skew, etc. images. To do so, we left multiply a transformation matrix by each of the point vectors.

For this assignment, build the first letters for both your first and last name using point plots in R. For example, the following code builds an H.

x=c(rep(0,500),seq(0,1,length.out=1000), rep(1,500))

y=c(seq(-1,1,length.out=500),rep(0,1000), seq(-1,1,length.out=500))

z=rbind(x,y)

plot(y\~x, xlim=c(-3,3), ylim=c(-3,3))

Then, write R code that will left multiply (%\>%) a square matrix (x) against each of the vectors of points (y). Initially, that square matrix will be the Identity matrix.

Use a loop that changes the transformation matrix incrementally to demonstrate 1) shear, 2) scaling, 3) rotation , and 4) projection in animated fashion.

Hint: Use x11() to open a new plotting window in R.

Upload your document as a .RMD file. I will know if your assignment is correct if the animation runs. correctly

```
```{r message=FALSE}
library(dplyr)
library(plotly)
library(gifski)
library(gganimate)
```

## Create letter CU

```{r}
#letter CU
x=c(seq(-1, -2, length.out = 800), rep(-2, 800), seq(-2, -1, length.out = 800), rep(0, 800), seq(0,1, length.out = 800), rep(1, 800))
y=c(rep(1,800), seq(1, -1, length.out = 800), rep(-1, 800), seq(1,-1, length.out = 800), rep(-1, 800), seq(-1, 1, length.out = 800))
z=rbind(x,y)
plot(y~x, xlim=c(-3,3), ylim=c(-3,3), col='grey')
```

## Create function that will left multiply

```{r create function}
leftMultiply  <- function(x,y){
   x %*% y
}
leftMultiply(matrix(rep(seq(1,3, length.out=3),3), nrow = 3, ncol = 3),diag(3))
```

## Shear

```{r, animation.hook='gifski',interval=0.2,fig.width=4}
for (i in seq(0,1,length.out=20)) {
   z1<-apply(z,2,function(x) leftMultiply(x,matrix(c(1,i,0,1),nrow=2,ncol=2)))
    plot(z1[2,]~z1[1,], xlim=c(-3,3), ylim=c(-3,3), col='grey')
}
```

## Scaling

```{r, animation.hook='gifski',interval=0.3,fig.width=4}
for (i in seq(1,4,length.out=20)) {
  z1<-apply(z,2,function(x) leftMultiply(x,matrix(c(i,0,0,i),nrow=2,ncol=2)))
   plot(z1[2,]~z1[1,], xlim=c(-3,3), ylim=c(-3,3), col='grey')
}
```

## Rotation

```{r, animation.hook='gifski',interval=0.3,fig.width=4}
for (i in seq(0,pi*2,length.out=20)) {
  z1<-apply(z,2,function(x) leftMultiply(x,matrix(c(cos(i),sin(i),-sin(i),cos(i)),nrow=2,ncol=2)))
   plot(z1[2,]~z1[1,], xlim=c(-3,3), ylim=c(-3,3), col='grey')
}
```

## Projection

```{r, animation.hook='gifski',interval=0.3,fig.width=4}
for (i in seq(0,2*pi,length.out=20)) {
  tempZ<-rbind(z,rep(0,ncol(z)))
  z1<-apply(tempZ,2,function(x) leftMultiply(x,matrix(c(1,0,0,0,cos(i),-sin(i),0,sin(i),cos(i)),nrow=3,ncol=3)))
   plot(z1[2,]~z1[1,], xlim=c(-3,3), ylim=c(-3,3), col='grey')
} 
```
