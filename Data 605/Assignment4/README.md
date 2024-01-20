# Assignment 4

## Instructions

With the attached data file (images used in study below), build and visualize eigenimagery that accounts for 80% of the variability. Provide full R code and discussion.

## Introduction to Eigenimagery

Eigenimages are images analyzed and reduced to eigenvectors. This image is created through Principal Component Analysis, a technique that relies on linear transformation, transforming multi-dimensional data into a coordinate plot.

```
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)

#BiocManager::install("EBImage")
#install.packages("magick")
#install.packages("jpeg")
#install.packages("OpenImageR")
#install.packages("xfun")

library(xfun)
library(EBImage)
library(magick)
library(jpeg)
library(OpenImageR)
```

### Load Images 

```{r}
num=17
files=list.files("C:/Users/urios/OneDrive/Documents/jpg/",pattern="\\.jpg")[1:num] 
print(files)
```

### Create Function that Reads File

```{r}
height=1200; width=2500;scale=20
plot_jpeg = function(path, add=FALSE)
{ jpg = readJPEG(path, native=T) # read the file
  res = dim(jpg)[2:1] # get the resolution, [x, y]
  if (!add) # initialize an empty plot area if add==FALSE
    plot(1,1,xlim=c(1,res[1]),ylim=c(1,res[2]),asp=1,type='n',xaxs='i',yaxs='i',xaxt='n',yaxt='n',xlab='',ylab='',bty='n')
  rasterImage(jpg,1,1,res[1],res[2])
}

```

### Put Data into an Array

```{r}
im=array(rep(0,length(files)*height/scale*width/scale*3), dim=c(length(files), height/scale, width/scale,3))

for (i in 1:17){
  temp=resize(readJPEG(paste0("C:/Users/urios/OneDrive/Documents/jpg/", files[i])),height/scale, width/scale)
  im[i,,,]=array(temp,dim=c(1, height/scale, width/scale,3))}

```

### Vectorize

```{r, results='hide'}
flat=matrix(0, 17, prod(dim(im))) 
for (i in 1:17) {
  print(files[i])
  newim <- readJPEG(paste0("C:/Users/urios/OneDrive/Documents/jpg/", files[i]))
  r=as.vector(im[i,,,1]); g=as.vector(im[i,,,2]);b=as.vector(im[i,,,3])
  flat[i,] <- t(c(r, g, b))
}
shoes=as.data.frame(t(flat))
```

### Actual Plots

```{r}
par(mfrow=c(3,3))
par(mai=c(.3,.3,.3,.3))
for (i in 1:17){  #plot the first images only
plot_jpeg(writeJPEG(im[i,,,]))
}

```

### Eigencomponents from Correlation Structure
 
```{r}
scaled=scale(shoes, center = TRUE, scale = TRUE)
mean.shoe=attr(scaled, "scaled:center") #saving for classification
std.shoe=attr(scaled, "scaled:scale")  #saving for classification...later

```

### Calculate Covariance (Correlation)

```{r}
Sigma_=cor(scaled)
```

### Get the Eigencomponents

```{r}
myeigen=eigen(Sigma_)
cumsum(myeigen$values) / sum(myeigen$values)
```

### Eigenshoes

```{r}
scaling=diag(myeigen$values[1:5]^(-1/2)) / (sqrt(nrow(scaled)-1))
eigenshoes=scaled%*%myeigen$vectors[,1:5]%*%scaling
par(mfrow=c(2,3))
imageShow(array(eigenshoes[,1], c(60,125,3)))
```

### Generate Principal Components

```{r}
height=1200
width=2500
scale=20
newdata=im
dim(newdata)=c(length(files),height*width*3/scale^2)
mypca=princomp(t(as.matrix(newdata)), scores=TRUE, cor=TRUE)
```

### Eigenshoes

```{r}
mypca2=t(mypca$scores)
dim(mypca2)=c(length(files),height/scale,width/scale,3)
par(mfrow=c(5,5))
par(mai=c(.001,.001,.001,.001))
for (i in 1:17){#plot the first 25 Eigenshoes only
plot_jpeg(writeJPEG(mypca2[i,,,], bg="white"))  #complete without reduction
}
```

### Variance

```{r}
a=round(mypca$sdev[1:17]^2/ sum(mypca$sdev^2),3)
cumsum(a)
```

### New Data Sets

```{r}
x = t(t(eigenshoes)%*%scaled)
print(x)

dim(eigenshoes)
```
```

