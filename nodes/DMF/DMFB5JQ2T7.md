---
tag: DMFB5JQ2T7
kind: definition
name: Breakdown point
msc: [62F35, 62G35]
defines: BRGGGZVQDS
uses: [0TTNRP5PFQ, 0QNRBHWV35, 08W2CW8PKW]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_statistics
    locator: Breakdown point
---

## Definition

Let $T$ be an [[estimator|0TTNRP5PFQ]] that maps each sample $x = (x_1, \dots, x_n)$ of points in $\R^p$ to a value $T(x) \in \R^k$.
For $0 \le m \le n$, let $\mathcal{Y}_m(x)$ be the set of samples obtained from $x$ by replacing at most $m$ points by arbitrary points of $\R^p$.
The *finite-sample breakdown point* of $T$ at $x$ is
$$\varepsilon^*_n(T, x) = \min\Big\{ \frac{m}{n} \;:\; \sup_{y \in \mathcal{Y}_m(x)} \norm{T(y) - T(x)} = \infty \Big\}.$$
The *asymptotic breakdown point* is the limit of $\varepsilon^*_n$ as $n \to \infty$, when it exists.

## Remarks

Example: the sample median of real data has $\varepsilon^*_n = \floor{(n+1)/2}/n$.
For $n = 2k + 1$, changing $k$ points leaves an original point at the middle position, between original values; changing $k + 1$ points to a huge value $M$ makes the median $M$.
So the asymptotic breakdown point of the [[median|08W2CW8PKW]] is $1/2$.

Non-example of robustness: the [[sample mean|0QNRBHWV35]] has $\varepsilon^*_n = 1/n$, since replacing one point $x_1$ by $x_1 + nM$ moves the mean by $M$.
Its asymptotic breakdown point is $0$.

The $k$-trimmed mean, which drops the $k$ smallest and $k$ largest values, has $\varepsilon^*_n = (k+1)/n$.
For estimators of location that are translation equivariant, the asymptotic breakdown point is at most $1/2$.
