---
tag: PMTK0C47E0
kind: definition
name: Quasisymmetric map
msc: [30C65, 30L10, 30C62]
defines: G215XD6D4D
uses: [063W5JMY85, 05GZ11PWRY, 0TMZ21WKCN]
sources:
  - url: https://en.wikipedia.org/wiki/Quasisymmetric_map
---

## Definition

Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]].
Let $\eta \colon [0, \infty) \to [0, \infty)$ be a [[homeomorphism|05GZ11PWRY]].
An injective map $f \colon X \to Y$ is *$\eta$-quasisymmetric* if
$$\frac{d_Y(f(x), f(a))}{d_Y(f(x), f(b))} \le \eta\!\left( \frac{d_X(x, a)}{d_X(x, b)} \right)$$
for all $x, a, b \in X$ with $b \ne x$.
The map $f$ is *quasisymmetric* if it is $\eta$-quasisymmetric for some such $\eta$.

## Remarks

Example: an $L$-bi-[[Lipschitz|0TMZ21WKCN]] map, with $L^{-1} d_X(x, y) \le d_Y(f(x), f(y)) \le L\, d_X(x, y)$, is $\eta$-quasisymmetric with $\eta(t) = L^2 t$.
Indeed the numerator is at most $L\, d_X(x, a)$ and the denominator is at least $L^{-1} d_X(x, b)$.
A similarity is quasisymmetric with $\eta(t) = t$.

Non-example: $f(x) = e^x$ on $\R$ is not quasisymmetric.
For $s > 0$ take $a = x + s$ and $b = x - s$; the ratio on the right is $1$, while the ratio on the left is $\frac{e^s - 1}{1 - e^{-s}} = e^s$.
No single value $\eta(1)$ can bound $e^s$ for all $s$.

A quasisymmetric map is a topological embedding, and its inverse on $f(X)$ is quasisymmetric too.
An increasing homeomorphism $h$ of $\R$ is quasisymmetric if and only if there is $M \ge 1$ with $\frac{1}{M} \le \frac{h(x + t) - h(x)}{h(x) - h(x - t)} \le M$ for all $x \in \R$ and $t > 0$.
