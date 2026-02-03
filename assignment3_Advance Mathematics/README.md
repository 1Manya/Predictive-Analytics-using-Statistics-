# PDF Parameter Estimation

## Objective
The objective of this experiment is to estimate the parameters of a given probability density function using the transformed variable z.
using r= 102317119 for step 1 
## Given Function
The probability density function considered in this experiment is:

p(z) = c * exp( -lambda * (z - mu)^2 )

where mu, lambda, and c are the parameters to be estimated.
## Methodology
The transformed data z obtained from the previous step is used for estimating the parameters. Since the given function follows a Gaussian-type shape, simple statistical methods are sufficient.

First, the mean of z is calculated and taken as the value of mu. This represents the central value of the data. After that, the variance of z is calculated to measure how much the data is spread around the mean.

Using the variance, the value of lambda is computed using the relation:
lambda = 1 / (2 * variance)

Finally, the value of constant c is calculated to properly scale the probability density function.

## Result
Using the above method, the parameters mu, lambda, and c were obtained for the given probability density function.
mu: 25.812999155899675
variance: 342.236959009029
lambda: 0.001460976048430844
c: 0.02156485844361762
## Tools Used
Python and NumPy 
