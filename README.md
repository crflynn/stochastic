# 2DKS
2 Dimensional Kolmogorov-Smirnov test for goodness-of-fit.

Hypothesis testing
A KS test is a non parametric way to test if some data fits with a certain probability distribution, 
or if two datasets where created with the same underlying probability distribution. 
Note: the test only rejects the hypothesis that the data fits with the probability distribution, or does not reject it
for a certain significance level. It cannot confirm, only 'not-reject'.

For now, only the two sample 2D KS test is implemented.

Prerequisites: scipy  for the pearsonR, numpy for the ndarray.

Based on the idae by Peacock (1983), an upgrade by Fasano and Franceschin (1987) with
much guidance from Numerical recipes in C by Press and Teukolsky.
