---
tag: MZFRXECCMC
kind: concept
name: Discriminant of a quadratic form
msc: ["11E04", 15A63]
topics: [6TSCEW8QMK]
audience: ug2
aliases: [discriminant-of-a-quadratic-form]
uses: [0RBQS1JJCR, VN9AG8JKYT, 9160DW40TE, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
  - url: https://en.wikipedia.org/wiki/Square_class
  - url: https://en.wikipedia.org/wiki/Binary_quadratic_form
---

## Summary

The discriminant is the determinant of the matrix of a quadratic form, kept only up to multiplication by nonzero squares.
It is the first invariant after the dimension, and it gives a one-line test that two forms are not equivalent.
Let $F$ be a field of characteristic not $2$, and let $Q$ be a [[quadratic form|0RBQS1JJCR]] on a vector space $V$ of finite dimension $n$ over $F$.
Let $A$ be the symmetric matrix of $Q$ in some basis, as in [[the correspondence theorem|VN9AG8JKYT]].
The *discriminant* of $Q$ is $0$ when $\det A = 0$, and otherwise it is the [[square class|9160DW40TE]] of the [[determinant|00KDZRW4C0]] $\det A$:
$$\operatorname{disc} Q = \det A \cdot F^{\times 2} \in F^\times / F^{\times 2}.$$
By [[the invariance theorem|WYQGZK8GFT]], the result does not depend on the basis, and equivalent forms have the same discriminant.

## Motivation

When the basis changes by an invertible matrix $P$, the matrix of $Q$ becomes $P^{\mathsf{T}} A P$, and its determinant becomes $\det(P)^2 \det A$.
So the number $\det A$ is not an invariant, but its class modulo nonzero squares is.
That class is a cheap test of equivalence.
For example, over $\mathbb{Q}$ the forms $x^2 + y^2$ and $x^2 + 2y^2$ have determinants $1$ and $2$, and $2$ is not the square of a rational number, so the forms are not equivalent.

The test is sharpest over finite fields.
There the dimension and the discriminant together classify all nondegenerate forms, by [[the finite field theorem|2HBR7137AD]].
Over $\mathbb{R}$ the discriminant is only the sign $(-1)^q$, and the [[signature|07EZA80NEH]] carries more information.
Over $\mathbb{Q}$ and the $p$-adic fields the discriminant is one of several invariants in the theory of [[quadratic forms over local and global fields|NQC5CJZY4J]].

## Notation

Books write $\operatorname{disc} Q$, $d(Q)$ or $d_Q$, and some write a representative $d \in F^\times$ and say "up to squares".
Some books use the *signed discriminant* $(-1)^{n(n-1)/2} \det A$, chosen so that the [[hyperbolic plane|1X5PZSK44P]] has signed discriminant $1$, and call it the discriminant.
Number theory uses a third convention for a binary form $a x^2 + b xy + c y^2$: the number $b^2 - 4ac$ itself, with no division by squares; see [[binary quadratic forms|SBDSYA037Q]].
The matrix of that form has off-diagonal entries $b/2$, so the two conventions are related by
$$\det \begin{pmatrix} a & b/2 \\ b/2 & c \end{pmatrix} = ac - \frac{b^2}{4} = -\frac{1}{4} \left( b^2 - 4ac \right).$$
Since $\tfrac14$ is a square, the class of $\det A$ is the class of $-(b^2 - 4ac)$: the conventions differ by a sign modulo squares.

## Remarks

### A first computation

Take $Q = x^2 + xy + y^2$ over $\mathbb{Q}$.
The cross term $xy$ splits into two halves, so the matrix and its determinant are
$$A = \begin{pmatrix} 1 & \tfrac12 \\ \tfrac12 & 1 \end{pmatrix}, \qquad \det A = 1 - \frac14 = \frac34 = 3 \cdot \left( \frac12 \right)^2.$$
So $\operatorname{disc} Q$ is the class of $3$.
Check: completing the square gives $Q = (x + \tfrac{y}{2})^2 + 3 (\tfrac{y}{2})^2$, which is $\langle 1, 3 \rangle$ with determinant $3$.
The number-theory discriminant is $b^2 - 4ac = 1 - 4 = -3$, which is $-4 \det A$.
[[The discriminant of x² + xy + y²|96WEHXG3KP]] works this out in full.

### More examples

A diagonal form $\langle a_1, \dots, a_n \rangle = a_1 x_1^2 + \dots + a_n x_n^2$ has discriminant the class of $a_1 a_2 \cdots a_n$, because its matrix is diagonal.
[[The forms x² + y² and x² + 2y²|C18PABZVSN]] have discriminants $1$ and $2$, which are different classes in $\mathbb{Q}^\times / \mathbb{Q}^{\times 2}$, so they are not equivalent over $\mathbb{Q}$.
Over $\mathbb{R}$ the square classes are the two signs, so a nondegenerate form with $p$ positive and $q$ negative squares has discriminant $(-1)^q$.
Over $\mathbb{C}$ every nonzero number is a square, so every nondegenerate form has discriminant $1$, in line with [[the classification over C|0CEX9BRXRZ]].

### What it is not

The number $\det A$ is not the discriminant.
The forms $x^2$ and $4x^2$ on $\mathbb{Q}$ are equivalent by $x \mapsto 2x$, but their matrices have determinants $1$ and $4$, as [[the non-invariance of the determinant|VND7J04NCS]] explains.
Only the class modulo squares survives a change of basis.

The trace of $A$ is not an invariant at all.
The form $x^2 + y^2$ has trace $2$, and the equivalent form $(x + y)^2 + (x - y)^2 = 2x^2 + 2y^2$ has trace $4$, while $4/2 = 2$ is not even a square.

### The rules you can use

The discriminant does not depend on the basis, and equivalent forms share it, by [[the invariance theorem|WYQGZK8GFT]].
A form is [[nondegenerate|01NHFZF2SK]] exactly when its discriminant is not $0$, because nondegeneracy means $\det A \ne 0$.
The discriminant of an orthogonal sum is the product of the discriminants, because the matrix of the sum is block diagonal and its determinant is the product of the blocks.
Over a finite field of odd order, two nondegenerate forms of the same dimension are equivalent exactly when their discriminants agree.
Over $\mathbb{Q}$ this converse fails: $x^2 + y^2$ and $-x^2 - y^2$ both have discriminant $1$, but the first is positive definite and the second is negative definite.

### Watch out

Three errors are common.
The first is to compare the numbers $\det A$ in place of their classes: over $\mathbb{Q}$ the determinants $2$ and $8$ give the same discriminant, because $8 = 2 \cdot 2^2$.
The second is to mix the conventions $\det A$ and $b^2 - 4ac$ for binary forms, which differ by the factor $-4$ and so by a sign modulo squares.
The third is to forget the factor $\tfrac12$: the matrix of $x^2 + xy$ is $\begin{pmatrix} 1 & 1/2 \\ 1/2 & 0 \end{pmatrix}$ with determinant $-\tfrac14$, not $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ with determinant $-1$.
Here both determinants lie in the class of $-1$, but for $x^2 + xy + y^2$ the wrong matrix gives $0$ in place of $\tfrac34$.

### History

Gauss studied binary quadratic forms with integer coefficients in his Disquisitiones Arithmeticae of 1801.

### Try it

First, find the discriminant of $Q = 2x^2 + 6xy + 3y^2$ over $\mathbb{Q}$.
The matrix is $\begin{pmatrix} 2 & 3 \\ 3 & 3 \end{pmatrix}$ with determinant $6 - 9 = -3$, so $\operatorname{disc} Q$ is the class of $-3$.

Second, are $x^2 + 5y^2$ and $5x^2 + y^2$ equivalent over $\mathbb{Q}$?
Swapping $x$ and $y$ turns one into the other, so they are equivalent, and indeed both have discriminant $5$.

## Explanations

### L1 human

Write the symmetric matrix of a quadratic form and compute its determinant.
If you change the variables, the determinant gets multiplied by a square number, such as $4$ or $\tfrac19$.
So we keep the determinant only up to squares, and that is the discriminant.
For example, $x^2 + y^2$ has determinant $1$, and $x^2 + 2y^2$ has determinant $2$.
Since $2$ is not a square of a fraction, no change of variables with fractions turns one form into the other.

### L2 human

Here is a problem where the discriminant is not enough: are $Q_1 = x^2 + 3y^2$ and $Q_2 = 2x^2 + 6y^2$ equivalent over $\mathbb{Q}$?
The determinants are $3$ and $12 = 3 \cdot 2^2$, so the discriminants agree, and we need another test.
Equivalent forms take the same values, and $Q_2(1, 0) = 2$.
Suppose that $Q_1(a/c, b/c) = 2$ with integers $a, b, c$ and no common factor, so that
$$a^2 + 3b^2 = 2c^2.$$
Modulo $3$ this says $a^2 \equiv 2c^2$, and since squares modulo $3$ are $0$ or $1$, both sides must be $0$, so $3$ divides $a$ and $c$.
Then $9$ divides $a^2$ and $2c^2$, so $9$ divides $3b^2$, and $3$ divides $b$ too, which is a contradiction.
So $Q_1$ never takes the value $2$, and the two forms are not equivalent although their discriminants agree.
The typical use of the discriminant is the other direction: different discriminants prove at once that two forms are not equivalent.

### L3 human

The discriminant is the determinant of the quadratic space $(V, Q)$: the form induces a symmetric form on the line $\Lambda^n V$, and its class is $\operatorname{disc} Q$.
On the Witt ring $W(F)$, the signed discriminant gives a homomorphism from the ideal $I$ of even-dimensional classes onto $F^\times / F^{\times 2}$, with kernel $I^2$.
Over a $p$-adic field, the dimension, the discriminant and the Hasse invariant classify nondegenerate forms, and these local data enter the [[Hasse-Minkowski theorem|R8HCWA981S]].
For binary forms over $\mathbb{Z}$, the number $b^2 - 4ac$ is an invariant on the nose, and it organizes the theory of class groups of quadratic fields.
