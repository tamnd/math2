---
tag: XCREJ9A53D
kind: definition
name: Bühlmann model
msc: [91G05, 62P05]
defines: BZJMY230YG
uses: [KWYCW4P8RH, 0WQNRCNY3M, 0477R9PYAE, 0TTDGTEFMN, 05NZ1HHQMV]
sources:
  - url: https://en.wikipedia.org/wiki/Bühlmann_model
---

## Definition

The *Bühlmann model* for one risk consists of a random parameter $\Theta$ and random claims $X_1, \dots, X_n$ such that:

1. Given $\Theta$, the claims $X_1, \dots, X_n$ are conditionally independent and identically distributed.
2. The hypothetical mean $m(\Theta) = E[X_j \mid \Theta]$ and the process variance $s^2(\Theta) = \operatorname{Var}(X_j \mid \Theta)$ have finite expectations and $m(\Theta)$ has finite variance.

Write $\mu = E[m(\Theta)]$, $v = E[s^2(\Theta)]$ and $a = \operatorname{Var}(m(\Theta))$, and assume $a > 0$.
The *Bühlmann credibility premium* is
$$P = Z \bar{X} + (1 - Z)\mu, \qquad Z = \frac{n}{n + k}, \qquad k = \frac{v}{a},$$
where $\bar{X} = (X_1 + \cdots + X_n)/n$.

## Remarks

Here $E$ is the [[expected value|0WQNRCNY3M]], $\operatorname{Var}$ is the [[variance|0477R9PYAE]] and $E[\cdot \mid \Theta]$ is [[conditional expectation|0TTDGTEFMN]].
Among all estimators of $m(\Theta)$ of the form $c_0 + c_1 X_1 + \cdots + c_n X_n$, the premium $P$ has the least [[mean squared error|05NZ1HHQMV]].
Example: if $v = 8$, $a = 2$ and $n = 4$, then $k = 4$ and $Z = 1/2$.
Non-example: if the claims are not conditionally identically distributed, for instance because the exposure grows from year to year, clause 1 fails; the Bühlmann–Straub model treats that case with weights.
If $a = 0$, all risks have the same mean, and the best premium is $\mu$ itself, which is the limit $Z = 0$.
The model is a special case of [[credibility theory|KWYCW4P8RH]].
