---
tag: A01GEGWKVB
kind: concept
name: Variance reduction
msc: [65C05]
sources:
  - url: https://en.wikipedia.org/wiki/Variance_reduction
same_as:
  wikidata: Q3454689
  wikipedia: Variance reduction
---

## Summary

Variance reduction is the family of techniques that make a [[Monte Carlo method|HWP11G3HTN]] more accurate for the same computing effort.
The error of a plain Monte Carlo estimate with $n$ samples is about $\sigma/\sqrt{n}$, where $\sigma^2$ is the [[variance|0477R9PYAE]] of one sample.
The rate $n^{-1/2}$ is fixed for plain random sampling.
So the gains come from replacing the sampled quantity by another with the same mean and a smaller variance.
Halving $\sigma$ saves a factor of four in the number of samples.

## Explanations

### L1 human

A Monte Carlo estimate is noisy, and the noise shrinks slowly as more samples are taken.
Variance reduction attacks the noise at its source: it changes what is sampled so that each sample is less scattered while the average stays the same.
For example, to estimate the average of $f(U) = U$ for uniform $U$ in $(0, 1)$, the pair average $\frac12 (U + (1 - U))$ is always exactly $\frac12$, so it has no scatter at all.
Real problems do not give such perfect cancellation, but gains by factors of ten or a hundred are common.
