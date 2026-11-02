---
tag: 77NG85NDQM
kind: definition
name: Multivariate approximation
msc: [41A63, 41A10]
defines: CT3PNBCYMX
uses: [03J5RAKB30, YDN0T4MEX0, 07GNX8GCYP]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Definition

Let $d \ge 2$, let $\Omega \subseteq \R^d$, and let $X$ be a [[normed space|03J5RAKB30]] of real functions on $\Omega$, such as $C(\Omega)$ for compact $\Omega$ or $L^p(\Omega)$.
Let $V_1, V_2, \dots$ be subsets of $X$, called approximating families, usually finite-dimensional subspaces or sets described by $n$ parameters.
*Multivariate approximation* is the approximation of functions $f \in X$ of the $d$ variables by elements of the families $V_n$.
Its quality is measured by the [[error of best approximation|YDN0T4MEX0]]
$$E(f, V_n) = \inf_{v \in V_n} \norm{f - v}_X.$$
The subject studies how $E(f, V_n)$ depends on $n$, on $d$ and on the smoothness of $f$.

## Remarks

Example: $\Omega = [0, 1]^d$, $X = C(\Omega)$, and $V_n$ the [[polynomials in several variables|07GNX8GCYP]] of total degree at most $n$, a space of dimension $\binom{n + d}{d}$.
By the [[Stone–Weierstrass theorem|1P8D3MK79H]], $E(f, V_n) \to 0$ for every continuous $f$.

Non-example: for $d = 1$ the same question is univariate approximation, the classical case covered by the [[Weierstrass approximation theorem|0JQE130DHW]].

A typical rate for a fixed dimension: if $f$ has bounded derivatives of order $s$ and $V_n$ has dimension $N$, the best linear methods give errors of order $N^{-s/d}$.
This rate degrades as $d$ grows.
