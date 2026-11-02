---
tag: 8GWEWBZE9P
kind: definition
name: Mann–Whitney U test
msc: [62G10]
defines: CKF9KDXBP7
uses: [087P03NEND, 0AJN7WHBJZ, 0MXMS3AE13]
sources:
  - url: https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test
---

## Definition

Let $X_1, \dots, X_m$ be [[i.i.d.|0AJN7WHBJZ]] with continuous [[distribution function|0MXMS3AE13]] $F$, and let $Y_1, \dots, Y_n$ be i.i.d. with continuous distribution function $G$, independent of the $X_i$.
The *Mann–Whitney statistic* is
$$U = \#\set{(i, j) : 1 \le i \le m, \ 1 \le j \le n, \ X_i > Y_j}.$$
The *Mann–Whitney U test* of $H_0 \colon F = G$ rejects $H_0$ when $U$ is far from $mn/2$.
For a one-sided alternative it rejects only when $U$ is large, or only when $U$ is small.
Under $H_0$ the law of $U$ depends only on $m$ and $n$.

## Remarks

Let $R_X$ be the sum of the ranks of $X_1, \dots, X_m$ in the pooled sample of size $m + n$.
Then $U = R_X - m(m+1)/2$, so the test is the same as the Wilcoxon rank-sum test.
Under $H_0$, $E[U] = mn/2$ and $\operatorname{Var}(U) = mn(m + n + 1)/12$, and $U$ is asymptotically normal.
The ratio $U/(mn)$ is an unbiased estimator of $P(X_1 > Y_1)$, and $U$ is a two-sample [[U-statistic|NTVQB1DC56]].
With ties, each tied pair counts $1/2$.

Example: $X = (3, 5)$ and $Y = (1, 4)$.
The pairs with $X_i > Y_j$ are $(3, 1)$, $(5, 1)$ and $(5, 4)$, so $U = 3$.
In the pooled order $1, 3, 4, 5$ the $X$ values have ranks $2$ and $4$, and $R_X - 3 = 6 - 3 = 3$ agrees.

Non-example: measurements of the same subjects before and after a treatment are not independent samples.
The clause on independence fails, and the [[Wilcoxon signed-rank test|38SETDT2HN]] on the differences is used instead.
