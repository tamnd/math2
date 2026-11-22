---
tag: 01NHFZF2SK
kind: concept
name: Nondegenerate bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
specializes: [0SQZMXB6GP]
uses: [0SQZMXB6GP, 0QK6K857HS, 07JBSZE0V4, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Degenerate_bilinear_form
    locator: Nondegenerate forms
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Non-degenerate bilinear forms
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Summary

A bilinear form is nondegenerate when it sees every nonzero vector: no nonzero vector pairs to zero with the whole space.
Such a form lets you identify the space with its dual, so that every linear form becomes "pair with this vector".
Let $V$ be a finite-dimensional vector space over a field $F$, and let $B$ be a [[bilinear form|0SQZMXB6GP]] on $V$.
The *left radical* and the *right radical* of $B$ are the subspaces
$$\{u \in V : B(u, v) = 0 \text{ for all } v \in V\}, \qquad \{v \in V : B(u, v) = 0 \text{ for all } u \in V\}.$$
The form $B$ is *nondegenerate* when its left radical is $\{0\}$, as the [[formal definition|0KAN330PAH]] states.
In finite dimension this is the same as each of three other conditions: the right radical is $\{0\}$, the [[matrix|0QK6K857HS]] of $B$ is [[invertible|0EB9N0S33C]], and the map $u \mapsto B(u, \cdot)$ is an isomorphism from $V$ onto the [[dual space|07JBSZE0V4]] $V^*$.

## Motivation

The [[dot product|0S52TNNTH9]] on $\mathbb{R}^n$ never loses a vector: for $u \ne 0$ the number $u \cdot u$ is positive.
A general form can lose vectors completely.
The form $B(x, y) = x_1 y_1$ on $\mathbb{R}^2$ gives $B((0, 1), y) = 0$ for every $y$, so the vector $(0, 1)$ is invisible to it.
Such vectors carry no information about the form, and they make many theorems fail, for example the dimension formula for orthogonal complements.
The nondegenerate forms are the forms with no invisible vectors.

For these forms, each linear form $\varphi$ on $V$ is $B(u, \cdot)$ for exactly one vector $u$, as the [[Riesz representation theorem|04GYPXDXNH]] gives for an inner product.
This is why nondegeneracy is the standing hypothesis of the later pages of the sub-area: [[orthogonal complements|01TXN7ETH2]] have the right size, [[symplectic spaces|PQ7JJY0VPH]] are built on nondegenerate alternating forms, and the [[Witt decomposition|BPMRSPB6GD]] starts from a nondegenerate symmetric form.

## Notation

For a [[reflexive form|M0G958M917]], such as a symmetric or an alternating form, the two radicals are equal, and books write $\operatorname{rad} B$, $V^\perp$ or $\ker B$ for this one subspace.
Some books say *nonsingular*, *regular* or *non-degenerate* in place of nondegenerate.
For a pairing $V \times W \to F$ of two spaces, the nondegenerate case is often called a *perfect pairing*.
In Mathlib the predicate is `LinearMap.BilinForm.Nondegenerate`, and it uses the left radical.

## Remarks

### A first test

Take the form $B(x, y) = x^{\mathsf{T}} A y$ on $\mathbb{Q}^2$ with
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}.$$
Its determinant is $1 \cdot 4 - 2 \cdot 2 = 0$, so $A$ is not invertible and $B$ is degenerate.
To find the invisible vectors, note that $B(u, y) = (A^{\mathsf{T}} u)^{\mathsf{T}} y$, and this is zero for every $y$ exactly when $A^{\mathsf{T}} u = 0$.
Here $A^{\mathsf{T}} u = 0$ says $u_1 + 2u_2 = 0$, so the left radical is the line through $(2, -1)$.
Check: $B((2, -1), y) = (2 - 2) y_1 + (4 - 4) y_2 = 0$.
If you change the corner entry $4$ to $5$, the determinant becomes $1$, and the form is nondegenerate.

### Two radicals for one form

For a form that is not symmetric, the two radicals can be different subspaces.
Take $B(x, y) = x_1 y_2$ on $F^2$, with matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
The value $B(u, v) = u_1 v_2$ is zero for all $v$ exactly when $u_1 = 0$, so the left radical is the line spanned by $e_2$.
It is zero for all $u$ exactly when $v_2 = 0$, so the right radical is the line spanned by $e_1$.
The two lines differ, but both have dimension $1 = 2 - \operatorname{rank} A$.
The [[criteria for nondegeneracy|3ND2FNJ38Y]] prove that in finite dimension the two radicals always have the same dimension, $\dim V - \operatorname{rank} A$.
So it does not matter which radical the definition uses, as long as $V$ is finite-dimensional.

### Nondegenerate forms

The dot product on $F^n$ is nondegenerate, because its matrix is the identity.
The [[trace form on 2 by 2 matrices|CWKB533GHM]] is nondegenerate, because its matrix in the basis of matrix units has determinant $-1$.
The [[determinant form on the plane|8K74K4BF5H]], $B(x, y) = x_1 y_2 - x_2 y_1$, has matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ with determinant $1$, so it is nondegenerate.
The [[form x1y1 - x2y2 on the real plane|X6C1Z0W252]] is nondegenerate too, since its matrix $\operatorname{diag}(1, -1)$ has determinant $-1$.
That last form has $B((1, 1), (1, 1)) = 1 - 1 = 0$, so a nondegenerate form can still give zero on a vector paired with itself.
For a finite-dimensional $V$, the evaluation pairing $V^* \times V \to F$, $(\varphi, v) \mapsto \varphi(v)$, is a perfect pairing.

### Degenerate forms

The [[symmetric form on the rational 3-space with matrix rows (1, 1, 2), (1, 2, 3), (2, 3, 5)|RZMEYX1YJT]] is degenerate.
Its third row is the sum of the first two, so the matrix has rank $2$, and its radical is the line through $(1, 1, -1)$.
Check: the rows applied to $(1, 1, -1)$ give $1 + 1 - 2 = 0$, $1 + 2 - 3 = 0$ and $2 + 3 - 5 = 0$.
The [[alternating form on the rational 3-space|J16BA48F44]] with matrix rows $(0, 1, 0)$, $(-1, 0, 1)$ and $(0, -1, 0)$ is degenerate as well.
This is no accident: an alternating form has even rank by the [[classification of alternating forms|V8KKHKXXB3]], so on a space of odd dimension it is always degenerate, in every characteristic.

### The rules you can use

The first facts all come from the [[criteria for nondegeneracy|3ND2FNJ38Y]].
The left radical is zero exactly when the right radical is zero, exactly when the matrix is invertible, exactly when $V \to V^*$ is an isomorphism.
So the determinant of one Gram matrix decides the question, and the answer does not depend on the basis, because a change of basis multiplies the determinant by $(\det P)^2 \ne 0$.
For a nondegenerate $B$ and any subspace $W$, the [[dimension statement|M2JH84VEY9]] gives $\dim W + \dim W^\perp = \dim V$.
If $B$ is reflexive, then $B$ induces a nondegenerate form on the quotient $V / \operatorname{rad} B$, by $(u + \operatorname{rad} B, v + \operatorname{rad} B) \mapsto B(u, v)$.

### Watch out

Nondegenerate does not mean that $B(v, v) \ne 0$ for every $v \ne 0$.
That stronger condition is anisotropy, and the form $x_1 y_1 - x_2 y_2$ shows the difference: it is nondegenerate, but $(1, 1)$ pairs to zero with itself.
The correct test asks for a single $u \ne 0$ with $B(u, v) = 0$ for every $v$, not for one pair with value zero.

A second trap is the restriction to a subspace.
The same form $x_1 y_1 - x_2 y_2$ is identically zero on the line spanned by $(1, 1)$, so a nondegenerate form can restrict to a degenerate one, or even to the zero form.

A third trap is infinite dimension.
There the left and right radicals can have different sizes, and an injective map $V \to V^*$ is never surjective, since $V^*$ is then larger than $V$.
The criteria need $\dim V < \infty$.

### Try it

First, decide whether $B(x, y) = x_1 y_1 + 3x_1 y_2 + 2x_2 y_1 + 6x_2 y_2$ on $\mathbb{Q}^2$ is nondegenerate.
Its matrix has rows $(1, 3)$ and $(2, 6)$, with determinant $6 - 6 = 0$, so it is degenerate.

Second, find its left radical.
You need $A^{\mathsf{T}} u = 0$, that is $u_1 + 2u_2 = 0$ and $3u_1 + 6u_2 = 0$, so the left radical is the line through $(2, -1)$.

Third, find its right radical and compare.
You need $A v = 0$, that is $v_1 + 3v_2 = 0$, so the right radical is the line through $(3, -1)$, a different line of the same dimension.

## Explanations

### L1 human

Think of a form as a machine that takes two vectors and returns a number.
A vector is invisible to the machine if it gives zero together with every other vector.
For the form $x_1 y_1$ on the plane, the vector $(0, 1)$ is invisible, because the machine reads only first entries.
A form is nondegenerate when no nonzero vector is invisible.
The dot product is nondegenerate: the vector $(a, b)$ paired with itself gives $a^2 + b^2$, which is positive unless $a = b = 0$.

### L2 human

Here is a typical use: every linear form comes from a vector.
Let $B(x, y) = x^{\mathsf{T}} A y$ on $\mathbb{Q}^2$ with $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, and let $\varphi(y) = 3y_1 + 2y_2$.
The determinant is $2 - 1 = 1$, so $B$ is nondegenerate, and $\varphi = B(u, \cdot)$ for exactly one $u$.
Since $B(u, y) = (A^{\mathsf{T}} u)^{\mathsf{T}} y$, we need $A^{\mathsf{T}} u = (3, 2)$:
$$2u_1 + u_2 = 3, \qquad u_1 + u_2 = 2.$$
Subtract the equations to get $u_1 = 1$, and then $u_2 = 1$.
Check: $B((1, 1), y) = (2 + 1) y_1 + (1 + 1) y_2 = 3y_1 + 2y_2$.
The problem shows how a nondegenerate form turns each linear form into a vector, by solving one linear system with an invertible matrix.

### L3 human

A bilinear form on $V$ is the same as a linear map $V \to V^*$, and nondegeneracy says that this map is an isomorphism.
So a nondegenerate form is an identification of $V$ with its dual, and with it come adjoints, orthogonal complements and isometry groups such as the orthogonal and [[symplectic|PQ7JJY0VPH]] groups.
In infinite dimension the algebraic dual is too large, and analysis replaces it by the continuous dual; for a Hilbert space the Riesz theorem then makes the inner product a perfect pairing.
Over a commutative ring, injectivity of $V \to V^*$ is weaker than being an isomorphism.
The form $B(x, y) = 2xy$ on $\mathbb{Z}$ is injective in this sense, but the linear form $y \mapsto y$ is not $B(u, \cdot)$ for any integer $u$.
This is why number theory separates nondegenerate lattices from unimodular ones.
