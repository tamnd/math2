---
tag: ZH8JC9DZ1J
kind: proof
name: Proof that similarity is an equivalence relation
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug1
proves: HWKZ8DM8P0
uses: [027KDW2K72, 0TWTS88TWN, 06DW9BAWB1, 073E4XC016, 0S4WTRE9GG]
methods: [RGNF33GVHX]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: lead section
---

## Proof

We check the three axioms of an equivalence relation in turn.

1. Reflexive. The [[identity matrix|06DW9BAWB1]] $I_n$ is [[invertible|0TWTS88TWN]] with $I_n^{-1} = I_n$, since $I_n I_n = I_n$.
2. So $I_n^{-1} A I_n = I_n A I_n = A$, because $I_n$ is a neutral element for the matrix product. By the [[definition of similarity|027KDW2K72]], $A$ is similar to $A$.
3. Symmetric. Assume $B$ is similar to $A$. By the definition, $B = P^{-1} A P$ for an invertible $P$.
4. Multiply on the left by $P$ and on the right by $P^{-1}$. By [[associativity|073E4XC016]], $P B P^{-1} = (P P^{-1}) A (P P^{-1}) = I_n A I_n = A$.
5. Put $R = P^{-1}$. The matrix $R$ is invertible with $R^{-1} = P$, since $P^{-1} P = P P^{-1} = I_n$. This is the definition of an inverse with the roles exchanged.
6. By step 4, $A = R^{-1} B R$. So $A$ is similar to $B$.
7. Transitive. Assume $B = P^{-1} A P$ and $C = Q^{-1} B Q$, with $P$ and $Q$ invertible.
8. Substitute the first equation into the second. By associativity, $C = Q^{-1} (P^{-1} A P) Q = (Q^{-1} P^{-1}) A (P Q)$.
9. By the [[theorem on the inverse of a product|0S4WTRE9GG]], $PQ$ is invertible and $(PQ)^{-1} = Q^{-1} P^{-1}$.
10. So $C = (PQ)^{-1} A (PQ)$ with $PQ$ invertible, and $C$ is similar to $A$.
11. Steps 2, 6 and 10 are the three axioms. So similarity is an equivalence relation on $M_n(F)$. $\blacksquare$

## Idea

Each axiom of an equivalence relation matches one property of the invertible matrices.
The identity gives reflexivity, the inverse gives symmetry, and the product gives transitivity.
In other words, the invertible matrices form a group, and similarity is the orbit relation of its conjugation action.

## Variants

- One can prove the theorem with linear maps: $A$ and $B$ are similar if and only if they are the matrices of one endomorphism in two bases. "Being the matrix of the same map" is then an equivalence relation at once.
- The same proof shows that conjugacy in any group is an equivalence relation.
