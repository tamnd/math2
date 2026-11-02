---
tag: A05WR6TEK5
kind: concept
name: Empirical distribution function
msc: [62G30]
sources:
  - url: https://en.wikipedia.org/wiki/Empirical_distribution_function
same_as:
  wikidata: Q1339385
  wikipedia: Empirical distribution function
---

## Summary

The empirical distribution function of a sample is the [[cumulative distribution function|0H8H7ZTHW2]] of the distribution that puts mass $1/n$ on each observation.
At each point $t$ it gives the fraction of observations that are at most $t$.
It estimates the true distribution function without any parametric assumption, and for an i.i.d. sample the [[Glivenko–Cantelli theorem|E7B78X780X]] shows that it converges to it uniformly, almost surely.
Goodness-of-fit tests such as the [[Kolmogorov–Smirnov test|YZYHWC6C5F]] compare it with a hypothesised distribution function.

## Explanations

### L1 human

Sort your data and draw a staircase that starts at height $0$ and jumps up by $1/n$ at each data point.
This staircase is the empirical distribution function.
For the data $1, 2, 2, 5$, it is $0$ before $1$, $1/4$ on $[1, 2)$, $3/4$ on $[2, 5)$ and $1$ from $5$ on.
With more and more data, the staircase hugs the true distribution function more and more closely.
