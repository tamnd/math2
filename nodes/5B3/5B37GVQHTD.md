---
tag: 5B37GVQHTD
kind: definition
name: Affine Lie algebra
msc: [17B67, 17B65, 81R10]
defines: 9A6RGRV056
uses: [HD13X0CNBD, 38Z0HSXTCA, YJFGP89JYD, XDAXWHBNSZ, GMB9ANSTT1]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_Lie_algebra
---

## Definition

Let $A$ be an $n \times n$ [[generalized Cartan matrix|38Z0HSXTCA]].
The matrix $A$ is *of affine type* if:

1. $A$ is indecomposable, that is, no reordering of the indices brings $A$ into block diagonal form with two or more blocks;
2. there is a column vector $u \in \R^n$ with all entries positive such that $Au = 0$.

An *affine Lie algebra* is a [[Kac–Moody algebra|HD13X0CNBD]] $\mathfrak{g}(A)$ whose generalized Cartan matrix $A$ is of affine type.

## Remarks

Example: $A = \begin{pmatrix} 2 & -2 \\ -2 & 2 \end{pmatrix}$ is indecomposable, and $u = (1, 1)^T$ has positive entries with $Au = 0$.
So $\mathfrak{g}(A)$ is an affine Lie algebra, usually written $A_1^{(1)}$ or $\widehat{\mathfrak{sl}}_2$.

Non-example: $A = \begin{pmatrix} 2 & -3 \\ -3 & 2 \end{pmatrix}$ is indecomposable, but $Au = 0$ means $2u_1 = 3u_2$ and $3u_1 = 2u_2$, which forces $u = 0$.
So clause 2 fails, and $\mathfrak{g}(A)$ is not affine.

Untwisted realization: let $\mathfrak{g}$ be a finite-dimensional [[simple Lie algebra|XDAXWHBNSZ]] over $\C$ with a nonzero [[invariant symmetric bilinear form|GMB9ANSTT1]] $(\cdot \mid \cdot)$.
On $\widehat{\mathfrak{g}} = (\mathfrak{g} \otimes \C[t, t^{-1}]) \oplus \C c \oplus \C d$ define the bracket by
$$[x \otimes t^m, y \otimes t^n] = [x, y] \otimes t^{m+n} + m\, \delta_{m+n, 0}\, (x \mid y)\, c,$$
$$[d, x \otimes t^m] = m\, x \otimes t^m, \qquad [c, \widehat{\mathfrak{g}}] = 0,$$
for $x, y \in \mathfrak{g}$ and $m, n \in \Z$.
This Lie algebra is the affine Lie algebra attached to the extended Cartan matrix of $\mathfrak{g}$.
Its subspace $\mathfrak{g} \otimes \C[t, t^{-1}]$ is the [[loop algebra|YJFGP89JYD]] of $\mathfrak{g}$, but with the bracket changed by the central term.
The other affine Lie algebras, called twisted, arise in the same way from loops twisted by a diagram automorphism of $\mathfrak{g}$.
