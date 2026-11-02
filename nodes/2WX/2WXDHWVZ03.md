---
tag: 2WXDHWVZ03
kind: definition
name: F-test
msc: [62F03, 62J10]
defines: 8MTVCMAATD
uses: [087P03NEND, PBT8VRJADK, 036756NFD6]
sources:
  - url: https://en.wikipedia.org/wiki/F-test
---

## Definition

Let $d_1, d_2 \ge 1$ be integers and let $\alpha \in (0, 1)$.
An *F-test* is a [[hypothesis test|087P03NEND]] of a null hypothesis $H_0$ based on a [[statistic|036756NFD6]] $F \ge 0$ with the following property.
Under $H_0$, $F$ has the [[F-distribution|PBT8VRJADK]] with $d_1$ and $d_2$ degrees of freedom.
The test at level $\alpha$ rejects $H_0$ when $F > F_{1 - \alpha}(d_1, d_2)$, the $1 - \alpha$ quantile of that law.

## Remarks

Example: in one-way analysis of variance, there are $k$ groups and $N$ observations in total, with independent normal errors of common variance.
Let $\mathrm{SSB}$ be the sum of squares between groups and $\mathrm{SSW}$ the sum of squares within groups.
Under $H_0$ that all group means are equal, $F = \frac{\mathrm{SSB}/(k - 1)}{\mathrm{SSW}/(N - k)}$ has the F-distribution with $k - 1$ and $N - k$ degrees of freedom.
The check: $\mathrm{SSB}/\sigma^2$ and $\mathrm{SSW}/\sigma^2$ are independent chi-squared variables with $k - 1$ and $N - k$ degrees of freedom, by Cochran's theorem.
Non-example: for two non-normal samples, the variance ratio $S_1^2/S_2^2$ does not have an F-distribution under equal variances in general.
So comparing it with F quantiles is not an F-test in this sense, and its level can be far from $\alpha$.
