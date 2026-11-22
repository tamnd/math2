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

We check the three axioms of an equivalence relation in turn, and each one uses one property of invertible matrices.

1. Reflexive.
   The [[identity matrix|06DW9BAWB1]] $I_n$ is [[invertible|0TWTS88TWN]] with $I_n^{-1} = I_n$, since $I_nI_n = I_n$.
2. Because $I_n$ is neutral for the matrix product, $I_n^{-1}AI_n = I_nAI_n = A$.
   By the [[definition of similarity|027KDW2K72]], $A$ is similar to $A$.
3. Symmetric.
   Assume that $B$ is similar to $A$, so $B = P^{-1}AP$ for an invertible $P$.
4. We multiply on the left by $P$ and on the right by $P^{-1}$, and use [[associativity|073E4XC016]]:
   $$PBP^{-1} = (PP^{-1})A(PP^{-1}) = I_nAI_n = A.$$
5. Put $R = P^{-1}$.
   The equations $P^{-1}P = PP^{-1} = I_n$ say that $R$ is invertible with $R^{-1} = P$.
6. So step 4 reads $A = R^{-1}BR$, and $A$ is similar to $B$.
7. Transitive.
   Assume that $B = P^{-1}AP$ and $C = Q^{-1}BQ$, with $P$ and $Q$ invertible.
8. We substitute the first equation into the second and use associativity:
   $$C = Q^{-1}(P^{-1}AP)Q = (Q^{-1}P^{-1})A(PQ).$$
9. By the theorem on the [[inverse of a product|0S4WTRE9GG]], $PQ$ is invertible and $(PQ)^{-1} = Q^{-1}P^{-1}$.
10. So $C = (PQ)^{-1}A(PQ)$ with $PQ$ invertible, and $C$ is similar to $A$.
11. Steps 2, 6 and 10 are the three axioms, so similarity is an equivalence relation on $M_n(F)$.

## Idea

Each axiom of an equivalence relation matches one property of the invertible matrices.
The identity gives reflexivity, the inverse gives symmetry, and the product gives transitivity.
In other words, the invertible matrices form a group, and similarity is the relation "lies in the same orbit" for the action of this group by conjugation.

## Variants

A second proof uses group actions.
The rule $A \cdot P = P^{-1}AP$ is a right action of the group $GL_n(F)$ on $M_n(F)$, since $A \cdot I_n = A$ and $(A \cdot P) \cdot Q = A \cdot (PQ)$.
For every group action, "$B$ lies in the orbit of $A$" is an equivalence relation, by the identity, inverse and product of the group.
The steps above are this general argument written out for matrices.
The same argument, with group elements in place of matrices, shows that conjugacy in any group is an equivalence relation.
