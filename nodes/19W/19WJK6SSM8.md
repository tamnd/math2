---
tag: 19WJK6SSM8
kind: proof
name: Proof that a family is a basis if and only if its determinant is nonzero
msc: [15A15, 15A75]
topics: [DTBK11SR77]
audience: ug2
proves: 5D1CHPV9Z3
methods: [0NTF6DMVAP]
uses: [0V94H674MB, 059THXBRBB, 0EVHJFTG9Z, WFM1CX5PZT, 03Q7RE2HXR]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of n vectors
---

## Proof

We move the question from $V$ to $F^n$ with the coordinate map, where it becomes the invertibility of one matrix.

1. Let $\varphi \colon V \to F^n$ send $v$ to its coordinate vector $[v]_B$.
   By the [[isomorphism with the coordinate space|059THXBRBB]], $\varphi$ is a linear isomorphism.
2. Let $w_j = \varphi(v_j)$, and let $M$ be the $n \times n$ matrix with the columns $w_1, \dots, w_n$.
3. Since $\varphi$ is linear, for all scalars $c_1, \dots, c_n$,
$$\varphi\Big(\sum_j c_j v_j\Big) = \sum_j c_j w_j.$$
4. Since $\varphi$ is injective and $\varphi(0) = 0$, step 3 shows that $\sum_j c_j v_j = 0$ if and only if $\sum_j c_j w_j = 0$.
   So the $v_j$ are [[linearly independent|0EVHJFTG9Z]] if and only if the $w_j$ are.
5. Since $\varphi$ is surjective, step 3 shows that the $v_j$ span $V$ if and only if the $w_j$ span $F^n$.
6. By steps 4 and 5, $(v_1, \dots, v_n)$ is a basis of $V$ if and only if $(w_1, \dots, w_n)$ is a basis of $F^n$.
7. By the [[column criterion|WFM1CX5PZT]], the columns of the square matrix $M$ form a basis of $F^n$ if and only if $M$ is invertible.
8. By the [[invertibility criterion over commutative rings|03Q7RE2HXR]], $M$ is invertible if and only if $\det M$ is a unit of $F$.
9. In a field every nonzero element has an inverse and $0$ has none, so the units are the nonzero elements.
   Hence $M$ is invertible if and only if $\det M \ne 0$.
10. By the [[definition|0V94H674MB]], $\det M = \det_B(v_1, \dots, v_n)$.
    With steps 6 to 9, this proves that $v_1, \dots, v_n$ is a basis if and only if $\det_B(v_1, \dots, v_n) \ne 0$.

## Idea

Coordinates in $B$ turn $V$ into $F^n$, and an isomorphism does not change which families are independent or spanning.
In $F^n$, a family of $n$ vectors is a basis exactly when the matrix with those columns is invertible.
The determinant detects invertibility, so it detects bases.

## Variants

A second proof avoids the coordinate map and uses the [[change of basis rule|T1WN2DHS63]] for one direction.
If the $v_j$ form a basis $B'$, then $\det_B(B') \det_{B'}(B) = 1$, so $\det_B(B')$ cannot be $0$.
For the other direction, suppose that the $v_j$ are dependent, so one of them, say $v_k$, is a combination of the others.
Expanding $\det_B$ in the slot $k$ by multilinearity gives a sum of determinants with two equal vectors, and each of them is $0$ because $\det_B$ is alternating.
