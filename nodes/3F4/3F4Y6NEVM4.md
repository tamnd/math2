---
tag: 3F4Y6NEVM4
kind: definition
name: Regular boundary point
msc: [31B25, 31B20, 31A25]
defines: B7948M365K
uses: [R12KQGVGN6, 02BH3MCBQB, 05D5EGMFYV, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Perron_method
---

## Definition

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded [[open set|02BH3MCBQB]] with [[boundary|05D5EGMFYV]] $\partial\Omega$.
For a [[continuous function|0X3WGX95FE]] $f \colon \partial\Omega \to \R$, let $H_f$ be its [[Perron–Wiener–Brelot solution|R12KQGVGN6]].
A point $\xi \in \partial\Omega$ is a *regular boundary point* of $\Omega$ if
$$\lim_{x \to \xi, \, x \in \Omega} H_f(x) = f(\xi)$$
for every continuous function $f$ on $\partial\Omega$.
A boundary point that is not regular is *irregular*.

## Remarks

Example: if $\Omega$ is the open unit ball, every boundary point is regular, because $H_f$ is the Poisson integral of $f$, which tends to $f(\xi)$ at each $\xi$.
Non-example: for the punctured ball $\Omega = \set{0 < \abs{x} < 1}$, the point $0$ is irregular: for $f = 0$ on the sphere and $f(0) = 1$, one has $H_f = 0$, which does not tend to $1$.
Equivalently, $\xi$ is regular if and only if there is a [[barrier|ED0SZS1VED]] at $\xi$.
The Dirichlet problem on $\Omega$ has a solution continuous on $\overline{\Omega}$ for every continuous $f$ if and only if every point of $\partial\Omega$ is regular; the solution is then $H_f$.
