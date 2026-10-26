---
tag: 0TTA57SEJG
kind: definition
name: Convergence in mean
msc: [60F25]
defines: 0A2HNZC44K
uses: [0DCT0QZVQ1, 0DKRR22AEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_random_variables
    locator: Convergence in mean
---

## Definition

Let $r \ge 1$ be real. Let $X, X_1, X_2, \dots$ be real random variables on one probability space with $E[|X|^r] < \infty$ and $E[|X_n|^r] < \infty$ for each $n$.
The sequence $(X_n)$ converges in $r$-th mean, or in $L^r$, to $X$ if
$$\lim_{n \to \infty} E\left[|X_n - X|^r\right] = 0.$$
For $r = 1$ one says convergence in mean, and for $r = 2$ convergence in mean square.

## Remarks

By [[Markov's inequality|05PWWHYBX5]], $P(|X_n - X| > \varepsilon) \le E[|X_n - X|^r] / \varepsilon^r$. So convergence in $r$-th mean implies convergence in probability.
For $s \ge r \ge 1$, convergence in $s$-th mean implies convergence in $r$-th mean.
Convergence in mean does not imply almost sure convergence, and almost sure convergence does not imply convergence in mean.
Example: on $[0, 1]$ with the uniform measure, $X_n = n \, 1_{[0, 1/n]}$ converges to $0$ almost surely but $E[X_n] = 1$ for all $n$.

## Explanations

### L1 human

Convergence in mean asks that the average size of the error $|X_n - X|^r$ goes to $0$.
Mean square convergence, with $r = 2$, is common in statistics, where it says that the mean squared error of an estimator goes to $0$.
