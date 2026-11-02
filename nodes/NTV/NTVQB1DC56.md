---
tag: NTVQB1DC56
kind: concept
name: U-statistic
msc: [62G05, 62G20]
specializes: [0Q5CG2NEQ8]
sources:
  - url: https://en.wikipedia.org/wiki/U-statistic
same_as:
  wikidata: Q7862949
  wikipedia: U-statistic
---

## Summary

A U-statistic is the average of a symmetric function, the kernel, over all subsets of a fixed size of the observations.
It is an unbiased estimator of the mean of the kernel.
The sample mean, the sample variance, Kendall's $\tau$ and the Mann–Whitney statistic are U-statistics or close relatives of them.
Under mild conditions, Hoeffding's theory gives their asymptotic normality in one stroke.

## Explanations

### L1 human

Suppose you want to estimate the average squared distance between two random members of a population.
Take every pair of points in your sample, compute half their squared distance, and average over all pairs.
This average is a U-statistic, and it turns out to be exactly the usual sample variance.
Averaging over all subsets, instead of using only some of them, uses the data as fully as possible.
