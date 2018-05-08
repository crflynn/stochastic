# 2DKS
2 Dimensional Kolmogorov-Smirnov test for goodness-of-fit.

## Hypothesis testing
A KS test is a non parametric way to test if some data fits with a certain probability distribution, 
or if two datasets were created with the same underlying probability distribution. 
*Note*: the test only rejects the hypothesis that the data fits with the probability distribution, or does not reject it
for a certain significance level. It cannot confirm, only 'not-reject'.

For now, only the two sample 2D KS test is implemented.

Prerequisites: scipy for the pearsonR, numpy for the ndarray.

Based on the idea by Peacock (1983), an upgrade by Fasano and Franceschin (1987) with
much guidance from Numerical recipes in C by Press and Teukolsky.

# References
Peacock, J. A. (1983). Two-dimensional goodness-of-fit testing in astronomy. **Monthly Notices of the Royal Astronomical Society**, 202(3), 615-627.
Fasano, G., & Franceschini, A. (1987). A multidimensional version of the Kolmogorov–Smirnov test. **Monthly Notices of the Royal Astronomical Society**, 225(1), 155-170.
Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (1996). Numerical recipes in C (Vol. 2). Cambridge: Cambridge university press.