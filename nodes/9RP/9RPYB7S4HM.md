---
tag: 9RPYB7S4HM
kind: definition
name: Wilcoxon signed-rank test
msc: [62G10]
defines: 38SETDT2HN
uses: [087P03NEND, 0AJN7WHBJZ, 0J97P5KZY0]
sources:
  - url: https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test
---

## Definition

Let $Z_1, \dots, Z_n$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with a continuous distribution that is symmetric about a number $\theta$, that is, $Z_1 - \theta$ and $\theta - Z_1$ have the same law.
Let $R_i$ be the rank of $\abs{Z_i}$ among $\abs{Z_1}, \dots, \abs{Z_n}$, so that the smallest has rank $1$.
The *signed-rank statistic* is
$$W^+ = \sum_{i \,:\, Z_i > 0} R_i.$$
The *Wilcoxon signed-rank test* of $H_0 \colon \theta = 0$ rejects $H_0$ when $W^+$ is too large, too small, or either, according to the alternative.
Under $H_0$, $W^+$ has the law of $\sum_{k=1}^{n} k B_k$, where $B_1, \dots, B_n$ are independent [[Bernoulli|0J97P5KZY0]] variables with parameter $1/2$.

## Remarks

Under $H_0$, $E[W^+] = n(n+1)/4$ and $\operatorname{Var}(W^+) = n(n+1)(2n+1)/24$, and $W^+$ is asymptotically normal.
For matched pairs $(X_i, Y_i)$ one takes $Z_i = Y_i - X_i$.

Example: $Z = (1.2, -0.4, 2.5)$.
The absolute values $1.2, 0.4, 2.5$ have ranks $2, 1, 3$, so $W^+ = 2 + 3 = 5$.
Under $H_0$ each of the $8$ sign patterns has probability $1/8$, and only the sets of ranks $\set{2, 3}$ and $\set{1, 2, 3}$ give a sum at least $5$.
So the one-sided p-value is $P(W^+ \ge 5) = 2/8 = 1/4$.

Non-example: if the $Z_i$ have median $0$ but a skewed law, the clause on symmetry fails.
Then the null law above is wrong, and the test can reject often even though the median is $0$; the [[sign test|NBK6G2VB7A]] is valid in that case.

Inverting the test gives the [[Hodges–Lehmann estimator|T6KRQAQQ15]] of $\theta$.
