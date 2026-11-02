---
tag: 5W1MCFBMYP
kind: definition
name: Eigenfunction of an integral operator
msc: [45C05, 47A75, 47G10]
defines: 4NSACSWRJZ
uses: [CB5G212Q03, 0N6960W0BV, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenfunction
---

## Definition

Let $a < b$, let $K \in L^2([a, b] \times [a, b])$, and let $T_K$ be the [[Hilbert–Schmidt integral operator|CB5G212Q03]] $(T_K \varphi)(x) = \int_a^b K(x, y) \varphi(y) \, dy$ on $L^2[a, b]$.
An *eigenfunction* of $T_K$ is a function $\varphi \in L^2[a, b]$, not $0$ almost everywhere, such that
$$\int_a^b K(x, y) \, \varphi(y) \, dy = \mu \, \varphi(x) \quad \text{for almost every } x \in [a, b]$$
for some $\mu \in \C$.
The number $\mu$ is the [[eigenvalue|0BQAA2BK3Q]] of $\varphi$.

## Remarks

So an eigenfunction is an [[eigenvector|0N6960W0BV]] of $T_K$ in the vector space $L^2[a, b]$.
When $\mu \ne 0$, the eigenfunctions for $\mu$ are the nonzero solutions of the homogeneous equation $\varphi = \lambda T_K \varphi$ with $\lambda = 1/\mu$.

Example: for $K(x, y) = \min(x, y)$ on $[0, 1]$ and $\varphi(x) = \sin(\pi x / 2)$, one has $\int_0^1 \min(x, y) \varphi(y) \, dy = \frac{4}{\pi^2} \varphi(x)$.
To check, call the left side $g(x)$; then $g(0) = 0$, $g'(1) = 0$ and $g'' = -\varphi$, and $\frac{4}{\pi^2} \varphi$ satisfies the same three conditions, which determine $g$.

Non-example: for the same kernel, $\varphi = 1$ is not an eigenfunction, since $\int_0^1 \min(x, y) \, dy = x - x^2/2$ is not a constant multiple of $1$.

The same definition is used with $L^2[a, b]$ replaced by $C[a, b]$ for continuous kernels, or by the $L^2$ space of a measure space.
For continuous kernels and $\mu \ne 0$, every eigenfunction in $L^2$ agrees almost everywhere with a continuous one.
