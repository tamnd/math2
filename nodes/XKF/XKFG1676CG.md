---
tag: XKFG1676CG
kind: concept
name: Empirical process
msc: [60F17, 62G30]
specializes: [0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Empirical_process
same_as:
  wikidata: Q5374250
  wikipedia: Empirical process
---

## Summary

The empirical process of a sample is the gap between its empirical distribution function and the true [[cumulative distribution function|0H8H7ZTHW2]], times $\sqrt{n}$.
It is the main object behind uniform laws of large numbers and functional central limit theorems in statistics.
The [[Glivenko–Cantelli theorem|E7B78X780X]] and [[Donsker's theorem|818832PMSV]] describe its behaviour as the sample size grows.

## Explanations

### L1 human

Draw $n$ numbers at random from a distribution and plot the fraction of them below each level $x$.
This staircase is the empirical distribution function, and it should be close to the true distribution function $F$.
The empirical process is the error between the two curves, multiplied by $\sqrt{n}$ so that it stays of order one.
For one fixed $x$ it is just the rescaled error of a proportion, which the central limit theorem says is roughly normal.
Seen as a random curve in $x$, it looks like a [[Brownian bridge|3MCVMBAGD1]] for large $n$.
