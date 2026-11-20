---
tag: 1X5PZSK44P
kind: concept
name: Hyperbolic plane
aliases: [hyperbolic-plane-bilinear-forms, hyperbolic-pair]
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
uses: [0AXZNE5XNH, 0P24YW565F, MZHFGPV1YT, 01NHFZF2SK, 0SPYAGE7T0]
sources:
  - url: https://en.wikipedia.org/wiki/Isotropic_quadratic_form
    locator: Hyperbolic plane
  - url: https://en.wikipedia.org/wiki/Isotropic_quadratic_form
    locator: Split quadratic space
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Summary

Let $F$ be a field, and let $H$ be a vector space of dimension $2$ over $F$ with a [[symmetric bilinear form|0AXZNE5XNH]] $B$.
$H$ is a hyperbolic plane when it has a basis $(u, v)$ with $B(u, u) = B(v, v) = 0$ and $B(u, v) = 1$, that is, when the [[matrix of $B$|0P24YW565F]] in some basis is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
Such a basis is a hyperbolic pair.
A hyperbolic plane is [[nondegenerate|01NHFZF2SK]] and [[isotropic|MZHFGPV1YT]].
When $\operatorname{char} F \neq 2$, each nondegenerate plane that contains an isotropic vector is hyperbolic, by the [[hyperbolic plane statement|SN50886T80]].
Hyperbolic planes are the building blocks of the isotropic part of every nondegenerate symmetric form, by the [[Witt decomposition|BPMRSPB6GD]].

## Motivation

An inner product space splits into orthogonal lines, each spanned by a vector of length $1$.
A form with isotropic vectors cannot split in this way along an isotropic vector $u$, because the line through $u$ is orthogonal to itself.
The smallest nondegenerate piece that contains $u$ is a plane, spanned by $u$ and a vector $v$ with $B(u, v) = 1$.
After a change of $v$, this plane has the simplest possible matrix, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
So the hyperbolic plane is the standard model of a form near an isotropic vector.

## Notation

- The hyperbolic plane is often written $\mathbb{H}$ or $H$.
- With $\operatorname{char} F \neq 2$, the basis $u + \frac12 v$, $u - \frac12 v$ gives the matrix $\operatorname{diag}(1, -1)$. So many books write the hyperbolic plane as $\langle 1 \rangle \perp \langle -1 \rangle$, or as the form $x_1 y_1 - x_2 y_2$.
- The quadratic form of a hyperbolic plane is $2 x_1 x_2$ in a hyperbolic pair, and $x_1^2 - x_2^2$ in the diagonal basis.
- For an alternating form, the plane with matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ is also called a hyperbolic plane, or a symplectic plane.

## Remarks

### Examples

- [[The form $x_1 y_1 - x_2 y_2$ on $\R^2$|X6C1Z0W252]] is a hyperbolic plane, with the hyperbolic pair $(1, 1)$, $\frac12 (1, -1)$.
- [[The form $x_1 y_1 + x_2 y_2$ on $\mathbb{F}_5^2$|QG9SC0MYDX]] is a hyperbolic plane, with the hyperbolic pair $(1, 2)$, $(3, 4)$.
- Over $\C$, the form $x_1 y_1 + x_2 y_2$ is a hyperbolic plane, since it contains the isotropic vector $(1, i)$ and is nondegenerate.
- The form $B(x, y) = x_1 y_2 + x_2 y_1$ on $F^2$ is a hyperbolic plane in the standard basis, over every field.

### Non-examples

- [[The form $x_1 y_1 + x_2 y_2$ on $\mathbb{F}_3^2$|DH7M9YDXSS]] is not a hyperbolic plane, because it is anisotropic.
- The dot product on $\R^2$ is not a hyperbolic plane, because it is positive definite.
- The form $x_1 y_1$ on $F^2$ is isotropic, but it is degenerate, so it is not a hyperbolic plane.

### Basic properties

- A hyperbolic plane has determinant $-1$ in a hyperbolic pair, so by the [[change of basis rule|0SPYAGE7T0]], $-\det A$ is a nonzero square for its matrix $A$ in every basis.
- A hyperbolic plane contains exactly two isotropic lines when $\operatorname{char} F \neq 2$: the lines through $u$ and through $v$.
- When $\operatorname{char} F \neq 2$, each isotropic vector $u$ of a nondegenerate symmetric space $V$ lies in a hyperbolic plane $H$, and $V = H \oplus H^\perp$.
- An orthogonal sum of $m$ hyperbolic planes has a totally isotropic subspace of dimension $m$, which is half the dimension.

### Common errors

- A nondegenerate plane with an isotropic vector $u$ is hyperbolic, but not every basis $(u, w)$ is a hyperbolic pair. The vector $w$ must be changed to $v = w - \frac{B(w, w)}{2} u$, after scaling $w$ so that $B(u, w) = 1$.
- In characteristic $2$, a nondegenerate symmetric plane with an isotropic vector need not be hyperbolic. Over $\mathbb{F}_2$, the matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ gives such a plane.
- The hyperbolic plane of bilinear forms is not the plane of hyperbolic geometry. Here the level set $x_1^2 - x_2^2 = 1$ of the quadratic form is a hyperbola.

## Explanations

### L1 human

A hyperbolic plane is a plane with a form that has two special directions.
Each of the two basis vectors gives $0$ with itself, and the two vectors give $1$ with each other.
The form $x_1 y_1 - x_2 y_2$ on the real plane is the standard example.
Its isotropic vectors lie on the two diagonals.

### L2 human

We show that $B(x, y) = x_1 y_1 - 3 x_2 y_2$ on $\Q^2$ is not a hyperbolic plane, but becomes one over $\Q(\sqrt 3)$.

1. $B(v, v) = v_1^2 - 3 v_2^2$. This is $0$ for $v \neq 0$ only when $3 = (v_1 / v_2)^2$ is a square.
2. $3$ is not a square in $\Q$, so $B$ is anisotropic over $\Q$, and not hyperbolic.
3. Over $\Q(\sqrt 3)$, $u = (\sqrt 3, 1)$ is isotropic: $3 - 3 = 0$.
4. Take $w = e_1$. Then $B(u, w) = \sqrt 3$, so we scale: $w' = e_1 / \sqrt 3$ gives $B(u, w') = 1$.
5. $B(w', w') = \frac13$, so $v = w' - \frac16 u = \bigl(\frac{1}{2\sqrt 3}, -\frac16\bigr)$.
6. A check: $B(v, v) = \frac{1}{12} - \frac{3}{36} = 0$ and $B(u, v) = \frac{\sqrt 3}{2\sqrt 3} + \frac{3}{6} = 1$.

The typical use is to split a hyperbolic plane off a space with an isotropic vector, and to continue on the complement.
A trap: the test "$-\det A$ is a square" uses the determinant, and here $-\det A = 3$, which is a square only over $\Q(\sqrt 3)$.

### L3 human

The hyperbolic plane is the class that is zero in the Witt group of a field: forms are compared up to added hyperbolic planes.
More generally, for any finite-dimensional space $U$, the space $U \oplus U^*$ with $B((x, \varphi), (y, \psi)) = \varphi(y) + \psi(x)$ is a hyperbolic space, an orthogonal sum of hyperbolic planes.
The alternating version gives the standard symplectic space $U \oplus U^*$.
