---
tag: XNDDW5R577
kind: definition
name: Fredholm module
msc: [19K33, 58B34, 46L87]
defines: Y30V3RBNGV
uses: [M2WFY1D3SZ, M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_module
---

## Definition

Let $A$ be a [[C*-algebra|M2WFY1D3SZ]].
Let $H$ be a separable Hilbert space and $\rho \colon A \to B(H)$ a $*$-representation.
An *odd Fredholm module* over $A$ is a triple $(H, \rho, F)$ with $F \in B(H)$ such that for all $a \in A$ the operators
$$(F^2 - 1)\rho(a), \qquad (F - F^*)\rho(a), \qquad [F, \rho(a)] = F \rho(a) - \rho(a) F$$
are [[compact|M2NEP1K5AE]].
An *even Fredholm module* is such a triple together with a grading, a self-adjoint unitary $\gamma \in B(H)$, such that $\gamma \rho(a) = \rho(a) \gamma$ for all $a \in A$ and $\gamma F = -F \gamma$.

## Remarks

Example: let $A = C(\mathbb{T})$ act on $H = L^2(\mathbb{T})$ by multiplication, and let $F = 2P - 1$, where $P$ is the orthogonal projection onto the Hardy space $H^2$ spanned by $z^n$, $n \ge 0$.
Then $F$ is a self-adjoint unitary, and $[P, M_f]$ is compact for continuous $f$ (it is of finite rank for trigonometric polynomials), so this is an odd Fredholm module.
Non-example: with $A = C(\mathbb{T})$ on $L^2(\mathbb{T})$, let $F = J$ be the flip $(J f)(z) = f(\bar{z})$.
Then $F$ is a self-adjoint unitary, but $[F, M_z] = (M_{\bar{z}} - M_z) J$, and this is not compact, because multiplication by a nonzero continuous function on $L^2(\mathbb{T})$ is never compact.
The module is *degenerate* if the three operators above are zero for all $a$; degenerate modules represent zero in K-homology.
