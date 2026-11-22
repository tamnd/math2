---
tag: DQH11Y1KMD
kind: proof
name: Proof that the discriminant is an invariant of equivalence
msc: ["11E04", 15A63]
topics: [6TSCEW8QMK]
audience: ug2
proves: WYQGZK8GFT
methods: [0NTF6DMVAP]
uses: [D3E2Y85S6H, FBSAPTP1PR, 0SPYAGE7T0, VN9AG8JKYT, 9160DW40TE]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Proof

We compute the determinant of the new matrix with the product rule, and then we reduce both a change of basis and an equivalence of forms to that computation.

1. By part 5 of [[the congruence statement|D3E2Y85S6H]], which uses the product rule and $\det P^{\mathsf{T}} = \det P$, we have $\det(P^{\mathsf{T}} A P) = \det(P)^2 \det A$.
   This proves part 1.
2. Let $Q$ be a quadratic form on $V$, and let $A$ and $A'$ be its symmetric matrices in two bases.
   By [[the correspondence theorem|VN9AG8JKYT]], which needs characteristic not $2$, both are matrices of the same associated bilinear form $B$.
3. By [[the change of basis rule|0SPYAGE7T0]], $A' = P^{\mathsf{T}} A P$, where $P$ is the invertible change of basis matrix.
4. By step 1, $\det A' = \det(P)^2 \det A$.
   Since $P$ is invertible, [[its determinant is nonzero|FBSAPTP1PR]].
5. If $\det A = 0$, then $\det A' = 0$.
   Otherwise $\det A' / \det A = \det(P)^2$ is a nonzero square, so the two determinants lie in the same [[square class|9160DW40TE]].
   This proves part 2.
6. Let $Q' = Q \circ T$ with $T \colon V \to V$ linear and invertible.
   The map $B'(u, v) = B(Tu, Tv)$ is symmetric and bilinear, and $B'(v, v) = Q(Tv) = Q'(v)$.
   By the uniqueness in the correspondence theorem, $B'$ is the associated bilinear form of $Q'$.
7. Fix a basis $e_1, \dots, e_n$ of $V$, and let $S$ be the matrix of $T$ in it.
   The matrix of $B'$ has entries $B(Te_i, Te_j)$, and these are the entries of $S^{\mathsf{T}} A S$.
8. The matrix $S$ is invertible because $T$ is.
   Steps 4 and 5 with $P = S$ show that $\det(S^{\mathsf{T}} A S)$ and $\det A$ are both $0$ or lie in the same square class.
   So $Q$ and $Q'$ have the same discriminant, which proves part 3.

## Idea

Everything comes down to one line: a new basis multiplies the determinant by $\det(P)^2$, because the determinant is multiplicative and a matrix and its transpose have the same determinant.
A square is invisible in $F^\times / F^{\times 2}$, so the class survives.
An equivalence $Q' = Q \circ T$ is the same computation with the matrix of $T$ in place of $P$.

## Variants

In coordinates, step 7 is the identity $(Su)^{\mathsf{T}} A (Sv) = u^{\mathsf{T}} (S^{\mathsf{T}} A S) v$, which reads off the matrix of $B'$ directly.

A second route goes through diagonal forms.
By [[the diagonalization theorem|0Z3FEWZ8HA]], $Q \cong \langle a_1, \dots, a_n \rangle$, and the discriminant is the class of $a_1 a_2 \cdots a_n$.
The theorem then says that any two diagonalizations of $Q$ have products of coefficients that differ by a square.
For example, $x^2 + y^2$ and its diagonalization $2u^2 + 2v^2$ have products $1$ and $4$.
