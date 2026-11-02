---
tag: KHA4WMRDKY
kind: definition
name: Instrumental variables estimation
msc: [62P20, 62J05]
defines: 6ETK64HYK6
uses: [41FVC4P5JB, YM708KHV2W, 0AS800VAYX, 0KBFAWYRTE, 0WQNRCNY3M, 0ZC9YTXZRY, 0B8KZRT28M]
sources:
  - url: https://en.wikipedia.org/wiki/Instrumental_variables_estimation
---

## Definition

Consider the linear model $y_i = x_i^T \beta + \varepsilon_i$, $i = 1, \dots, n$, with $x_i \in \R^k$, $\beta \in \R^k$ unknown and $E[\varepsilon_i] = 0$, where $E[x_i \varepsilon_i] \ne 0$ is allowed.
A random vector $z_i \in \R^L$ with $L \ge k$ is a vector of *instruments* if:

1. (exogeneity) $E[z_i \varepsilon_i] = 0$;
2. (relevance) the $L \times k$ matrix $E[z_i x_i^T]$ has [[rank|0ZC9YTXZRY]] $k$.

Let $X$, $Z$ and $y$ stack the $x_i^T$, $z_i^T$ and $y_i$ as rows, and assume $Z^T Z$ and $X^T P_Z X$ are invertible, where $P_Z = Z (Z^T Z)^{-1} Z^T$.
The *two-stage least squares* or *instrumental variables estimator* is
$$\hat\beta_{\mathrm{IV}} = (X^T P_Z X)^{-1} X^T P_Z y.$$
When $L = k$ and $Z^T X$ is invertible, it reduces to $\hat\beta_{\mathrm{IV}} = (Z^T X)^{-1} Z^T y$.

## Remarks

The name two-stage least squares comes from its computation.
First regress each column of $X$ on $Z$, which gives $\hat X = P_Z X$, the [[orthogonal projection|0B8KZRT28M]] of $X$ onto the column space of $Z$.
Then regress $y$ on $\hat X$ by [[ordinary least squares|YM708KHV2W]].
Under clauses 1 and 2, for independent and identically distributed observations with finite second moments, $\hat\beta_{\mathrm{IV}}$ is [[consistent|0AS800VAYX]] for $\beta$, while ordinary least squares in general is not.

Example: $k = L = 1$, no intercept, $y_i = \beta x_i + \varepsilon_i$.
Exogeneity gives $E[z_i y_i] = \beta E[z_i x_i]$, so $\beta = E[z_i y_i] / E[z_i x_i]$.
The estimator $\sum_i z_i y_i / \sum_i z_i x_i$ is the sample analogue.

Non-example: if $z_i$ is independent of $x_i$ and $E[z_i] = 0$, then $E[z_i x_i] = 0$ and clause 2 fails; the ratio above has a denominator tending to $0$ and does not identify $\beta$.
Instruments that satisfy clause 2 only barely, called weak instruments, give unreliable estimates in finite samples.
