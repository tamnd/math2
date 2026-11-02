---
tag: 2S6XZCQWY7
kind: definition
name: Generalized Fourier series
msc: [42C15, 42C10, 46C05]
defines: SNJC87TBHD
uses: [0QVNCJXRY3, 0Y2X7P2WB7, HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_Fourier_series
---

## Definition

Let $V$ be an [[inner product space|0QVNCJXRY3]] with inner product $\ip{\cdot}{\cdot}$, linear in the first argument.
Let $(\varphi_k)_{k \ge 0}$ be a sequence of nonzero, pairwise [[orthogonal|0Y2X7P2WB7]] vectors of $V$.
For $f \in V$, the *generalized Fourier coefficients* of $f$ are the numbers
$$c_k = \frac{\ip{f}{\varphi_k}}{\ip{\varphi_k}{\varphi_k}}, \quad k \ge 0.$$
The formal series $\sum_{k \ge 0} c_k \varphi_k$ is the *generalized Fourier series* of $f$ with respect to $(\varphi_k)$.

## Remarks

If the $\varphi_k$ are orthonormal, $c_k = \ip{f}{\varphi_k}$.
The partial sum $\sum_{k \le N} c_k \varphi_k$ is the orthogonal projection of $f$ onto the span of $\varphi_0, \dots, \varphi_N$, the closest point of that span to $f$.
By [[Bessel's inequality|0RBT5PB74K]], $\sum_k \abs{c_k}^2 \norm{\varphi_k}^2 \le \norm{f}^2$.
In a [[Hilbert space|HM2HHE3J51]] the series converges to the projection of $f$ onto the closed span of the family.
It converges to $f$ for every $f$ exactly when the family is complete, and then [[Parseval's identity|047RFCNVSK]] holds.

Example: in $L^2(-1, 1)$, take the Legendre polynomials $\varphi_0 = 1$, $\varphi_1 = x$, $\varphi_2 = \frac12 (3x^2 - 1)$, and so on, and $f(x) = x^2$.
Then $\ip{f}{\varphi_0} = \frac23$, $\ip{\varphi_0}{\varphi_0} = 2$, $\ip{f}{\varphi_1} = 0$, $\ip{f}{\varphi_2} = \frac{4}{15}$ and $\ip{\varphi_2}{\varphi_2} = \frac25$.
So $c_0 = \frac13$, $c_1 = 0$, $c_2 = \frac23$, and indeed $x^2 = \frac13 + \frac23 \cdot \frac12(3x^2 - 1)$; all later coefficients vanish.

Non-example: the formula fails to reconstruct $f$ when the family is not orthogonal.
In $L^2(0, 1)$ with $\varphi_0 = 1$ and $\varphi_1 = x$, which are not orthogonal, the function $f = x$ gives $c_0 = \frac12$ and $c_1 = 1$, so $c_0 \varphi_0 + c_1 \varphi_1 = x + \frac12 \ne f$.
