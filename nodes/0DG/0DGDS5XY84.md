---
tag: 0DGDS5XY84
kind: concept
name: Alternating bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
specializes: [0SQZMXB6GP, 0K6CH0MT0F]
uses: [0SQZMXB6GP, 0QK6K857HS, 0PBY4E9GQF, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Symmetric, skew-symmetric, and alternating forms
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: Skew-symmetric and alternating forms
  - book: isbn:9780387728285
    locator: Chapter 11
inventory: [JEX1WKZNKA]
---

## Summary

An alternating form is a pairing that gives zero whenever a vector meets itself, the way a signed area is zero when the two sides of a parallelogram coincide.
Such forms measure oriented areas, and the nondegenerate ones are the [[symplectic forms|PQ7JJY0VPH]] of mechanics and geometry.
Let $V$ be a vector space over a field $F$.
A [[bilinear form|0SQZMXB6GP]] $B$ on $V$ is *alternating* when
$$B(v, v) = 0 \qquad \text{for all } v \in V,$$
and it is *skew-symmetric* when $B(u, v) = -B(v, u)$ for all $u, v \in V$.
The [[formal definition|08ZQAKBKHF]] states both conditions.
Every alternating form is skew-symmetric, and the converse holds exactly when $1 + 1 \ne 0$ in $F$, that is, when the [[characteristic|1ZB13N78XW]] of $F$ is not $2$.

## Motivation

In the plane, the parallelogram with sides $u$ and $v$ has the signed area $u_1 v_2 - u_2 v_1$.
This number is linear in $u$ and in $v$, it changes sign when the two sides swap, and it is $0$ when $u = v$.
The last property is the bilinear case of the [[alternating multilinear maps|0K6CH0MT0F]] that define the determinant.

Alternating forms appear wherever signed areas do.
In classical mechanics, a state of a particle on a line is a pair $(q, p)$ of a position and a momentum.
The form $\omega\bigl((q, p), (q', p')\bigr) = q p' - p q'$ on these pairs is alternating, and the flow of Hamilton's equations keeps it.
Later in the sub-area, alternating forms get a complete classification by one number, the rank, and the nondegenerate ones give the [[symplectic vector spaces|PQ7JJY0VPH]] and the [[symplectic groups|X12FS2JAP0]].

## Notation

Books often write an alternating form as $\omega$, especially in symplectic geometry.
Its matrix in a basis is a [[skew-symmetric matrix|0PBY4E9GQF]] with zero diagonal, and some books call such a matrix alternating.
The words "antisymmetric" and "skew-symmetric" mean the same for forms.
Watch out: some books use "skew-symmetric" to mean alternating, so read the definition before you use a theorem over $\mathbb{F}_2$.

## Remarks

### A first computation

Take the [[determinant form on the plane|8K74K4BF5H]], $\omega(x, y) = x_1 y_2 - x_2 y_1$.
For $x = (2, 1)$ and $y = (1, 3)$:
$$\omega(x, y) = 2 \cdot 3 - 1 \cdot 1 = 5, \qquad \omega(y, x) = 1 \cdot 1 - 3 \cdot 2 = -5.$$
For any $x$ the two products cancel, $\omega(x, x) = x_1 x_2 - x_2 x_1 = 0$, so $\omega$ is alternating.
Its matrix is $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, with $J^{\mathsf{T}} = -J$ and a zero diagonal.

### More examples

On $F^4$ the form $x_1 y_3 + x_2 y_4 - x_3 y_1 - x_4 y_2$ is alternating, since $B(x, x) = x_1 x_3 + x_2 x_4 - x_3 x_1 - x_4 x_2 = 0$.
For two linear forms $a, b \in V^*$, the form $B(u, v) = a(u)\, b(v) - a(v)\, b(u)$ is alternating, since the two terms cancel when $u = v$.
The [[4 by 4 integer matrix of the Pfaffian example|M0JEPXXWQM]] defines an alternating form on $\mathbb{Q}^4$, and [[a symplectic basis for it|C8S4RH68S0]] is worked out.
The [[form on the rational 3-space with matrix rows (0, 1, 0), (-1, 0, 1), (0, -1, 0)|J16BA48F44]] is alternating and degenerate.

### What it is not

The [[dot product|0S52TNNTH9]] on $\mathbb{R}^n$ is not alternating, because $e_1 \cdot e_1 = 1$.
The [[form with matrix rows (1, 2) and (0, 3)|N9CJZW5596]] is neither alternating nor skew-symmetric, because $B(e_1, e_1) = 1$ and $B(e_1, e_2) = 2 \ne 0 = -B(e_2, e_1)$.
The [[identity form over the field with two elements|1V7NMPCSK9]] is the important case: $x_1 y_1 + x_2 y_2$ over $\mathbb{F}_2$ is skew-symmetric, since $-1 = 1$ there, but $B(e_1, e_1) = 1$, so it is not alternating.

### The rules you can use

The [[relation between the two notions|SX9CD5NEPD]] comes from expanding a square.
For an alternating form, $0 = B(u + v, u + v) = B(u, v) + B(v, u)$, so every alternating form is skew-symmetric.
For a skew-symmetric form, $B(v, v) = -B(v, v)$ gives $2B(v, v) = 0$, and we can divide by $2$ only when $1 + 1 \ne 0$.
The matrix test, valid in every characteristic, is $A^{\mathsf{T}} = -A$ together with $A_{ii} = 0$ for all $i$.

Orthogonality for an alternating form reads the same in both directions, since $B(v, u) = -B(u, v)$, so the form is [[reflexive|M0G958M917]].
Every vector is orthogonal to itself, so every vector is [[isotropic|MZHFGPV1YT]].
In finite dimension, the [[classification of alternating forms|V8KKHKXXB3]] says that the rank is even and that the matrix is congruent to blocks $J$ and zeros.
So an alternating form on a space of odd dimension is always degenerate, and the determinant of an alternating matrix is the square of its [[Pfaffian|NH5HWBPWS9]].

### Watch out

The two words differ in characteristic $2$.
Over $\mathbb{F}_2$ the identity matrix $I_2$ satisfies $I_2^{\mathsf{T}} = I_2 = -I_2$, so its form is skew-symmetric, but its diagonal is not zero, so its form is not alternating.
The wrong move is to test only $A^{\mathsf{T}} = -A$; the correct move is to test the diagonal as well.

A second trap: $B(v, v) = 0$ for every $v$ does not make $B$ the zero form.
The determinant form has $\omega(e_1, e_2) = 1$.

### Try it

First, is the form with matrix $\begin{pmatrix} 0 & 3 \\ -3 & 0 \end{pmatrix}$ over $\mathbb{Q}$ alternating, and what is its value on $x = (1, 2)$ and $y = (2, 1)$?
It is alternating, since the matrix is skew-symmetric with zero diagonal, and $B(x, y) = 3(x_1 y_2 - x_2 y_1) = 3(1 - 4) = -9$.

Second, over $\mathbb{F}_3$, is every skew-symmetric form alternating?
Yes, since $1 + 1 = 2 \ne 0$ in $\mathbb{F}_3$, so $2B(v, v) = 0$ gives $B(v, v) = 0$.

## Explanations

### L1 human

Two arrows in the plane span a parallelogram, and an alternating form gives its area with a sign.
For $(1, 0)$ and $(0, 1)$ the value is $1$, and in the other order it is $-1$.
An arrow paired with itself spans no area, so the value is $0$.
Swapping the arrows flips the sign, because the turn from the first arrow to the second changes direction.

### L2 human

Here is a typical check on $\mathbb{Q}^3$, for $B(x, y) = x^{\mathsf{T}} A y$ with
$$A = \begin{pmatrix} 0 & 2 & -1 \\ -2 & 0 & 3 \\ 1 & -3 & 0 \end{pmatrix}.$$
The matrix satisfies $A^{\mathsf{T}} = -A$, for example $A_{12} = 2$ and $A_{21} = -2$, and its diagonal is zero, so $B$ is alternating.
Check with $x = (1, 1, 1)$: $Ax = (1, 1, -2)$, and $x^{\mathsf{T}} A x = 1 + 1 - 2 = 0$.
The dimension $3$ is odd, so $B$ must be degenerate, and indeed $r = (3, 1, 2)$ lies in the radical:
$$A r = (0 + 2 - 2,\ -6 + 0 + 6,\ 3 - 3 + 0) = (0, 0, 0).$$
So a determinant need not be computed: the parity of the dimension already tells us that $\det A = 0$.

### L3 human

The alternating forms on $V$ are the linear forms on the exterior square $\Lambda^2 V$, and in finite dimension they are the elements of $\Lambda^2 V^*$.
A differential $2$-form on a manifold is a smooth choice of an alternating form on each tangent space, and a closed nondegenerate one is a [[symplectic structure|CAN490EPRT]].
Their classification is simpler than that of symmetric forms: over every field the rank alone decides congruence.
In characteristic $2$ the alternating forms are a proper part of the symmetric forms, and it is they, not the skew-symmetric forms, that give the symplectic groups.
