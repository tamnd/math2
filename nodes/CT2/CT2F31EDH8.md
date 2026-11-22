---
tag: CT2F31EDH8
kind: concept
name: Complexification and realification
aliases: [complexification, realification, linear-complex-structure]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: grad
uses: [000AYPA9AJ, 05G2G0P224, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Complexification
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Linear_complex_structure
    locator: Definition
  - book: isbn:9780387728285
    locator: Chapter 1
same_as:
  wikipedia: Complexification
---

## Summary

Complexification lets a real vector space use complex scalars, and realification lets a complex space forget them.
The first keeps the dimension and the second doubles it, and together they let real and complex linear algebra borrow from each other.
For a real [[vector space|000AYPA9AJ]] $V$, the *complexification* is the set $V_\mathbb{C} = V \times V$, with the pair $(u, w)$ written $u + iw$, with entrywise addition and with
$$(a + bi)(u + iw) = (au - bw) + i(aw + bu) \qquad (a, b \in \mathbb{R}).$$
It is a complex vector space with $\dim_\mathbb{C} V_\mathbb{C} = \dim_\mathbb{R} V$.
For a complex space $W$, the *realification* $W_\mathbb{R}$ is the same set with the scalars restricted to $\mathbb{R}$, and $\dim_\mathbb{R} W_\mathbb{R} = 2 \dim_\mathbb{C} W$.
A *complex structure* on a real space $V$ is a real linear map $J \colon V \to V$ with $J^2 = -I$, and it makes $V$ a complex space by the rule $(a + bi)v = av + bJv$.

## Motivation

A real matrix can have complex eigenvalues.
The rotation $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ of the plane has eigenvalues $\pm i$, and its eigenvectors cannot live in $\mathbb{R}^2$, since no real line is fixed by a quarter turn.
Complexification gives them a home, $(\mathbb{R}^2)_\mathbb{C} = \mathbb{C}^2$, in which $R$ still acts.
Many proofs about real matrices, such as the real spectral theorem and the real Jordan form, go through the complex space and come back.

Realification runs the other way.
It is how one sees $\mathbb{C}^n$ as $\mathbb{R}^{2n}$, which is needed whenever complex numbers meet geometry, as in the study of holomorphic maps as maps of the plane.
A complex structure $J$ records exactly the extra data that turns a real space back into a complex one: it says what multiplication by $i$ should be.

## Notation

Books write $V_\mathbb{C}$, $V^\mathbb{C}$ or $V \otimes_\mathbb{R} \mathbb{C}$ for the complexification.
The [[tensor product|0BF2DE2SYK]] form $V \otimes_\mathbb{R} \mathbb{C}$ is the definition in many books and in Mathlib, and it is isomorphic to $V \times V$ with the rule above, by $v \otimes (a + bi) \mapsto (av, bv)$.
The realification is written $W_\mathbb{R}$, or $W$ itself when the field is clear, and it is also called *restriction of scalars*.

## Remarks

### First computations

For $V = \mathbb{R}^n$, the pair $(u, w)$ of real vectors is the complex vector $u + iw$, so $(\mathbb{R}^n)_\mathbb{C} = \mathbb{C}^n$.
In the same way $(M_n(\mathbb{R}))_\mathbb{C} = M_n(\mathbb{C})$ and $(\mathbb{R}[x])_\mathbb{C} = \mathbb{C}[x]$.
The rule for scalars is the rule for multiplying complex numbers.
For instance, $i$ times $i$ should be $-1$, and indeed
$$i \bigl(i(u + iw)\bigr) = i(-w + iu) = -u - iw = (-1)(u + iw).$$

For realification, $\mathbb{C}$ as a real space is $\mathbb{R}^2$ with basis $1, i$.
Multiplication by $i$ sends $x + iy$ to $-y + ix$, so it is the real map $J(x, y) = (-y, x)$, and $J^2(x, y) = J(-y, x) = (-x, -y)$, so $J^2 = -I$.
More generally, $\mathbb{C}^n$ as a real space is $\mathbb{R}^{2n}$, with basis $e_1, ie_1, \dots, e_n, ie_n$.

### Dimensions

If $b_1, \dots, b_n$ is a [[basis|0VTQTPQGAV]] of $V$ over $\mathbb{R}$, then $b_1 + i0, \dots, b_n + i0$ is a basis of $V_\mathbb{C}$ over $\mathbb{C}$.
A vector $u + iw$ with $u = \sum x_k b_k$ and $w = \sum y_k b_k$ equals $\sum (x_k + iy_k) b_k$, and these complex coefficients are unique, so $\dim_\mathbb{C} V_\mathbb{C} = \dim_\mathbb{R} V$.
If $w_1, \dots, w_m$ is a basis of $W$ over $\mathbb{C}$, then $w_1, iw_1, \dots, w_m, iw_m$ is a basis of $W_\mathbb{R}$, because $(x + iy)w_k = x w_k + y(iw_k)$, so $\dim_\mathbb{R} W_\mathbb{R} = 2 \dim_\mathbb{C} W$.

A real linear map $T$ extends to $T_\mathbb{C}(u + iw) = Tu + iTw$, and in the basis above $T_\mathbb{C}$ has the same matrix as $T$.
That is how a real matrix acts on $\mathbb{C}^n$.

### What it is not

A map with $J^2 = I$ gives no complex structure.
For the swap $J(x, y) = (y, x)$ on $\mathbb{R}^2$ and the rule $(a + bi)v = av + bJv$, we get $i(i(1, 0)) = J(J(1, 0)) = (1, 0)$, while $(i \cdot i)(1, 0) = (-1, 0)$, so axiom 5 fails.

Some real spaces have no complex structure at all.
On $\mathbb{R}^3$, a map with $J^2 = -I$ would give $\det(J)^2 = \det(-I) = (-1)^3 = -1$, which no real number satisfies.
The same argument shows that a finite-dimensional real space with a complex structure has even dimension, and every even-dimensional space has one, built from blocks like the $J$ above.

### Watch out

The space $V_\mathbb{C}$ is bigger than $V$ as a real space: for $V = \mathbb{R}^2$, the space $\mathbb{C}^2$ has real dimension $4$, since $(V_\mathbb{C})_\mathbb{R} \cong V \oplus V$.
So always say over which field a dimension is taken: $\dim_\mathbb{C} \mathbb{C}^n = n$, but $\dim_\mathbb{R} \mathbb{C}^n = 2n$.
Complexifying a realification does not give back the space either, because $(W_\mathbb{R})_\mathbb{C}$ has complex dimension $2 \dim_\mathbb{C} W$.

### History

Hamilton defined the complex numbers as pairs of real numbers in the 1830s.
The complexification $V \times V$ applies the same construction to a whole real vector space.

### Try it

First, what is $(2 + i)(u + iw)$ in $V_\mathbb{C}$?
By the rule with $a = 2$ and $b = 1$, it is $(2u - w) + i(2w + u)$.

Second, does $\mathbb{R}^4$ have a complex structure?
Yes: take $J(x_1, x_2, x_3, x_4) = (-x_2, x_1, -x_4, x_3)$, which applies the quarter turn to each pair of coordinates, so $J^2 = -I$.

## Explanations

### L1 human

Complexification lets a real space use complex numbers as scalars.
It pairs two real vectors as a real part and an imaginary part, just as $3 + 4i$ pairs the real numbers $3$ and $4$.
Realification does the opposite: it forgets the complex scalars and keeps only the real ones.
Then the complex line $\mathbb{C}$ becomes the real plane, so the dimension doubles from $1$ to $2$.

### L2 human

Here is a typical use: find the eigenvectors of the quarter turn $R(x, y) = (-y, x)$ on $\mathbb{R}^2$.
Over $\mathbb{R}$ there are none, since $R$ moves every nonzero vector off its own line.
In $(\mathbb{R}^2)_\mathbb{C} = \mathbb{C}^2$, try the vector $(1, -i)$ and apply $R_\mathbb{C}$, which uses the same matrix:
$$R_\mathbb{C}(1, -i) = (i, 1) = i(1, -i),$$
since $i \cdot (-i) = 1$.
So $(1, -i)$ is an eigenvector with eigenvalue $i$, and its conjugate $(1, i)$ is an eigenvector with eigenvalue $-i$.
The real and imaginary parts of $(1, -i)$ are $(1, 0)$ and $(0, -1)$, and in that real basis $R$ acts as a rotation block; this is how the real canonical forms are built.

### L3 human

A complex structure $J$ on $\mathbb{R}^{2n}$ is the same as an identification $\mathbb{R}^{2n} \cong \mathbb{C}^n$, and the set of all such $J$ is the homogeneous space $\mathrm{GL}_{2n}(\mathbb{R}) / \mathrm{GL}_n(\mathbb{C})$.
On $V_\mathbb{C}$, the map $u + iw \mapsto u - iw$ is a conjugate-linear involution whose fixed points form $V$, and a complex space with such a real structure is the complexification of its fixed space.
Complexification is extension of scalars along $\mathbb{R} \subset \mathbb{C}$, and realification is restriction of scalars; the two are adjoint functors, a pattern that returns for modules and for [[tensor products|0BF2DE2SYK]] in general.
