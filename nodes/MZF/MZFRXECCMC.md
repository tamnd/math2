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

Let $F$ be a field of characteristic not $2$, and let $Q$ be a [[quadratic form|0RBQS1JJCR]] on a vector space $V$ of finite dimension $n$.
Let $A$ be the symmetric matrix of $Q$ in a basis, as in [[the correspondence theorem|VN9AG8JKYT]].
The *discriminant* of $Q$ is the [[determinant|00KDZRW4C0]] $\det A$, taken modulo nonzero squares.
It is $0$ when $\det A = 0$, and otherwise the [[square class|9160DW40TE]] of $\det A$ in $F^\times / F^{\times 2}$.
By [[the invariance theorem|WYQGZK8GFT]], it does not depend on the basis, and equivalent forms have the same discriminant.
After the dimension, it is the simplest invariant of a quadratic form.
Over a finite field of odd order, the two together classify nondegenerate forms.

## Motivation

The matrix of $Q$ changes to $P^T A P$ when the basis changes, so $\det A$ is multiplied by $\det(P)^2$.
The number $\det A$ is not an invariant, but its class modulo squares is.
This class is a cheap test: if two forms have different discriminants, they are not equivalent.
For example, over $\Q$ it shows at once that $x^2 + y^2$ and $x^2 + 2y^2$ are not equivalent.

## Notation

- $\operatorname{disc} Q$ or $d(Q)$: the class of $\det A$ in $F^\times / F^{\times 2}$, or $0$.
- Signed discriminant: $d_\pm(Q) = (-1)^{n(n-1)/2} \det A$. With this sign, the [[hyperbolic plane|1X5PZSK44P]] $xy$ has signed discriminant $1$. Some books call this the discriminant.
- For a binary form $a x^2 + b x y + c y^2$, number theory uses the number $b^2 - 4ac$, an integer, with no division by squares; see [[binary quadratic forms|SBDSYA037Q]].
- The two conventions are related by $\det \begin{pmatrix} a & b/2 \\ b/2 & c \end{pmatrix} = ac - \frac{b^2}{4} = -\frac14 (b^2 - 4ac)$.

## Remarks

### Examples

- [[Over $\Q$, $x^2 + y^2$ and $x^2 + 2y^2$|C18PABZVSN]] have discriminants $1$ and $2$, which are different square classes. So they are not equivalent over $\Q$.
- [[The binary form $x^2 + xy + y^2$|96WEHXG3KP]] has $\det A = \frac34$, which is in the class of $3$, and $b^2 - 4ac = -3$.
- Over $\R$, the square classes are the signs. A nondegenerate form of signature $(p, q, 0)$ has discriminant $(-1)^q$.
- Over $\C$, every nonzero element is a square, so all nondegenerate forms have discriminant $1$.
- The diagonal form $\langle a_1, \dots, a_n \rangle$ has discriminant $a_1 a_2 \cdots a_n$ modulo squares.

### Non-examples

- [[The determinant itself is not an invariant|VND7J04NCS]]: $x^2$ and $4x^2$ are equivalent over $\Q$, but their matrices have determinants $1$ and $4$.
- The trace of $A$ is not an invariant: $x^2 + y^2$ has trace $2$, and the equivalent form $(x + y)^2 + (x - y)^2 = 2x^2 + 2y^2$ has trace $4$.

### Basic properties

- Equivalent forms have the same discriminant, by [[the invariance theorem|WYQGZK8GFT]].
- $Q$ is nondegenerate if and only if its discriminant is not $0$.
- The discriminant of an orthogonal sum is the product of the discriminants.
- Over a finite field of odd order, take two nondegenerate forms of the same dimension. By [[the finite field theorem|2HBR7137AD]], they are equivalent if and only if they have the same discriminant.
- Over $\Q$, the discriminant is not enough: $x^2 + y^2$ and $-x^2 - y^2$ both have discriminant $1$, but one is positive definite and the other negative definite.

### History

The Wikipedia article on quadratic forms has a history section.
It records that Gauss studied binary forms over the integers in the Disquisitiones Arithmeticae of 1801.
No source in the reading list of this topic gives the first use of the discriminant of a form in $n$ variables.
So we give no date for it.

### Common errors

- Comparing the numbers $\det A$ instead of their square classes. Over $\Q$, the determinants $2$ and $8$ give the same discriminant.
- Mixing the conventions $\det A$ and $b^2 - 4ac$ for binary forms. They differ by the factor $-\frac14$, so they differ in sign.
- Forgetting the factor $\frac12$ in the matrix of a binary form with an $xy$ term.

## Explanations

### L1 human

Take the symmetric matrix of a quadratic form, and compute its determinant.
After a change of variables, the determinant is multiplied by a square.
So we only keep the determinant up to squares, and this is the discriminant.
Two forms with different discriminants cannot be turned into each other.

### L2 human

Worked example: we test whether $Q_1 = x^2 + 3y^2$ and $Q_2 = 2x^2 + 6y^2$ are equivalent over $\Q$.

1. $\det A_1 = 3$ and $\det A_2 = 12 = 3 \cdot 2^2$. The discriminants are equal.
2. So the discriminant does not separate them. Over $\Q$ more invariants exist, so we need another test.
3. $Q_2$ takes the value $2$ at $(1, 0)$. If $x^2 + 3y^2 = 2$ for rationals $x = a/c$, $y = b/c$, then $a^2 + 3b^2 = 2c^2$. Reducing modulo $3$ gives $a^2 \equiv 2c^2$, which forces $a$ and $c$ to be divisible by $3$, and then also $b$. So there is no solution in lowest terms.
4. So $Q_1$ does not take the value $2$, and the two forms are not equivalent over $\Q$, although they have the same discriminant.

A trap: equal discriminants do not prove equivalence, except over special fields such as finite fields.

### L3 human

The discriminant is the determinant of the quadratic space $(V, Q)$, the induced form on $\Lambda^n V$, viewed in $F^\times / F^{\times 2}$.
The signed discriminant gives a group homomorphism from the fundamental ideal of the Witt ring $W(F)$ to $F^\times / F^{\times 2}$, with kernel $I^2$.
Over a local field, the dimension, the discriminant and the Hasse invariant classify forms; this is the local input in [[the Hasse-Minkowski theorem|R8HCWA981S]].
