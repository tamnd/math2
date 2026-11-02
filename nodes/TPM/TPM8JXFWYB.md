---
tag: TPM8JXFWYB
kind: definition
name: Romberg's method
msc: [65D30, 65B05, 41A55]
defines: VP40T7MHGM
uses: [FH0538XCZR, WMTZG71K2Y]
sources:
  - url: https://en.wikipedia.org/wiki/Romberg%27s_method
---

## Definition

Let $a < b$ be real numbers and let $f$ be a continuous function on $[a, b]$.
For $n \ge 0$ let $h_n = (b - a)/2^n$, and let $R(n, 0)$ be the composite [[trapezoidal rule|FH0538XCZR]] with $2^n$ subintervals:
$$R(n, 0) = h_n \Big( \tfrac12 f(a) + \sum_{k=1}^{2^n - 1} f(a + k h_n) + \tfrac12 f(b) \Big).$$
For $1 \le m \le n$ define
$$R(n, m) = R(n, m - 1) + \frac{R(n, m - 1) - R(n - 1, m - 1)}{4^m - 1}.$$
*Romberg's method* approximates $\int_a^b f(x)\,dx$ by the entries of the triangular table $R(n, m)$, usually by the diagonal entry $R(n, n)$.

## Remarks

Each column is a [[Richardson extrapolation|WMTZG71K2Y]] of the previous one, which removes the term $h^{2m}$ from the error expansion.
If $f$ is smooth enough, the error of $R(n, m)$ is $O(h_n^{2m + 2})$ as $n \to \infty$.
The values $R(n, 0)$ can be computed recursively: $R(n, 0) = \frac12 R(n - 1, 0) + h_n \sum_{k=1}^{2^{n-1}} f(a + (2k - 1) h_n)$, so no function value is computed twice.

Example: $f(x) = x^2$ on $[0, 1]$.
Then $R(0, 0) = \frac12 (0 + 1) = \frac12$ and $R(1, 0) = \frac12 \big( \frac12 \cdot 0 + \frac14 + \frac12 \cdot 1 \big) = \frac38$.
So $R(1, 1) = \frac38 + \frac{3/8 - 1/2}{3} = \frac13$, which is the exact integral, as Simpson's rule is exact for quadratics.

Non-example: replacing $4^m - 1$ by $2^m - 1$ gives a different table that does not cancel the even powers of $h$, so it is not Romberg's method.
