Probability Density Function Parameter Estimation
Objective

To estimate the parameters of a given probability density function using the transformed variable obtained from the previous step.

Given PDF

The probability density function used in this experiment is:

𝑝
^
(
𝑧
)
=
𝑐
 
𝑒
−
𝜆
(
𝑧
−
𝜇
)
2
p
^
	​

(z)=ce
−λ(z−μ)
2

where 
𝜇
μ, 
𝜆
λ, and 
𝑐
c are the parameters to be estimated.

Method Used

The parameters are estimated using simple statistical estimation techniques. Since the given function has a Gaussian-like form, its parameters can be calculated directly from the data.

The mean of the transformed variable 
𝑧
z is calculated and taken as 
𝜇
μ. The variance of 
𝑧
z is then computed to find how the values are spread around the mean.

Using the variance, the value of 
𝜆
λ is calculated as:

𝜆
=
1
2
×
variance
λ=
2×variance
1
	​


After that, the constant 
𝑐
c is calculated using:

𝑐
=
𝜆
𝜋
c=
π
λ
	​

	​

Result

Using the above method, the values of 
𝜇
μ, 
𝜆
λ, and 
𝑐
c were obtained and represent the learned parameters of the given probability density function.

Tools Used

Python

NumPy
