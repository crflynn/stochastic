# 2DKS
## 2 Dimensional Kolmogorov-Smirnov test for goodness-of-fit.

KS tests are non-parametric methods made to test the hypothesis that data fits a certain probability distribution, or to see if the distribution function of two datasets differs. 
*Note*: the test only rejects the hypothesis that the data fits with the probability distribution, or does not reject it for a certain significance level. It cannot confirm, only 'not-reject'.

In this case, we check if two-dimensional data fits a particular distribution. The extension to higher dimensions is non-trivial and requires on the order of N2 operations i.e. slow for large datasets.

Mainly intended to be interacted with using functions `ks2d1s` and `ks2d2s`, which take as inputs one 2-column matrix and one 2D function, or two 2-column matrices respectively. 
These algorithms compute the relative probabilities of finding data in orthonormal quadrants that surround each point in the data set, then uses those to compute the K-S statistic with its distribution function (`Qks`). Look around 14.3.7 and 14.7.1 in [3] for detailed arcane mathemagic explanations. 

## Issues
Float number representation and rounding: probabilities expected to sum to 1.0 return 0.99999999 instead, etc...  No plans to implement any kind of solution to this: it sounds much more trouble than it is worth. This test is theoretically just an approximation, rounding to a couple digits seem reasonable.

The computed KS statistic remains untested.

ks2d1s: Input: no 2D XxY density matrices, 
    Integration method: only numerical.

## MISC

Prerequisites: *scipy*, *numpy*.

Keywords: Kolmogoro-smirnov test, multi-dimensional, two-dimensional, KS test, hypothesis testing, statistics, probability theory.

Based on the idea by Peacock (1983), an upgrade by Fasano and Franceschin (1987) with
much guidance from Numerical recipes in C by Press and Teukolsky (1996).

# References
[1] Peacock, J. A. (1983). Two-dimensional goodness-of-fit testing in astronomy. *Monthly Notices of the Royal Astronomical Society*, 202(3), 615-627.

[2] Fasano, G., & Franceschini, A. (1987). A multidimensional version of the Kolmogorov–Smirnov test. *Monthly Notices of the Royal Astronomical Society*, 225(1), 155-170.

[3] Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (1996). *Numerical recipes in C (Vol. 2).* Cambridge: Cambridge university press.
