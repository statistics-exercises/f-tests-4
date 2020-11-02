# Plotting the f-distribution

Hopefully, the last exercise convinced you that the test statistic we have been using:

![](https://render.githubusercontent.com/render/math?math=F=\frac{\left(\frac{S_1^2}{\sigma_1^2}\right)}{\left(\frac{S_2^2}{\sigma_2^2}\right)}=\frac{1}{\lambda_0}\frac{S_1^2}{S_2^2})

is not a sample from a normal distribution.  This should have been obvious, however.  The numerator and denominator in the quotient above are both positive and hence F must be positive.   It thus cannot possibly be a sample from a normal distribution as we know there is a finite probability of generating any real number if we sample from a normal random variable.

The distribution that is being sampled from here is the f-distribution.  This distribution is a function of two parameters ![](https://render.githubusercontent.com/render/math?math=v_1) and ![](https://render.githubusercontent.com/render/math?math=v_2) which are known as the numbers of degrees of freedom.  ![](https://render.githubusercontent.com/render/math?math=v_1) is equal to ![](https://render.githubusercontent.com/render/math?math=N_1-1) and ![](https://render.githubusercontent.com/render/math?math=v_2) is equal to ![](https://render.githubusercontent.com/render/math?math=N_2-1), where ![](https://render.githubusercontent.com/render/math?math=N_1) and ![](https://render.githubusercontent.com/render/math?math=N_2) are the numbers of random variables used to calculate sample variances in the numerator and denominator of the expression above.  Obviously, ![](https://render.githubusercontent.com/render/math?math=v_1) and ![](https://render.githubusercontent.com/render/math?math=v_2) must both be positive integers.

With that in mind, __your task here is to plot the probability density function for the f-distribution with (4,5) degrees of freedom__.  Notice that you can extract the value of the cumulative distribution function at x for the t-distribution with `(v1,v2)` degrees of freedom using the python command:

````
y = scipy.stats.f.cdf( x, v1, v2 )
````

To get the inverse of the cumulative distribution at `y` you use the following command:

````
x = scipy.stats.f.ppf( x, v1, v2 )
````

and lastly to get the probability density function for this random variable at `x` you use: 

````
p = scipy.stats.f.pdf( x, v1, v2 )
````
