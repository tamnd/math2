---
tag: YE8SC6FQ1Q
kind: definition
name: Chain-ladder method
msc: [91G05, 62P05]
defines: BTXP4Y6S2G
uses: []
sources:
  - url: https://en.wikipedia.org/wiki/Chain-ladder_method
---

## Definition

Let $n \ge 2$.
A *run-off triangle* is a family of positive numbers $C_{i,j}$ for $i, j \in \set{1, \dots, n}$ with $i + j \le n + 1$.
The number $C_{i,j}$ is the cumulative claim amount of accident year $i$ after $j$ development years.
The *chain-ladder method* computes:

1. the development factors $\displaystyle \hat f_j = \frac{\sum_{i=1}^{n-j} C_{i,j+1}}{\sum_{i=1}^{n-j} C_{i,j}}$ for $j = 1, \dots, n-1$;
2. the projected ultimate claims $\hat C_{i,n} = C_{i,n+1-i} \, \hat f_{n+1-i} \, \hat f_{n+2-i} \cdots \hat f_{n-1}$ for $i = 2, \dots, n$, and $\hat C_{1,n} = C_{1,n}$;
3. the reserve $\hat R_i = \hat C_{i,n} - C_{i,n+1-i}$ for each accident year $i$, and the total reserve $\sum_{i} \hat R_i$.

## Remarks

Example with $n = 2$: $C_{1,1} = 100$, $C_{1,2} = 150$, $C_{2,1} = 200$.
Then $\hat f_1 = 150/100 = 1.5$, $\hat C_{2,2} = 200 \cdot 1.5 = 300$ and the reserve is $\hat R_2 = 100$.
Non-example: incremental amounts, the claims paid in each development year only, are not a run-off triangle in the sense above.
The factors must be computed from cumulative amounts, so one first takes partial sums along each row.
Each $\hat f_j$ is a weighted average of the individual ratios $C_{i,j+1}/C_{i,j}$ with weights $C_{i,j}$.
Mack's distribution-free model gives assumptions under which the chain-ladder projections are unbiased and yields a formula for their standard error.
