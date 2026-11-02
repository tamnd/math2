---
tag: Q4YAST023H
kind: statement
role: theorem
name: Newton–Gregory forward formula
msc: [41A05, 65D05, 39A70]
uses: [9W77FPTM9E, N5ZHV4HWDC, 0GBZM0MT0F]
about: [9W77FPTM9E]
sources:
  - url: https://en.wikipedia.org/wiki/Newton_polynomial
---

## Statement

Let $x_0 \in \R$, let $h > 0$, and let $x_i = x_0 + i h$ for $i = 0, 1, \dots, n$.
Let $f$ be a real function defined at these points.
Define the forward differences by $\Delta^0 f(x) = f(x)$ and $\Delta^{k+1} f(x) = \Delta^k f(x + h) - \Delta^k f(x)$.
Let $p$ be the interpolating polynomial of degree at most $n$ with $p(x_i) = f(x_i)$ for $i = 0, \dots, n$.
Then for every real $s$,
$$p(x_0 + s h) = \sum_{k=0}^{n} \binom{s}{k} \Delta^k f(x_0), \qquad \binom{s}{k} = \frac{s (s - 1) \cdots (s - k + 1)}{k!}.$$

## Remarks

Proof idea: the [[Newton polynomial|9W77FPTM9E]] gives $p(x) = \sum_{k=0}^{n} f[x_0, \dots, x_k] \prod_{j<k} (x - x_j)$.
For equally spaced nodes, induction on $k$ shows that the [[divided difference|N5ZHV4HWDC]] is $f[x_0, \dots, x_k] = \Delta^k f(x_0) / (k!\, h^k)$.
With $x = x_0 + s h$ one has $\prod_{j<k} (x - x_j) = h^k s (s - 1) \cdots (s - k + 1)$, and the two formulas combine.

Example: $f(x) = x^2$, $x_0 = 0$, $h = 1$, $n = 2$.
The values are $0, 1, 4$, so $\Delta f(0) = 1$ and $\Delta^2 f(0) = 2$.
The formula gives $p(s) = 0 + s + \binom{s}{2} \cdot 2 = s + s(s - 1) = s^2$, which is $f$ itself.

The formula needs equal spacing; for unequal nodes the general Newton form with divided differences must be used.

## Explanations

### L1 human

Given equally spaced values of a function, the formula builds the polynomial through them from a table of differences.
The first differences measure slope, the second differences measure curvature, and so on.
The weights are binomial coefficients in the position $s$, measured in steps of $h$.
It is the discrete analogue of the Taylor series, with differences in place of derivatives and $\binom{s}{k}$ in place of $s^k / k!$.

### L2 human

The formula is the basis of classical table interpolation and of many finite difference formulas.
Differentiating or integrating it term by term gives numerical differentiation rules and the Newton–Cotes formulas.
The error is that of [[polynomial interpolation|SS1YMS2NPC]]: if $f$ is $n + 1$ times differentiable, then $f(x_0 + s h) - p(x_0 + s h) = h^{n+1} \binom{s}{n+1} f^{(n+1)}(\xi)$ for some $\xi$ in the smallest interval containing $x_0, x_n$ and $x_0 + s h$.
There is a matching backward formula, based at $x_n$ with backward differences.
