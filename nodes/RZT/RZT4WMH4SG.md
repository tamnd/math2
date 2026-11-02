---
tag: RZT4WMH4SG
kind: definition
name: Schauder basis
msc: [46B15]
defines: 528G11SDWR
uses: [0BDTTM24DP, WN6M8B3ZKB, 08P6T2WH6R, 0Z2P41SVDP, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Schauder_basis
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $X$ be a [[Banach space|0BDTTM24DP]] over $\mathbb{K}$ with norm $\norm{\cdot}$.
A sequence $(e_n)_{n \ge 1}$ in $X$ is a *Schauder basis* of $X$ if the following holds.
For every $x \in X$ there is a unique sequence $(\alpha_n)_{n \ge 1}$ in $\mathbb{K}$ such that
$$\lim_{N \to \infty} \norm{x - \sum_{n=1}^{N} \alpha_n e_n} = 0,$$
that is, the [[series|WN6M8B3ZKB]] $\sum_n \alpha_n e_n$ converges to $x$ in $X$.

## Remarks

Example: in $\ell^p$ with $1 \le p < \infty$, see [[spaces ℓ^p|08P6T2WH6R]], the unit vectors $e_n$ (with $1$ in place $n$ and $0$ elsewhere) form a Schauder basis.
For $x \in \ell^p$ and $\alpha_n = x_n$, one has $\norm{x - \sum_{n \le N} x_n e_n}_p = \left( \sum_{n > N} \abs{x_n}^p \right)^{1/p} \to 0$.
The coefficients are unique, because a norm-convergent series converges coordinatewise, so the $n$-th coordinate of $\sum_k \alpha_k e_k$ is $\alpha_n$.

Non-example: in $\ell^\infty$ the unit vectors are not a Schauder basis.
For $x = (1, 1, 1, \dots)$ the only possible coefficients are $\alpha_n = 1$, and $\norm{x - \sum_{n \le N} e_n}_\infty = 1$ for every $N$.
In fact $\ell^\infty$ has no Schauder basis at all, because it is not [[separable|0Z2P41SVDP]].

The order of the basis matters, since the series need not converge after a rearrangement.
A Schauder basis of an infinite-dimensional Banach space is never a [[Hamel basis|0VTQTPQGAV]].
The coefficient functionals $x \mapsto \alpha_n$ are always continuous.
