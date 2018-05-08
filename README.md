# 2DKS
## 2 Dimensional Kolmogorov-Smirnov test for goodness-of-fit.

A KS test is a non parametric method from hypothesis testing. It checks wether data fits with a certain probability distribution, or if two datasets were created with the same underlying probability distribution. 
*Note*: the test only rejects the hypothesis that the data fits with the probability distribution, or does not reject it for a certain significance level. It cannot confirm, only 'not-reject'.

Mainly intened to be interacted with using functions `ks2d1s` and `ks2d2s`, which take as inputs one 2 column matrix and one 2D function or two two column matrices respectively. 
The algorithm finds the relative probabilities of finding data in the 4 quadrants that surround points in the data set, then uses those to compute the K-S statistic with its distribution function. Look around 14.3.7 and 14.7.1 in [3] for detailed arcane mathemagics explanations. 

Prerequisites: *scipy*, *numpy*.

Keywords: Kolmogoro-smirnov test, multi-dimensional, two-dimensional, KS test, hypothesis testing, statistics, probability theory.

Based on the idea by Peacock (1983), an upgrade by Fasano and Franceschin (1987) with
much guidance from Numerical recipes in C by Press and Teukolsky.

# References
[1] Peacock, J. A. (1983). Two-dimensional goodness-of-fit testing in astronomy. *Monthly Notices of the Royal Astronomical Society*, 202(3), 615-627.

[2] Fasano, G., & Franceschini, A. (1987). A multidimensional version of the Kolmogorov–Smirnov test. *Monthly Notices of the Royal Astronomical Society*, 225(1), 155-170.

[3] Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (1996). *Numerical recipes in C (Vol. 2).* Cambridge: Cambridge university press.
