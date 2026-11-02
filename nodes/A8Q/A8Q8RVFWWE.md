---
tag: A8Q8RVFWWE
kind: definition
name: Nijenhuis tensor
msc: [53C15, 32Q60]
defines: T46ZBWDPHQ
uses: [F45VQ47GPV, WX302T93TW, 68FGQEBD6J, 9SYWRGVTRS, D46QECMC10]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_complex_manifold
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]].
Let $J \colon TM \to TM$ be a smooth [[tensor field|WX302T93TW]] of type $(1,1)$, that is, a smooth field of linear endomorphisms of the tangent spaces.
Let $[\cdot, \cdot]$ be the [[Lie bracket of vector fields|68FGQEBD6J]].
The *Nijenhuis tensor* of $J$ is the map $N_J$ that sends vector fields $X, Y$ to the vector field
$$N_J(X, Y) = [JX, JY] - J[JX, Y] - J[X, JY] + J^2 [X, Y].$$

## Remarks

The map $N_J$ is $C^\infty(M)$-bilinear and antisymmetric, so it is a tensor field of type $(1,2)$, a $2$-form with values in $TM$.
It equals $\frac{1}{2}[J, J]$, where $[J, J]$ is the [[Frölicher–Nijenhuis bracket|D46QECMC10]] of $J$ with itself.
For an [[almost complex structure|9SYWRGVTRS]], where $J^2 = -\id$, the formula reads $N_J(X, Y) = [JX, JY] - J[JX, Y] - J[X, JY] - [X, Y]$.
Some authors use a different constant factor.

Example: on $\R^2$ let $J \partial_x = \partial_y$ and $J \partial_y = -\partial_x$.
For $X, Y$ among $\partial_x, \partial_y$, all of $X, Y, JX, JY$ are constant combinations of $\partial_x$ and $\partial_y$, so all brackets vanish.
By bilinearity over functions, $N_J = 0$.
More generally, for an almost complex structure one has $N_J(JX, Y) = -J N_J(X, Y)$, so $N_J(JX, X) = 0$; on a $2$-manifold $X$ and $JX$ span each tangent space where $X \ne 0$, hence $N_J = 0$ on every surface.

Non-example: the expression $[JX, JY] - [X, Y]$ alone is not a tensor.
Replacing $X$ by $fX$ for a function $f$ gives $f([JX, JY] - [X, Y]) - (JY)(f)\, JX + Y(f)\, X$, since $[fA, B] = f[A, B] - B(f) A$.
The last two terms are not zero in general, so the expression is not $C^\infty(M)$-linear in $X$; the two middle terms of $N_J$ cancel them.
