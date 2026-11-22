---
tag: MZHFGPV1YT
kind: concept
name: Isotropic vectors and subspaces
aliases: [isotropic-vector, anisotropic-form, totally-isotropic-subspace]
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
uses: [0SQZMXB6GP, 01TXN7ETH2, 01NHFZF2SK, 0AXZNE5XNH, 0DGDS5XY84, M2JH84VEY9]
sources:
  - url: https://en.wikipedia.org/wiki/Isotropic_quadratic_form
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Isotropic_quadratic_form
    locator: Field theory
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Summary

For the dot product, only the zero vector is orthogonal to itself.
For a general form, a nonzero vector can pair to $0$ with itself, and such vectors decide most of the structure of the form.
Let $B$ be a [[bilinear form|0SQZMXB6GP]] on a vector space $V$ over a field $F$.
A vector $v \in V$ is *isotropic* when
$$v \neq 0 \quad \text{and} \quad B(v, v) = 0,$$
that is, when $v$ is a nonzero vector [[orthogonal|01TXN7ETH2]] to itself.
The form is *isotropic* when it has an isotropic vector, and *anisotropic* when it has none.
A subspace $W$ is *totally isotropic* when $B(w, w') = 0$ for all $w, w' \in W$, which is the same as $W \subseteq W^\perp$.

## Motivation

Many proofs for inner products use the fact that $B(v, v) > 0$ for every $v \neq 0$.
For example, the line through $v$ then has an orthogonal complement that meets it only in $0$.
For the form $x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$ this fails, because $(1, 1)$ pairs to $1 - 1 = 0$ with itself, and its line is its own orthogonal complement.
So we need a name for these vectors and for the subspaces on which the form is zero.

Isotropic vectors appear in physics and in number theory.
In special relativity they are the directions of light rays, and together they make the [[light cone|JZ9ADDZX8D]] of [[Minkowski space|G49G4R1K04]].
In number theory, the question "does $a x^2 + b y^2 + c z^2 = 0$ have a solution other than $0$?" asks whether a form is isotropic.
Later in the sub-area, every isotropic vector of a nondegenerate symmetric form lies in a [[hyperbolic plane|1X5PZSK44P]], and the [[Witt decomposition|BPMRSPB6GD]] splits a form into hyperbolic planes and an anisotropic part.

## Notation

We write $q(v) = B(v, v)$ for the value of the form on the diagonal.
For a [[symmetric form|0AXZNE5XNH]], $q$ is the associated quadratic form, and $v$ is isotropic exactly when $q(v) = 0$ and $v \neq 0$.
The isotropic vectors together with $0$ make the *isotropic cone*, also called the *null cone*.
Books do not agree on the word for subspaces.
Some call $W$ isotropic when it contains one isotropic vector and totally isotropic when the form is zero on $W$, and books on symplectic geometry call $W$ isotropic when $W \subseteq W^\perp$.
Read the definition before you use a result.
For a nondegenerate symmetric form with $1 + 1 \neq 0$ in $F$, the largest dimension of a totally isotropic subspace is the *Witt index*.

## Remarks

### A first example: the two diagonals

Take $B(x, y) = x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$.
For $v = (a, b)$, factor the value on the diagonal:
$$B(v, v) = a^2 - b^2 = (a - b)(a + b).$$
So $v$ is isotropic exactly when $v \neq 0$ and $b = a$ or $b = -a$.
The isotropic vectors are the nonzero points of the two diagonal lines, as [[the form on the real plane|X6C1Z0W252]] works out in full.
Each diagonal is totally isotropic: for $u = (1, 1)$ we get $B(su, tu) = st(1 - 1) = 0$.
The form is still [[nondegenerate|01NHFZF2SK]], since its matrix $\operatorname{diag}(1, -1)$ has determinant $-1$.
So isotropic vectors can exist without any degeneracy.

### The answer depends on the field

The same formula can be anisotropic over one field and isotropic over another.
The sum of squares $x_1 y_1 + x_2 y_2 + x_3 y_3$ on $\mathbb{Q}^3$ is anisotropic, because a sum of rational squares is $0$ only when each square is $0$.
Over $\mathbb{F}_3$ the same form is isotropic, since
$$B((1, 1, 1), (1, 1, 1)) = 1 + 1 + 1 = 3 = 0,$$
and [[the sum of three squares over the field with three elements|5VMQ97B0XH]] lists all $8$ isotropic vectors.
With two squares, $x_1 y_1 + x_2 y_2$ on $\mathbb{F}_3^2$ is [[anisotropic|DH7M9YDXSS]], because $-1 = 2$ is not a square in $\mathbb{F}_3$.
Over $\mathbb{F}_5$ it is isotropic, since $1 + 2^2 = 5 = 0$.
Over $\mathbb{C}$ it is isotropic too, since $1 + i^2 = 0$ for $v = (1, i)$.
Every inner product on a real space is anisotropic, because $B(v, v) > 0$ for $v \neq 0$.

### Totally isotropic subspaces

For an [[alternating form|0DGDS5XY84]], $B(v, v) = 0$ for every $v$ by definition, so every nonzero vector is isotropic.
Then the interesting question is not whether isotropic vectors exist, but how large a totally isotropic subspace can be.

Let $V$ have finite dimension $n$, and let $B$ be nondegenerate.
If $W$ is totally isotropic, then $W \subseteq W^\perp$, and the [[dimension statement for orthogonal complements|M2JH84VEY9]] gives $\dim W^\perp = n - \dim W$.
So
$$\dim W \leq n - \dim W, \qquad \text{that is,} \qquad 2 \dim W \leq n.$$
For $x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$ the bound is $1$, and the diagonals reach it.
For a nondegenerate alternating form the bound is always reached, and the totally isotropic subspaces of dimension $n / 2$ are the [[Lagrangian subspaces|30PND47YCP]].

### The rules you can use

A nonzero vector $v$ in the radical has $B(v, w) = 0$ for every $w$, so in particular $B(v, v) = 0$.
So every degenerate form is isotropic, and every anisotropic form is nondegenerate.
The restriction of an anisotropic form to a subspace is again anisotropic, so it is nondegenerate as well.

For a symmetric form with $1 + 1 \neq 0$, the diagonal values decide the whole form on a subspace.
Expand $B(u + w, u + w)$ by bilinearity and symmetry:
$$2 B(u, w) = B(u + w, u + w) - B(u, u) - B(w, w).$$
So $W$ is totally isotropic exactly when $B(w, w) = 0$ for every $w \in W$.

Over an algebraically closed field, every symmetric form on a space of dimension $2$ or more is isotropic, because a homogeneous polynomial of degree $2$ in two or more variables has a zero other than $0$ there.
Over a finite field, every symmetric form on a space of dimension $3$ or more is isotropic.
This follows from the [[Chevalley-Warning theorem|08895Q5W96]]: the number of zeros of $q$ is divisible by the characteristic $p$, and the zero vector is one of them, so there are at least $p - 1$ others.

### Watch out

An isotropic vector need not lie in the radical.
In $x_1 y_1 - x_2 y_2$, the vector $u = (1, 1)$ is isotropic, but $B(u, (1, 0)) = 1 \neq 0$.

The isotropic cone is not a subspace in general.
In the same form, $(1, 1)$ and $(1, -1)$ are isotropic, but their sum $(2, 0)$ has $B((2, 0), (2, 0)) = 4$.

In characteristic $2$, the rule "every $w \in W$ has $B(w, w) = 0$" is weaker than "$B$ is zero on $W$".
Over $\mathbb{F}_2$ the symmetric form with matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has
$$B(v, v) = 2 v_1 v_2 = 0 \quad \text{for every } v,$$
but $B(e_1, e_2) = 1$, so $\mathbb{F}_2^2$ is not totally isotropic.

### Try it

First, decide whether $x_1 y_1 + x_2 y_2$ on $\mathbb{F}_7^2$ is isotropic.
The nonzero squares in $\mathbb{F}_7$ are $1$, $4$ and $2$, and $-1 = 6$ is not among them, so the form is anisotropic.

Second, find all isotropic vectors of $B(x, y) = x_1 y_2 + x_2 y_1$ on $\mathbb{Q}^2$.
Here $B(v, v) = 2 v_1 v_2$, so the isotropic vectors are the nonzero vectors on the two coordinate axes.

Third, show that the line through $u = (1, 1, 1)$ in $\mathbb{F}_3^3$ is totally isotropic for the sum of three squares.
For scalars $s, t$ we get $B(su, tu) = st \cdot 3 = 0$, so the form is zero on the line.

## Explanations

### L1 human

For the ordinary dot product, a vector of length zero must be the zero vector.
Other forms are different: a nonzero vector can give $0$ when you pair it with itself.
For the rule $x_1 y_1 - x_2 y_2$, the vector $(1, 1)$ gives $1 \cdot 1 - 1 \cdot 1 = 0$.
Such a vector is called isotropic.
A form with no isotropic vector is called anisotropic, and in this respect it behaves like the dot product.

### L2 human

Here is a typical problem: find the isotropic vectors of $B(x, y) = x_1 y_1 + x_2 y_2 - x_3 y_3$ on $\mathbb{R}^3$, and the largest totally isotropic subspaces.
The value on the diagonal is
$$B(v, v) = v_1^2 + v_2^2 - v_3^2,$$
so $v \neq 0$ is isotropic exactly when $v_3^2 = v_1^2 + v_2^2$.
This is a double cone around the third axis, and it contains $(1, 0, 1)$, $(0, 1, -1)$ and $(3, 4, 5)$.
Check: $9 + 16 - 25 = 0$.
The line through $(1, 0, 1)$ is totally isotropic, since $B(s(1, 0, 1), t(1, 0, 1)) = st(1 - 1) = 0$.
No plane is totally isotropic, because the form is nondegenerate and $2 \cdot 2 > 3$.
So the largest totally isotropic subspaces are the lines on the cone.
The next step in practice is to pair an isotropic vector $u$ with a vector $v$ such that $B(u, v) = 1$, which builds a hyperbolic plane.
Watch out: two isotropic vectors can add up to a vector that is not isotropic, since $(1, 0, 1) + (0, 1, -1) = (1, 1, 0)$ gives $1 + 1 - 0 = 2$.

### L3 human

For a symmetric form, the isotropic lines are the points of a projective quadric, and finding its rational points is a central question in the arithmetic of [[quadratic forms|0RBQS1JJCR]].
Over $\mathbb{Q}$, the [[Hasse-Minkowski theorem|R8HCWA981S]] says that a form is isotropic exactly when it is isotropic over $\mathbb{R}$ and over every field of $p$-adic numbers.
When $1 + 1 \neq 0$, [[Witt's theorem|CCB8VNQCV0]] shows that all maximal totally isotropic subspaces of a nondegenerate symmetric space have the same dimension, the Witt index.
For a nondegenerate alternating form, the maximal totally isotropic subspaces are the Lagrangian subspaces, and the totally isotropic subspaces organize the geometry of the [[symplectic group|X12FS2JAP0]] and of the [[orthogonal group|0TKYAEJ8N7]].
