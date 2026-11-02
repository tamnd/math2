---
tag: JWH2KYCGBQ
kind: statement
role: proposition
name: Shift property of the Z-transform
msc: [44A55, 39A06]
uses: [3DBAMXA80B, EPG6JPVJE7, 1P8WX3EGHF]
about: [5FY0JQGHYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Properties
---

## Statement

Let $x = (x_n)_{n \in \Z}$ be a sequence of complex numbers and let $k$ be an integer.

1. Bilateral form. Let $y_n = x_{n - k}$ for all $n \in \Z$. Then $y$ and $x$ have the same [[region of convergence|1P8WX3EGHF]], and on it the [[bilateral Z-transforms|3DBAMXA80B]] satisfy $Y(z) = z^{-k} X(z)$.
2. Unilateral delay. Suppose $x_n = 0$ for $n < 0$ and $k \ge 0$. Then the [[unilateral Z-transform|EPG6JPVJE7]] of $(x_{n - k})_{n \ge 0}$ is $z^{-k} X(z)$.
3. Unilateral advance. Let $k \ge 1$ and let $X$ be the unilateral Z-transform of $(x_n)_{n \ge 0}$. Then the unilateral Z-transform of $(x_{n + k})_{n \ge 0}$ is
$$z^{k} \left( X(z) - \sum_{j=0}^{k-1} x_j z^{-j} \right),$$
on the same set of $z$.

## Remarks

Each clause is a change of summation index.
For clause 1, $\sum_n x_{n-k} z^{-n} = z^{-k} \sum_m x_m z^{-m}$ with $m = n - k$, and the same computation with absolute values shows that the regions agree.
For clause 3, $\sum_{n \ge 0} x_{n+k} z^{-n} = z^{k} \sum_{m \ge k} x_m z^{-m}$, and the sum over $m \ge k$ is $X(z)$ minus its first $k$ terms.
Example: for $x_n = 1$ ($n \ge 0$), $X(z) = z/(z-1)$, and clause 3 with $k = 1$ gives $z (z/(z-1) - 1) = z/(z-1)$, as it must, since the shifted sequence is again constant.
Clause 2 needs $x_n = 0$ for $n < 0$; otherwise the terms $x_{-k}, \ldots, x_{-1}$ also enter the unilateral transform of the delayed sequence.

## Explanations

### L1 human

Delaying a sequence by one step multiplies its Z-transform by $z^{-1}$.
Advancing it by one step multiplies by $z$, but in the one-sided case the first value falls off and must be subtracted.
This is why $z^{-1}$ is called the unit delay in signal processing.

### L2 human

Clause 3 is the discrete analogue of $\mathcal{L}\{f'\}(s) = s F(s) - f(0)$ for the Laplace transform.
It is what makes the Z-transform solve linear difference equations with constant coefficients: each shifted unknown becomes $z^k$ times the transform, plus a polynomial built from the initial values.
Clause 1 shows that a time-invariant system acts on transforms by multiplication.
