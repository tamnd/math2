---
tag: DYFY16SFHZ
kind: concept
name: Kendall rank correlation coefficient
msc: [62H20, 62G10]
sources:
  - url: https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient
same_as:
  wikidata: Q3268404
  wikipedia: Kendall rank correlation coefficient
---

## Summary

The Kendall rank correlation coefficient $\tau$ measures the agreement between the orderings of two variables.
It compares every pair of observations.
It counts the pairs ordered the same way by both variables, minus the pairs ordered in opposite ways, and divides by the number of pairs.
It lies between $-1$ and $1$ and depends only on the ranks of the data, like [[Spearman's coefficient|DJFYTQJ3SH]].

## Explanations

### L1 human

Take two judges who rank the same contestants.
For each pair of contestants, check whether the two judges put them in the same order.
Kendall's $\tau$ is the share of pairs on which they agree minus the share on which they disagree.
If they agree on every pair, $\tau = 1$; if they disagree on every pair, $\tau = -1$.
With three contestants ranked $1, 2, 3$ and $1, 3, 2$, the judges agree on two of three pairs, so $\tau = 2/3 - 1/3 = 1/3$.
