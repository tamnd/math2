---
tag: W11JCMFK4D
kind: statement
role: theorem
name: Superstability of the exponential equation
msc: [39B82, 39B52]
uses: [0XMEM406JM, CEGF8W64VQ]
about: [CEGF8W64VQ, TPYXQTYND6]
sources:
  - url: https://en.wikipedia.org/wiki/Hyers%E2%80%93Ulam%E2%80%93Rassias_stability
---

## Statement

Let $(S, +)$ be a [[semigroup|0XMEM406JM]], let $\delta \ge 0$, and let $f \colon S \to \C$ satisfy
$$\abs{f(x + y) - f(x) f(y)} \le \delta \quad \text{for all } x, y \in S.$$
Then one of the following holds:

1. $\abs{f(x)} \le \frac{1 + \sqrt{1 + 4\delta}}{2}$ for all $x \in S$;
2. $f(x + y) = f(x) f(y)$ for all $x, y \in S$.

## Remarks

Write $K = \frac{1 + \sqrt{1 + 4\delta}}{2}$, so that $K^2 - \delta = K$ and $K \ge 1$.
If $\abs{f(a)} = K + \eta$ with $\eta > 0$, then $\abs{f(2a)} \ge (K + \eta)^2 - \delta \ge K + 2\eta$, and iterating shows that $f$ is unbounded.
If $f$ is unbounded, compare $f(x + y + z)$ with $f(x + y) f(z)$ and with $f(x) f(y + z)$ to get
$$\abs{f(x + y) - f(x) f(y)} \abs{f(z)} \le 2\delta + \abs{f(x)} \delta,$$
and let $\abs{f(z)} \to \infty$.
So an approximate solution of [[Cauchy's exponential equation|CEGF8W64VQ]] is either bounded or an exact solution.
This is called superstability: it is stronger than [[Hyers–Ulam stability|TPYXQTYND6]], since an unbounded approximate solution must be exact.
Example: on $S = (\R, +)$, the constant $f = 1/2$ satisfies the hypothesis with $\delta = 1/4$, and it is bounded by $K = (1 + \sqrt{2})/2$ but not exponential.
The result was first proved by J. Baker, J. Lawrence and F. Zorzitto in 1979 for real functions on a vector space.

## Explanations

### L1 human

Suppose a function satisfies $f(x + y) = f(x) f(y)$ up to a fixed error.
Either the function stays small everywhere, or the error is in fact zero.
A large value of $f$ would magnify any error without bound, which the fixed bound forbids.

### L2 human

For the additive Cauchy equation, approximate solutions are near exact ones but need not be exact.
The exponential equation behaves differently because it is multiplicative: an error is amplified by large values of $f$.
Similar superstability results hold for d'Alembert's equation and other multiplicative equations.
