---
tag: 0KAN330PAH
kind: definition
name: Nondegenerate bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
defines: 01NHFZF2SK
uses: [0P799D6AMN]
formal:
  - system: lean4
    library: mathlib
    decl: LinearMap.BilinForm.Nondegenerate
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Degenerate_bilinear_form
    locator: Nondegenerate forms
---

## Definition

A nondegenerate bilinear form is one for which no nonzero vector pairs to zero with every vector.
Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $B$ be a [[bilinear form|0SQZMXB6GP]] on $V$.
The *left radical* and the *right radical* of $B$ are the subspaces
$$\{u \in V : B(u, v) = 0 \text{ for all } v \in V\}, \qquad \{v \in V : B(u, v) = 0 \text{ for all } u \in V\}.$$
The form $B$ is *nondegenerate* when its left radical is $\{0\}$, that is, when for each $u \in V$,
$$B(u, v) = 0 \text{ for all } v \in V \implies u = 0.$$
A bilinear form that is not nondegenerate is *degenerate*.

## Notation

For a reflexive form, such as a symmetric or an alternating form, the two radicals agree, and we write $\operatorname{rad} B$ or $V^\perp$ for them.
Mathlib writes `B.Nondegenerate` for `B : LinearMap.BilinForm F V`.

## Remarks

The definition uses the left radical, and this looks like a choice.
In finite dimension it is not a real choice, because the [[criteria for nondegeneracy|3ND2FNJ38Y]] show that the left radical is zero exactly when the right radical is zero.
The same criteria show that $B$ is nondegenerate exactly when its matrix in one basis, and then in every basis, has nonzero determinant, and exactly when $u \mapsto B(u, \cdot)$ is an isomorphism $V \to V^*$.

The implication in the definition must hold for each $u$ separately, and its hypothesis is about all $v$ at once.
So one pair $(u, v)$ with $B(u, v) = 0$ says nothing: the dot product on $\mathbb{R}^2$ gives $(1, 0) \cdot (0, 1) = 0$ and is still nondegenerate.

For a degenerate case, take $B(x, y) = x_1 y_1$ on $\mathbb{R}^2$ and $u = (0, 1)$.
Then $B(u, v) = 0 \cdot v_1 = 0$ for every $v$, and $u \ne 0$, so $u$ lies in the left radical and $B$ is degenerate.
The finite dimension in the hypothesis matters: on an infinite-dimensional space the left radical can be zero while the right radical is not, as the criteria page shows.
The [[concept page|01NHFZF2SK]] gives more examples and the main uses.

## Explanations

### L1 human

A form is nondegenerate when it can detect every nonzero vector.
For each nonzero vector $u$, some vector $v$ must give a nonzero value $B(u, v)$.
For the dot product, $u$ itself works, since $u \cdot u > 0$.
In matrix terms, the test is that the matrix of the form has nonzero determinant.

### L2 human

Take $B(x, y) = x_1 y_2 + x_2 y_1$ on $\mathbb{Q}^2$, with matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
For $u = (u_1, u_2)$, we get $B(u, e_1) = u_2$ and $B(u, e_2) = u_1$.
If both are zero, then $u = 0$, so the left radical is $\{0\}$ and $B$ is nondegenerate.
Check: the matrix has determinant $0 - 1 = -1 \ne 0$.
Watch out: every vector $u$ on an axis has $B(u, u) = 2u_1 u_2 = 0$, but that does not make the form degenerate.
