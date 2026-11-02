---
tag: YA786MZ8QD
kind: definition
name: Permutation test
msc: [62G10, 62G09]
defines: 2ECAM46NE2
uses: [087P03NEND, 0EHYZFZ4PK, 036756NFD6, 0RJMNEN3BJ]
sources:
  - url: https://en.wikipedia.org/wiki/Permutation_test
---

## Definition

Let $Z = (Z_1, \dots, Z_N)$ be a random vector, and let $S_N$ be the [[symmetric group|0RJMNEN3BJ]], acting on $\R^N$ by $(\pi z)_i = z_{\pi^{-1}(i)}$.
Let $H_0$ be a null hypothesis under which $Z$ is exchangeable, that is, $\pi Z$ has the same law as $Z$ for every $\pi \in S_N$.
Let $T \colon \R^N \to \R$ be a [[statistic|036756NFD6]].
The *permutation p-value* is
$$p(Z) = \frac{1}{N!} \, \#\set{\pi \in S_N : T(\pi Z) \ge T(Z)}.$$
The *permutation test* at level $\alpha$ rejects $H_0$ when $p(Z) \le \alpha$.

## Remarks

Under $H_0$, $P(p(Z) \le \alpha) \le \alpha$ for every $\alpha \in [0, 1]$, so the test has level $\alpha$, whatever the law of $Z$.
In the two-sample problem, $Z$ is the pooled sample $X_1, \dots, X_m, Y_1, \dots, Y_n$ with $N = m + n$, and $H_0$ says that all $N$ values are i.i.d.
Since $T$ usually depends only on which values fall in the first group, one may count the $\binom{N}{m}$ splits instead of the $N!$ permutations.
When $N!$ is too large, one uses a random sample of permutations, which gives a Monte Carlo approximation of $p(Z)$.

Example: $X = (3, 5)$, $Y = (1, 4)$ and $T = \bar X - \bar Y$, so $T = 4 - 2.5 = 1.5$.
The $6$ splits of $\set{1, 3, 4, 5}$ give the $X$-pairs $\set{1,3}, \set{1,4}, \set{1,5}, \set{3,4}, \set{3,5}, \set{4,5}$ and the values $-2.5, -1.5, -0.5, 0.5, 1.5, 2.5$.
Two of them are at least $1.5$, so $p = 2/6 = 1/3$.

Non-example: if under $H_0$ the two groups have the same mean but different variances, the pooled vector is not exchangeable.
The clause on exchangeability fails, and the test of equal means need not have level $\alpha$.

The [[Mann–Whitney U test|CKF9KDXBP7]] is a permutation test whose statistic depends only on the ranks.
