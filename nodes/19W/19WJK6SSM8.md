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

We move the question to $F^n$ with the coordinate map.

1. Let $\varphi \colon V \to F^n$, $v \mapsto [v]_B$. By the [[coordinate map statement|059THXBRBB]], $\varphi$ is a linear isomorphism.
2. Let $w_j = \varphi(v_j)$, and let $M$ be the matrix with columns $w_1, \dots, w_n$.
3. By linearity, $\varphi(\sum_j c_j v_j) = \sum_j c_j w_j$ for all scalars $c_j$.
4. $\varphi$ is injective, so $\sum_j c_j v_j = 0$ if and only if $\sum_j c_j w_j = 0$.
5. So the $v_j$ are [[linearly independent|0EVHJFTG9Z]] if and only if the $w_j$ are.
6. $\varphi$ is surjective. By step 3, the $v_j$ span $V$ if and only if the $w_j$ span $F^n$.
7. By steps 5 and 6, $(v_1, \dots, v_n)$ is a basis of $V$ if and only if $(w_1, \dots, w_n)$ is a basis of $F^n$.
8. By the [[column criterion|WFM1CX5PZT]], this holds if and only if $M$ is invertible.
9. By the [[invertibility criterion|03Q7RE2HXR]], $M$ is invertible if and only if $\det M$ is a unit of $F$.
10. In a field, the units are the nonzero elements. So $M$ is invertible if and only if $\det M \ne 0$.
11. By the [[definition|0V94H674MB]], $\det M = \det_B(v_1, \dots, v_n)$, which proves the claim.

## Idea

Coordinates in $B$ turn $V$ into $F^n$ without changing linear relations.
A family in $F^n$ is a basis exactly when its matrix is invertible, and this is exactly when the determinant is nonzero.

## Variants

A second proof uses the change of basis rule.
If the $v_j$ form a basis $B'$, then $\det_B(B') \det_{B'}(B) = 1$, so $\det_B(B') \ne 0$.
If they are dependent, one $v_j$ is a combination of the others, and the alternating property gives $\det_B(v_1, \dots, v_n) = 0$.
