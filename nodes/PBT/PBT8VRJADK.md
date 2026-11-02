---
tag: PBT8VRJADK
kind: concept
name: F-distribution
msc: ["62E15", "60E05"]
specializes: [0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/F-distribution
same_as:
  wikidata: Q177144
  wikipedia: F-distribution
---

## Summary

The F-distribution is the distribution of a ratio of two independent chi-squared variables, each divided by its degrees of freedom.
It has two parameters, the numerator and the denominator degrees of freedom.
It is the reference distribution of the F-test, of analysis of variance and of tests that compare two variances in normal models.

## Explanations

### L1 human

Take two independent estimates of the same variance, each based on its own number of normal observations.
Their ratio should be near $1$, but it fluctuates by chance, and the F-distribution describes exactly how much.
A ratio far above $1$ is evidence that the two variances are not equal after all.
For example, the square of a Student $t$ variable with $\nu$ degrees of freedom has the F-distribution with $1$ and $\nu$ degrees of freedom.
