---
tag: 8HVW5T9CRS
kind: proof
name: Proof that bilinear forms correspond to matrices and to linear maps into the dual
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
proves: ZVMJAF7D53
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0P799D6AMN, 0P24YW565F, 0M856Q1AMZ, 0W6M3PSD08, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Coordinate representation
---

## Proof

Part 1 (the maps into the dual space).

1. Fix $u \in V$. The map $L_B(u) = B(u, \cdot)$ is linear, by linearity of $B$ in the second slot. So $L_B(u) \in V^*$, by the definition of the [[dual space|0M856Q1AMZ]].
2. For $u, u' \in V$, $a \in F$ and every $v$, linearity in the first slot gives $B(au + u', v) = aB(u, v) + B(u', v)$. So $L_B(au + u') = aL_B(u) + L_B(u')$, and $L_B$ is linear.
3. The same two steps with the slots exchanged show that $R_B$ is a linear map $V \to V^*$.
4. The map $B \mapsto L_B$ is linear, because $(aB + B')(u, v) = aB(u, v) + B'(u, v)$ for all $u, v$.
5. Let $T \colon V \to V^*$ be linear, and define $B_T(u, v) = T(u)(v)$. It is linear in $v$ because $T(u) \in V^*$, and linear in $u$ because $T$ is linear.
6. By the definitions, $L_{B_T}(u)(v) = T(u)(v)$ and $B_{L_B}(u, v) = L_B(u)(v) = B(u, v)$. So $T \mapsto B_T$ is the inverse of $B \mapsto L_B$, and part 1 holds.

Part 2 (the formula $x^T A y$).

7. Write $u = \sum_i x_i e_i$ and $v = \sum_j y_j e_j$. Linearity in the first slot gives $B(u, v) = \sum_i x_i B(e_i, v)$.
8. Linearity in the second slot gives $B(e_i, v) = \sum_j y_j B(e_i, e_j) = \sum_j A_{ij} y_j$, by the definition of the [[matrix of $B$|0P24YW565F]].
9. So $B(u, v) = \sum_i \sum_j x_i A_{ij} y_j$, which is the matrix product $x^T A y$.

Part 3 (forms and matrices).

10. The map $B \mapsto A$ is linear, because $(aB + B')(e_i, e_j) = aB(e_i, e_j) + B'(e_i, e_j)$.
11. It is injective: if $A = 0$, then step 9 gives $B(u, v) = 0$ for all $u, v$.
12. It is surjective: for $A \in M_n(F)$ the map $(u, v) \mapsto x^T A y$ is bilinear, because coordinates depend linearly on vectors and the matrix product is linear in each factor. Its value on $(e_i, e_j)$ is $A_{ij}$.

Part 4 (the matrices of $L_B$ and $R_B$).

13. Each $\varphi \in V^*$ equals $\sum_i \varphi(e_i) e_i^*$, by the definition of the [[dual basis|0W6M3PSD08]]: both sides agree on each $e_k$.
14. By step 13, $L_B(e_j) = \sum_i B(e_j, e_i) e_i^* = \sum_i A_{ji} e_i^*$.
15. Column $j$ of the [[matrix of $L_B$|0YYMY95FWS]] holds the coordinates of $L_B(e_j)$. So its entry $(i, j)$ is $A_{ji}$, and the matrix is $A^T$.
16. By step 13, $R_B(e_j) = \sum_i B(e_i, e_j) e_i^* = \sum_i A_{ij} e_i^*$. So the entry $(i, j)$ of the matrix of $R_B$ is $A_{ij}$, and the matrix is $A$.

This proves all four parts.

## Idea

A bilinear form is fixed by its values on basis pairs, because it is linear in each slot.
Fixing one slot of the form gives a linear form, and this is the map into the dual space.
The matrix of that map has the values $B(e_j, e_i)$ in column $j$, which is why a transpose appears.

## Variants

Part 1 is the tensor-hom adjunction $\Hom(V \otimes V, F) \cong \Hom(V, V^*)$, and parts 2 and 3 follow from it with the basis $e_i^* \otimes e_j^*$ of $(V \otimes V)^*$.
