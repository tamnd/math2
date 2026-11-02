---
tag: A18HPFPC4D
kind: definition
name: Orthogonal polynomials
msc: [42C05, 33C45]
defines: 8TXASARQN1
uses: [DYR1QFNGNJ, 1G0B73WPX8, FQTXV6BQZG]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_polynomials
---

## Definition

Let $\mu$ be a positive [[Borel measure|DYR1QFNGNJ]] on $\R$ such that:

1. every moment $\int_\R \abs{x}^k \, d\mu(x)$, $k = 0, 1, 2, \dots$, is finite;
2. the [[support|FQTXV6BQZG]] of $\mu$ is an infinite set.

A sequence $(p_n)_{n \ge 0}$ of real [[polynomials|1G0B73WPX8]] is a sequence of *orthogonal polynomials* for $\mu$ if $\deg p_n = n$ for every $n$ and
$$\int_\R p_m(x) \, p_n(x) \, d\mu(x) = 0 \quad \text{for all } m \ne n.$$

## Remarks

Condition 2 ensures that $\int p^2 \, d\mu > 0$ for every nonzero polynomial $p$, so the integral is an inner product on the polynomials.
Gram–Schmidt orthogonalization of $1, x, x^2, \dots$ then gives such a sequence, and each $p_n$ is determined up to a nonzero constant factor.
The normalization $p_n(x) = x^n + \cdots$ gives the *monic* orthogonal polynomials, and $\int p_n^2 \, d\mu = 1$ gives the *orthonormal* ones.
Often $d\mu = w(x) \, dx$ for a weight function $w \ge 0$ on an interval.

Example: $d\mu = dx$ on $[-1, 1]$ and $p_0 = 1$, $p_1 = x$, $p_2 = \frac12(3x^2 - 1)$, the first Legendre polynomials.
The integrals of $p_0 p_1 = x$ and of $p_1 p_2$ vanish because these are odd functions.
And $\int_{-1}^{1} \frac12(3x^2 - 1) \, dx = \frac12 (2 - 2) = 0$.

Non-example: the monomials $1, x, x^2$ for the same measure are not orthogonal, since $\int_{-1}^{1} 1 \cdot x^2 \, dx = \frac23 \ne 0$.
