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

The hyperbolic plane is the simplest space with a nondegenerate form and an isotropic vector, and every isotropic vector of a nondegenerate symmetric space sits inside one.
So it plays the role for isotropic forms that a line spanned by a unit vector plays for inner products.
Let $F$ be a field, and let $H$ be a vector space of dimension $2$ over $F$ with a [[symmetric bilinear form|0AXZNE5XNH]] $B$.
Then $H$ is a *hyperbolic plane* when it has a basis $(u, v)$ with
$$B(u, u) = 0, \qquad B(v, v) = 0, \qquad B(u, v) = 1,$$
that is, when the [[matrix of $B$|0P24YW565F]] in some basis is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
Such a basis is a *hyperbolic pair*.
A hyperbolic plane is [[nondegenerate|01NHFZF2SK]], since this matrix has determinant $-1$, and it is [[isotropic|MZHFGPV1YT]], since $u$ is an isotropic vector.

## Motivation

An inner product space splits into orthogonal lines, each spanned by a vector $e$ with $B(e, e) = 1$.
A form with an isotropic vector $u$ cannot split off the line through $u$, because that line is orthogonal to itself.
The smallest nondegenerate piece that contains $u$ is a plane, spanned by $u$ and a vector $v$ that pairs with $u$.
After a correction of $v$, this plane has the simplest possible matrix, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

This is how the hyperbolic plane enters the theory.
The [[statement on isotropic vectors|SN50886T80]] splits a hyperbolic plane off any nondegenerate symmetric space that contains an isotropic vector, when $1 + 1 \neq 0$ in $F$.
Repeating the step gives the [[Witt decomposition|BPMRSPB6GD]] into hyperbolic planes and an anisotropic part.
The name comes from the real case, where the level set $x_1^2 - x_2^2 = 1$ of the diagonal form is a hyperbola.

## Notation

Books write the hyperbolic plane as $\mathbb{H}$, $H$ or $H(F)$.
When $1 + 1 \neq 0$, many books write it as $\langle 1, -1 \rangle$ or $\langle 1 \rangle \perp \langle -1 \rangle$, because it has a diagonal basis with the values $1$ and $-1$, as shown below.
Its quadratic form is $2 x_1 x_2$ in a hyperbolic pair and $x_1^2 - x_2^2$ in the diagonal basis.
For an [[alternating form|0DGDS5XY84]], the plane with matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ is also called a hyperbolic plane, or a symplectic plane, so check which kind of form a book means.

## Remarks

### A first hyperbolic plane

Take $B(x, y) = x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$.
The vectors $u = (1, 1)$ and $v = \tfrac{1}{2}(1, -1)$ give
$$B(u, u) = 1 - 1 = 0, \qquad B(v, v) = \tfrac{1}{4}(1 - 1) = 0, \qquad B(u, v) = \tfrac{1}{2}(1 + 1) = 1,$$
so $(u, v)$ is a hyperbolic pair, as [[the form on the real plane|X6C1Z0W252]] checks with the matrix $P^{\mathsf{T}} A P$.

We can also go the other way, from a hyperbolic pair to a diagonal basis, when $1 + 1 \neq 0$.
Expand by bilinearity, using $B(u, u) = B(v, v) = 0$ and $B(u, v) = B(v, u) = 1$:
$$B(u + \tfrac{1}{2} v, u + \tfrac{1}{2} v) = 1, \qquad B(u - \tfrac{1}{2} v, u - \tfrac{1}{2} v) = -1, \qquad B(u + \tfrac{1}{2} v, u - \tfrac{1}{2} v) = -\tfrac{1}{2} + \tfrac{1}{2} = 0.$$
So every hyperbolic plane has the diagonal matrix $\operatorname{diag}(1, -1)$ in a suitable basis, and $x_1 y_1 - x_2 y_2$ is the model over every field with $1 + 1 \neq 0$.

### How to recognize a hyperbolic plane

Let $1 + 1 \neq 0$ in $F$, and let $B$ be a nondegenerate symmetric form on a plane.
Then $B$ is a hyperbolic plane exactly when it has an isotropic vector, by the [[statement on isotropic vectors|SN50886T80]].

There is also a test by the determinant.
Diagonalize $B$ as $\operatorname{diag}(a, b)$ with $a, b \neq 0$.
The form $a x^2 + b y^2$ has a zero other than $0$ exactly when $-b/a$ is a square, which is the same as $-ab = -b/a \cdot a^2$ being a square.
By the [[change of basis rule|0SPYAGE7T0]], the determinant of the matrix $A$ changes only by the square factor $(\det P)^2$.
So the plane is hyperbolic exactly when $-\det A$ is a nonzero square in $F$.

For example, $x_1 y_1 + x_2 y_2$ over $\mathbb{F}_5$ has $-\det A = -1 = 4 = 2^2$, so it is a hyperbolic plane, and [[the pair over the field with five elements|QG9SC0MYDX]] finds the pair $(1, 2)$, $(3, 4)$.
Over $\mathbb{C}$ every nonzero number is a square, so every nondegenerate symmetric plane is hyperbolic.
The form $x_1 y_2 + x_2 y_1$ on $F^2$ is a hyperbolic plane in the standard basis, over every field, by the definition.

### What it is not

The form $x_1 y_1 + x_2 y_2$ on $\mathbb{F}_3^2$ is [[not a hyperbolic plane|DH7M9YDXSS]], because it has no isotropic vector: here $-\det A = -1 = 2$ is not a square in $\mathbb{F}_3$.
The dot product on $\mathbb{R}^2$ fails for the same reason, since it is positive definite and $-\det A = -1 < 0$.
The form $x_1 y_1$ on $F^2$ has the isotropic vector $e_2$, but it is degenerate, because $e_2$ pairs to $0$ with every vector.
So it is not a hyperbolic plane either.

### The rules you can use

When $1 + 1 \neq 0$, a hyperbolic plane contains exactly two isotropic lines, the lines through $u$ and through $v$.
The reason is one line of algebra:
$$B(su + tv, su + tv) = 2st,$$
which is $0$ exactly when $s = 0$ or $t = 0$.

A hyperbolic plane $H$ inside a larger finite-dimensional space $V$ always splits off.
Its form is nondegenerate, so $V = H \oplus H^\perp$ by the [[dimension statement for orthogonal complements|M2JH84VEY9]].

An orthogonal sum of $m$ hyperbolic planes with pairs $(u_i, v_i)$ has the totally isotropic subspace spanned by $u_1, \dots, u_m$.
Its dimension $m$ is half the dimension of the space, which is the largest possible for a nondegenerate form.

### Watch out

A nondegenerate plane with an isotropic vector $u$ is hyperbolic, but not every basis $(u, w)$ is a hyperbolic pair.
First scale $w$ so that $B(u, w) = 1$, and then replace $w$ by $v = w - \tfrac{1}{2} B(w, w)\, u$.

In characteristic $2$, a nondegenerate symmetric plane with an isotropic vector need not be hyperbolic.
Over $\mathbb{F}_2$, take the matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$, which has determinant $1$, so the form is nondegenerate, and $e_2$ is isotropic.
In a hyperbolic plane every vector has $B(w, w) = 2st = 0$, but here $B(e_1, e_1) = 1$.
So no basis gives the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

The hyperbolic plane of bilinear forms is not the plane of hyperbolic geometry.
The name refers only to the hyperbola $x_1^2 - x_2^2 = 1$.

### History

Witt's paper of 1937 on quadratic forms over arbitrary fields proved the cancellation theorem and built the Witt ring of a field.
In that ring, a sum of hyperbolic planes counts as zero.

### Try it

First, decide whether $x_1 y_1 + x_2 y_2$ over $\mathbb{F}_{13}$ is a hyperbolic plane.
Here $-\det A = -1 = 12 = 5^2$, so it is, and $(1, 5)$ is isotropic, since $1 + 25 = 26 = 0$.

Second, decide whether the form on $\mathbb{Q}^2$ with matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ is a hyperbolic plane.
Its determinant is $1 - 4 = -3$, and $-\det A = 3$ is not a square in $\mathbb{Q}$, so it is not; over $\mathbb{R}$ it is.

Third, find a hyperbolic pair for the form on $\mathbb{Q}^2$ with matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
Take $u = e_2$ and $z = e_1$, so $B(u, z) = 1$ and $B(z, z) = 1$; then $v = e_1 - \tfrac{1}{2} e_2$ has $B(v, v) = 1 - 1 + 0 = 0$ and $B(u, v) = 1$.

## Explanations

### L1 human

A hyperbolic plane is a plane with a form that has two special directions.
Each special vector pairs to $0$ with itself, and the two vectors pair to $1$ with each other.
The rule $x_1 y_1 - x_2 y_2$ on the real plane is the standard example.
There the special directions are the two diagonals: $(1, 1)$ gives $1 - 1 = 0$, and so does $(1, -1)$.

### L2 human

Here is a typical problem: the form $B(x, y) = x_1 y_1 - 3 x_2 y_2$ is not a hyperbolic plane over $\mathbb{Q}$, but it becomes one over $\mathbb{Q}(\sqrt{3})$.
The value on the diagonal is $B(v, v) = v_1^2 - 3 v_2^2$.
For $v \neq 0$ this is $0$ only when $v_2 \neq 0$ and $(v_1 / v_2)^2 = 3$, and $3$ is not a square in $\mathbb{Q}$.
So over $\mathbb{Q}$ the form is anisotropic and not hyperbolic.
Over $\mathbb{Q}(\sqrt{3})$ the vector $u = (\sqrt{3}, 1)$ is isotropic, since $3 - 3 = 0$.
Take $w = e_1 / \sqrt{3}$, so that $B(u, w) = 1$ and $B(w, w) = \tfrac{1}{3}$, and correct it:
$$v = w - \tfrac{1}{6} u = \left( \frac{1}{2\sqrt{3}}, -\frac{1}{6} \right).$$
Check: $B(v, v) = \tfrac{1}{12} - \tfrac{3}{36} = 0$ and $B(u, v) = \tfrac{1}{2} + \tfrac{1}{2} = 1$.
This shows the typical use: split a hyperbolic plane off a space with an isotropic vector, and continue on the complement.
Watch out: the determinant test agrees, since $-\det A = 3$, which is a square in $\mathbb{Q}(\sqrt{3})$ but not in $\mathbb{Q}$.

### L3 human

In the [[Witt group|KFVY0RPGF2]] of a field with $1 + 1 \neq 0$, forms are compared up to added hyperbolic planes, so the hyperbolic plane is the zero class.
More generally, for a finite-dimensional space $U$, the space $U \oplus U^*$ with the form
$$B((x, \varphi), (y, \psi)) = \varphi(y) + \psi(x)$$
is a hyperbolic space: a basis of $U$ and its dual basis give an orthogonal sum of $\dim U$ hyperbolic planes.
The form $\varphi(y) - \psi(x)$ on the same space is alternating, and it gives the standard [[symplectic vector space|PQ7JJY0VPH]].
In characteristic $2$ the right object is a quadratic form, and the hyperbolic plane is the quadratic form $x_1 x_2$.
