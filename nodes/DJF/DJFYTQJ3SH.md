---
tag: DJFYTQJ3SH
kind: concept
name: Spearman's rank correlation coefficient
msc: [62H20, 62G10]
sources:
  - url: https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient
same_as:
  wikidata: Q1126730
  wikipedia: Spearman's rank correlation coefficient
---

## Summary

Spearman's rank correlation coefficient $\rho_s$ is the Pearson [[correlation coefficient|0DNN9B6Q2F]] of the ranks of two variables.
It measures how well the relation between the variables is described by a monotone function, not only by a straight line.
It lies between $-1$ and $1$, and it equals $1$ exactly when one variable is a strictly increasing function of the other on the sample.
It is unchanged by any strictly increasing change of scale of either variable.

## Explanations

### L1 human

Replace each value of $x$ by its place in the sorted list of $x$ values, and do the same for $y$.
Then compute the ordinary correlation of these places.
If larger $x$ always goes with larger $y$, the places agree and the coefficient is $1$, even when the relation is curved.
For example, the points $(1, 1), (2, 4), (3, 9)$ lie on a parabola, not a line, yet their Spearman coefficient is $1$.
