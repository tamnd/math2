---
tag: BPMRSPB6GD
kind: statement
role: theorem
name: Witt decomposition and Witt index
aliases: [witt-decomposition, witt-decomposition-theorem, witt-index]
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
about: [0AXZNE5XNH, 1X5PZSK44P, MZHFGPV1YT]
uses: [0AXZNE5XNH, 0KAN330PAH, 0F6ES3BRYP, 1X5PZSK44P, MZHFGPV1YT, SN50886T80, 43VKGAA2H7]
sources:
  - url: https://en.wikipedia.org/wiki/Witt's_theorem
    locator: Witt's decomposition theorem
  - url: https://en.wikipedia.org/wiki/Isotropic_quadratic_form
    locator: Split quadratic space
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Statement

Outside characteristic $2$, every nondegenerate symmetric form splits into hyperbolic planes and one anisotropic piece, and the number of planes and the piece are determined by the form.

Let $F$ be a field with [[characteristic|0F6ES3BRYP]] not $2$.
Let $V$ be a finite-dimensional vector space over $F$ with a [[nondegenerate|0KAN330PAH]] [[symmetric bilinear form|0AXZNE5XNH]] $B$.
Write $X \perp Y$ for a direct sum $X \oplus Y$ of subspaces with $B(x, y) = 0$ for all $x \in X$ and $y \in Y$.

1. (Existence.) $V = H_1 \perp \dots \perp H_m \perp V_{\mathrm{an}}$, where each $H_i$ is a [[hyperbolic plane|1X5PZSK44P]] and $V_{\mathrm{an}}$ is [[anisotropic|MZHFGPV1YT]]. Here $m = 0$ or $V_{\mathrm{an}} = \{0\}$ are allowed.
2. (Uniqueness.) In any two such decompositions the numbers $m$ are equal, and the anisotropic parts are isometric.
3. (Witt index.) Every maximal totally isotropic subspace of $V$ has dimension $m$. This number $m$ is the *Witt index* of $B$.
4. $2m \leq \dim V$, and $V$ is anisotropic if and only if $m = 0$.

The [[proof|Y3VNY93EXZ]] splits off hyperbolic planes for part 1 and uses [[Witt cancellation|43VKGAA2H7]] for part 2.

## Remarks

### A first decomposition

Take $B(x, y) = x_1 y_1 + x_2 y_2 - x_3 y_3 - x_4 y_4$ on $\mathbb{Q}^4$.
The vector $u_1 = e_1 + e_3$ is isotropic, since $B(u_1, u_1) = 1 - 1 = 0$.
Its partner $v_1 = \tfrac{1}{2}(e_1 - e_3)$ has
$$B(u_1, v_1) = \tfrac{1}{2}(1 + 1) = 1, \qquad B(v_1, v_1) = \tfrac{1}{4}(1 - 1) = 0,$$
so $H_1 = \operatorname{span}(e_1, e_3)$ is a hyperbolic plane.
Its complement $H_1^\perp = \operatorname{span}(e_2, e_4)$ carries $x_2 y_2 - x_4 y_4$, and the same move with $e_2 + e_4$ and $\tfrac{1}{2}(e_2 - e_4)$ makes it a second hyperbolic plane $H_2$.
So $V = H_1 \perp H_2$, the anisotropic part is $\{0\}$, and the Witt index is $2$.
Check: $\operatorname{span}(e_1 + e_3, e_2 + e_4)$ is totally isotropic of dimension $2$, since $B(e_1 + e_3, e_2 + e_4) = 0$.
A three-dimensional case is the [[decomposition of $x_1 y_1 + x_2 y_2 - x_3 y_3$|V3AVVJV8HC]].

### Why each hypothesis is needed

The characteristic must not be $2$.
Over $\mathbb{F}_2$, the plane with matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ is nondegenerate, since its determinant is $-1 = 1$.
It contains the isotropic vector $e_2$, so it is not anisotropic.
It is not a hyperbolic plane either.
In characteristic $2$ the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ gives $B(v, v) = 2 v_1 v_2 = 0$ for every $v$, while here $B(e_1, e_1) = 1$.
So this plane has no decomposition of the given shape.

Nondegeneracy is needed, because the radical of a degenerate form is neither hyperbolic nor anisotropic.
A degenerate space is the orthogonal sum of its radical and a nondegenerate part, and the theorem applies to that part.
Finite dimension is needed for the induction in the proof.

### What it gives you

The decomposition turns the classification of forms into the classification of anisotropic forms.
Two nondegenerate forms of the same dimension are isometric if and only if they have the same Witt index and isometric anisotropic parts.
The answer depends on the field in a way you can compute.
Over an algebraically closed field every form in two or more variables is isotropic, so $\dim V_{\mathrm{an}} \leq 1$ and $m = \lfloor n/2 \rfloor$.
Over $\mathbb{R}$ a form with $p$ positive and $q$ negative squares has Witt index $\min(p, q)$, and its anisotropic part is definite.
Over a finite field $\mathbb{F}_q$ with $q$ odd, every form in three or more variables is isotropic, by the [[Chevalley-Warning theorem|08895Q5W96]], so $\dim V_{\mathrm{an}} \leq 2$.

### The converse

Every orthogonal sum $H_1 \perp \dots \perp H_m \perp A$ with $A$ anisotropic is nondegenerate.
A hyperbolic plane has an invertible matrix, and a vector $v$ in the radical of $A$ has $B(v, v) = 0$, so it is $0$.
The decomposition is unique only up to isometry, not as a set of subspaces, as the three-dimensional example shows with two different hyperbolic planes.

### Generalizations

A similar decomposition holds for nondegenerate Hermitian forms.
For nondegenerate alternating forms every vector is isotropic, so $V_{\mathrm{an}} = \{0\}$, and part 1 becomes the [[classification of alternating forms|V8KKHKXXB3]].
Forms whose anisotropic parts are isometric are called Witt equivalent, and the classes form the [[Witt group|KFVY0RPGF2]] of $F$.

### Watch out

An orthogonal basis does not show the Witt index at once.
The form $\operatorname{diag}(1, 1, -1, -1)$ above has an orthogonal basis $e_1, e_2, e_3, e_4$ with no isotropic vector in it.
The hyperbolic planes appear only when you pair a $+1$ with a $-1$, as in $e_1 + e_3$.

### Try it

Find the Witt index of $x_1 y_1 + x_2 y_2 + x_3 y_3$ over $\mathbb{R}$.
The form is positive definite, so it is anisotropic and the index is $0$.

## History

Ernst Witt proved the decomposition, together with the cancellation theorem behind its uniqueness, in his paper of 1937 on quadratic forms over arbitrary fields.
The same paper introduced the ring of classes of forms that is now called the Witt ring.

## Explanations

### L1 human

A symmetric form can give zero on a nonzero vector, as $x^2 - y^2$ does on $(1, 1)$.
The theorem says that each such zero comes with a partner, and the pair spans a standard plane, the hyperbolic plane.
You can split off these planes one by one until no zero is left.
What remains is a piece where only the zero vector gives zero.
The number of planes, the Witt index, and the remaining piece do not depend on your choices.

### L2 human

Here is a typical use: compare $B_1 = \operatorname{diag}(1, -1, 1)$ and $B_2 = \operatorname{diag}(1, -1, -1)$ on $\mathbb{Q}^3$.
In $B_1$, the vector $e_1 + e_2$ is isotropic, and it splits off the hyperbolic plane $\operatorname{span}(e_1, e_2)$, leaving the line $\langle 1 \rangle$ spanned by $e_3$.
In $B_2$, the same plane splits off and leaves the line $\langle -1 \rangle$ spanned by $e_3$.
Both forms have Witt index $1$.
Their anisotropic parts $\langle 1 \rangle$ and $\langle -1 \rangle$ are not isometric over $\mathbb{Q}$, because $-1$ is not a square in $\mathbb{Q}$.
So by part 2 the two forms are not isometric.
Check with determinants: $\det B_1 = -1$ and $\det B_2 = 1$, and these differ by the factor $-1$, which is not a square.

### L3 human

The decomposition reduces the theory of quadratic forms over a field to anisotropic forms.
Over $\mathbb{Q}$ the anisotropic question is decided place by place, by the [[Hasse-Minkowski theorem|R8HCWA981S]] of number theory.
The orthogonal group of $V$ acts transitively on the maximal totally isotropic subspaces, by [[Witt's theorem|CCB8VNQCV0]], which also gives part 3 by another route.
The tensor product of forms makes the Witt group a ring, the Witt ring of $F$.
