---
tag: GWGFT35TCZ
kind: definition
name: Analysis of variance
msc: [62J10]
defines: M9AQ5HKGP4
uses: [A06SGFCSCE, 8MTVCMAATD, PBT8VRJADK, 05AQE0QR0D, 03Y6AQ2S0J]
sources:
  - url: https://en.wikipedia.org/wiki/Analysis_of_variance
---

## Definition

Let $k \ge 2$ and $n_1, \dots, n_k \ge 1$, with $N = n_1 + \cdots + n_k > k$.
Let $y_{ij}$, for $i = 1, \dots, k$ and $j = 1, \dots, n_i$, be observations of $k$ groups.
Let $\bar y_i = \frac{1}{n_i} \sum_j y_{ij}$ be the mean of group $i$ and $\bar y = \frac{1}{N} \sum_{i,j} y_{ij}$ the overall mean.
The *one-way analysis of variance* is the decomposition
$$\sum_{i=1}^k \sum_{j=1}^{n_i} (y_{ij} - \bar y)^2 = \sum_{i=1}^k n_i (\bar y_i - \bar y)^2 + \sum_{i=1}^k \sum_{j=1}^{n_i} (y_{ij} - \bar y_i)^2,$$
written $SS_{\mathrm{tot}} = SS_{\mathrm{between}} + SS_{\mathrm{within}}$, together with the statistic
$$F = \frac{SS_{\mathrm{between}} / (k - 1)}{SS_{\mathrm{within}} / (N - k)},$$
defined when $SS_{\mathrm{within}} > 0$.
Consider the model $y_{ij} = \mu_i + \varepsilon_{ij}$ with independent errors $\varepsilon_{ij} \sim N(0, \sigma^2)$.
The *ANOVA $F$-test* of level $\alpha$ rejects the hypothesis $\mu_1 = \cdots = \mu_k$ when $F$ is large.
The threshold is the upper $\alpha$-quantile of the [[F-distribution|PBT8VRJADK]] with $k - 1$ and $N - k$ degrees of freedom.

## Remarks

The decomposition holds because, inside each group, the deviations $y_{ij} - \bar y_i$ sum to zero, so the cross term vanishes.
Under the hypothesis of equal means and [[normal|05AQE0QR0D]] errors, $F$ has the $F$-distribution with $k - 1$ and $N - k$ degrees of freedom.

Example: groups $\{1, 2, 3\}$ and $\{4, 5, 6\}$, so $k = 2$, $N = 6$, $\bar y_1 = 2$, $\bar y_2 = 5$, $\bar y = 3.5$.
Then $SS_{\mathrm{between}} = 3 \cdot 1.5^2 + 3 \cdot 1.5^2 = 13.5$ and $SS_{\mathrm{within}} = 2 + 2 = 4$.
Their sum $17.5$ equals $\sum (y - 3.5)^2 = 2(6.25 + 2.25 + 0.25)$.
So $F = 13.5 / (4/4) = 13.5$ on $1$ and $4$ degrees of freedom.

Non-example: if the groups have very different error variances, the hypothesis of a common $\sigma^2$ fails.
Then $F$ no longer has the $F$-distribution under equal means, and Welch's test is used instead.

The same idea extends to several factors, with one sum of squares for each main effect and interaction.
All these fixed-effects analyses are special cases of the [[general linear model|A06SGFCSCE]].
With $k = 2$, the $F$ statistic is the square of the two-sample $t$ statistic with pooled variance.
