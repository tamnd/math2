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

Let $V$ be a finite-dimensional vector space over a field $F$, and let $B$ be a [[bilinear form|0SQZMXB6GP]] on $V$.
The left radical of $B$ is the subspace of all $u$ with $B(u, v) = 0$ for every $v \in V$, and the right radical is the subspace of all $v$ with $B(u, v) = 0$ for every $u \in V$.
$B$ is nondegenerate when its left radical is $\{0\}$.
Then the right radical is $\{0\}$ too, the [[matrix|0QK6K857HS]] of $B$ is [[invertible|0EB9N0S33C]], and $u \mapsto B(u, \cdot)$ is an isomorphism $V \to V^*$.
The [[formal definition|0KAN330PAH]] states the condition.
Nondegenerate forms matter because they identify $V$ with its [[dual space|07JBSZE0V4]], so that every linear form is a pairing with a vector.

## Motivation

The [[dot product|0S52TNNTH9]] on $\R^n$ detects every nonzero vector $u$: the value $u \cdot u$ is positive.
A general form may have nonzero vectors that it does not see at all, such as $(0, 1)$ for the form $x_1 y_1$ on $\R^2$.
Such vectors carry no information about the form, and we can divide them out.
The forms without such vectors are the nondegenerate ones.
For them, each linear form $\varphi$ is $B(u, \cdot)$ for exactly one $u$, just as the [[Riesz representation|04GYPXDXNH]] gives for an inner product.

## Notation

- The radical of a [[reflexive form|M0G958M917]] is written $\operatorname{rad} B$, $V^\perp$ or $\ker B$. For a reflexive form the left and right radicals are equal.
- Some books say "nonsingular" or "regular" for nondegenerate.
- In Mathlib the predicate is `LinearMap.BilinForm.Nondegenerate`, with the left radical.
- For a pairing $V \times W \to F$ with $\dim V = \dim W$, "perfect pairing" is a common name for the nondegenerate case.

## Remarks

### Examples

- The [[dot product|0S52TNNTH9]] on $F^n$ is nondegenerate, because its matrix is the identity matrix.
- The [[trace form on $M_2(F)$|CWKB533GHM]] is nondegenerate, because its matrix has determinant $-1$.
- The [[determinant form on $F^2$|8K74K4BF5H]] is nondegenerate, because its matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ has determinant $1$.
- The [[form $x_1 y_1 - x_2 y_2$ on $\R^2$|X6C1Z0W252]] is nondegenerate, though it has nonzero vectors with $B(v, v) = 0$.
- The evaluation pairing $V^* \times V \to F$, $(\varphi, v) \mapsto \varphi(v)$, is a perfect pairing for finite-dimensional $V$.

### Non-examples

- The [[form on $\Q^3$ with matrix $\begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 3 & 5 \end{pmatrix}$|RZMEYX1YJT]] is degenerate: its radical is the line through $(1, 1, -1)$.
- The form $x_1 y_1$ on $F^2$ is degenerate: $e_2$ is in its radical.
- The [[alternating form on $\Q^3$ with matrix $\begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}$|J16BA48F44]] is degenerate, as is every alternating form on a space of odd dimension outside characteristic $2$.

### Basic properties

- The [[criteria for nondegeneracy|3ND2FNJ38Y]]: the left radical is zero exactly when the right radical is zero, exactly when the matrix is invertible, exactly when $V \to V^*$ is an isomorphism.
- The two radicals have the same dimension, $\dim V - \rank B$.
- For a nondegenerate $B$ and a subspace $W$, $\dim W + \dim W^\perp = \dim V$, by the [[dimension statement for orthogonal complements|M2JH84VEY9]].
- A nondegenerate form may be degenerate on a subspace. The form $x_1 y_1 - x_2 y_2$ is zero on the line through $(1, 1)$.
- If $B$ is reflexive, then $B$ induces a nondegenerate form on $V / \operatorname{rad} B$.

### Common errors

- Nondegenerate does not mean "$B(v, v) \neq 0$ for $v \neq 0$". That is anisotropy, and it is stronger. The form $x_1 y_1 - x_2 y_2$ is nondegenerate and has $B((1, 1), (1, 1)) = 0$.
- In infinite dimension, the left and the right radical can differ, and an injective map $V \to V^*$ need not be surjective. The criteria need finite dimension.
- The restriction of a nondegenerate form to a subspace can be degenerate, even zero.

## Explanations

### L1 human

A form is nondegenerate when it can see every nonzero vector.
This means: for each nonzero vector $u$, some vector $v$ gives a nonzero value $B(u, v)$.
For the form $x_1 y_1$ on the plane, the vector $(0, 1)$ is invisible, since it gives $0$ with everything.
So that form is degenerate.
The dot product sees every vector, so it is nondegenerate.

### L2 human

We test $B(x, y) = x^T A y$ on $\Q^2$ with $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.

1. $\det A = 4 - 4 = 0$, so $B$ is degenerate.
2. The left radical is the null space of $A^T$, since $B(u, v) = (A^T x)^T y$ is zero for all $y$ exactly when $A^T x = 0$.
3. $A^T x = 0$ means $x_1 + 2x_2 = 0$. So the radical is the line through $(2, -1)$.
4. A check: $B((2, -1), y) = (2 - 2)y_1 + (4 - 4)y_2 = 0$.

The typical use is to identify $V$ with $V^*$, and to get $\dim W^\perp = \dim V - \dim W$.
A trap: a vector $v \neq 0$ with $B(v, v) = 0$ does not make the form degenerate.
Only a vector orthogonal to all vectors does.

### L3 human

A bilinear form is a map $V \to V^*$, and nondegeneracy says that this map is an isomorphism.
So a nondegenerate form is the same as an identification of $V$ with its dual, and it gives adjoints, orthogonal complements and isometry groups.
In infinite dimension the condition splits: an inner product on a Hilbert space gives an injective map into the dual, and the Riesz theorem is needed for surjectivity.
In commutative algebra a pairing of modules is perfect when both maps to the duals are isomorphisms, which is stronger than injectivity, as the form $2xy$ on $\mathbb{Z}$ shows.
