---
tag: 3HAV1FH6V9
kind: definition
name: Hypergeometric function of a matrix argument
msc: [33C70, 33C80, 62H10]
defines: DXZP6V23Z7
uses: [VDBAW9PN88, 0JV30XN73Z, 0VR671PHE5, 43VFMJCDYJ, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function_of_a_matrix_argument
---

## Definition

Let $m \ge 1$ be an integer, let $\alpha > 0$, and let $X$ be a complex $m \times m$ [[symmetric matrix|0VR671PHE5]] with [[eigenvalues|0BQAA2BK3Q]] $x_1, \dots, x_m$.
Write $\kappa \vdash k$ when $\kappa = (\kappa_1 \ge \kappa_2 \ge \dots)$ is an [[integer partition|0JV30XN73Z]] of $k$.
Let $C_\kappa^{(\alpha)}(X)$ be the Jack polynomial of $\kappa$ in $x_1, \dots, x_m$, normalised so that $\sum_{\kappa \vdash k} C_\kappa^{(\alpha)}(X) = (\operatorname{tr} X)^k$.
It is $0$ when $\kappa$ has more than $m$ nonzero parts.
For a complex number $a$, the *generalized Pochhammer symbol* is
$$(a)_\kappa^{(\alpha)} = \prod_{i \ge 1} \prod_{j = 1}^{\kappa_i} \left( a - \frac{i - 1}{\alpha} + j - 1 \right).$$
Let $a_1, \dots, a_p$ and $b_1, \dots, b_q$ be complex numbers such that $(b_l)_\kappa^{(\alpha)} \ne 0$ for every $l$ and every $\kappa$ with at most $m$ parts.
The *hypergeometric function of matrix argument* is the series
$${}_pF_q^{(\alpha)}(a_1, \dots, a_p; b_1, \dots, b_q; X) = \sum_{k = 0}^{\infty} \sum_{\kappa \vdash k} \frac{(a_1)_\kappa^{(\alpha)} \cdots (a_p)_\kappa^{(\alpha)}}{(b_1)_\kappa^{(\alpha)} \cdots (b_q)_\kappa^{(\alpha)}} \frac{C_\kappa^{(\alpha)}(X)}{k!},$$
wherever it converges.

## Remarks

For $m = 1$ there is one partition $\kappa = (k)$ of each $k$, $C_{(k)}^{(\alpha)}(x) = x^k$ and $(a)_{(k)}^{(\alpha)} = (a)_k$, so the series is the scalar [[generalized hypergeometric function|VDBAW9PN88]].
The value depends only on the eigenvalues of $X$.
For $\alpha = 2$ the polynomials $C_\kappa^{(2)}$ are the zonal polynomials of real symmetric matrices; for $\alpha = 1$ they are multiples of [[Schur polynomials|43VFMJCDYJ]], suited to complex Hermitian matrices.
Example: ${}_0F_0^{(\alpha)}(X) = \sum_k \frac{1}{k!} \sum_{\kappa \vdash k} C_\kappa^{(\alpha)}(X) = \sum_k \frac{(\operatorname{tr} X)^k}{k!} = e^{\operatorname{tr} X}$.
Non-example: for $m = 2$ and $\alpha = 1$, the choice $b_1 = 1$ is excluded, since $(1)_{(1, 1)}^{(1)} = 1 \cdot (1 - 1) = 0$ appears in a denominator, although $b_1 = 1$ is allowed in the scalar case.
