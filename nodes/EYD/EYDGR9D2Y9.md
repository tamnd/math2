---
tag: EYDGR9D2Y9
kind: definition
name: Euler–Boole summation
msc: ["65B15", "11B68", "40A25"]
defines: 141Y4NMGY7
uses: [0BE3QDH73A]
sources:
  - url: https://en.wikipedia.org/wiki/Euler–Boole_summation
---

## Definition

The *Euler polynomials* $E_k(x)$, for $k \ge 0$, are defined by the generating function
$$\frac{2 e^{xt}}{e^t + 1} = \sum_{k \ge 0} E_k(x) \frac{t^k}{k!}.$$
The *periodic Euler functions* $\widetilde{E}_k$ are the functions on $\R$ with $\widetilde{E}_k(x) = E_k(x)$ for $0 \le x < 1$ and $\widetilde{E}_k(x + 1) = -\widetilde{E}_k(x)$ for all $x$.

Let $m \ge 1$ and $n \ge 1$ be integers, let $0 \le h \le 1$, and let $f$ be a [[smooth function|0BE3QDH73A]] on an open interval that contains $[0, n]$.
*Euler–Boole summation* is the identity
$$\sum_{j=0}^{n-1} (-1)^j f(j + h) = \frac12 \sum_{k=0}^{m-1} \frac{E_k(h)}{k!} \left( (-1)^{n-1} f^{(k)}(n) + f^{(k)}(0) \right) + \frac{1}{2 (m-1)!} \int_0^n f^{(m)}(x) \, \widetilde{E}_{m-1}(h - x) \, dx,$$
and the finite sum over $k$ is the Euler–Boole expansion of the alternating sum to order $m$.

## Remarks

The first Euler polynomials are $E_0(x) = 1$ and $E_1(x) = x - \frac12$.
They satisfy $E_k(x + 1) + E_k(x) = 2x^k$, which is the source of the formula.

Example: take $f(x) = x$, $h = 0$, $n = 2$ and $m = 2$.
The left side is $0 - 1 = -1$.
The term $k = 0$ gives $\frac12 (-f(2) + f(0)) = -1$, the term $k = 1$ gives $\frac12 \cdot (-\frac12) \cdot (-f'(2) + f'(0)) = 0$, and the integral vanishes because $f'' = 0$.
Both sides equal $-1$.

Non-example: the identity is for alternating sums.
For the plain sum $\sum_{j=0}^{n-1} f(j)$ the right side is wrong in general, and the Euler–Maclaurin formula applies instead.
