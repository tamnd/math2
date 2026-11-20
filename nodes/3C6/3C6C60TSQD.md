---
tag: 3C6C60TSQD
kind: proof
name: Proof that similar matrices have the same invariants
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug1
proves: 191HBJ7PVZ
uses: [027KDW2K72, 02FDWY55AS, 0Y4NF1DRKD, 04CPJ6AF00, 0TYMASG33Y, 0V58FPM3EQ, 073E4XC016]
methods: [0NTF6DMVAP, S3QADD13E9]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: Properties
---

## Proof

Let $B = P^{-1} A P$ with $P$ invertible.
We prove the six parts in turn.

1. Rank, first inequality. By the [[rank of a product|02FDWY55AS]], $\rank B = \rank(P^{-1}(AP)) \le \rank(AP) \le \rank A$.
2. Rank, second inequality. By [[associativity|073E4XC016]], $P B P^{-1} = (P P^{-1}) A (P P^{-1}) = A$. The same rule gives $\rank A \le \rank B$.
3. Steps 1 and 2 give $\rank B = \rank A$. This proves part 1.
4. Trace. By the [[cyclic property|0Y4NF1DRKD]] with $X = P^{-1}$ and $Y = AP$, $\tr(P^{-1}(AP)) = \tr((AP)P^{-1}) = \tr(A(PP^{-1})) = \tr A$. This proves part 2.
5. Determinant. By [[multiplicativity|04CPJ6AF00]], $\det B = \det(P^{-1}) \det A \det P$.
6. The field $F$ is commutative, so $\det B = \det A \cdot \det(P^{-1}) \det P = \det A \cdot \det(P^{-1} P) = \det A \cdot \det I_n = \det A$. This proves part 3.
7. Characteristic polynomial. This is the [[theorem on the characteristic polynomial|0TYMASG33Y]], which proves part 4. The eigenvalues in $F$ are the roots of this polynomial, with the same multiplicities.
8. Powers. We show $B^k = P^{-1} A^k P$ by induction on $k$. For $k = 0$, both sides are $I_n$.
9. If $B^k = P^{-1} A^k P$, then $B^{k+1} = B^k B = P^{-1} A^k (P P^{-1}) A P = P^{-1} A^{k+1} P$, by associativity.
10. Polynomials. Let $q = \sum_{k} c_k x^k$. By step 9 and the distributive law, $q(B) = \sum_k c_k P^{-1} A^k P = P^{-1} \left(\sum_k c_k A^k\right) P = P^{-1} q(A) P$.
11. So $q(B)$ is similar to $q(A)$, and $\rank q(B) = \rank q(A)$ by step 3 applied to $q(A)$. This proves part 6.
12. Minimal polynomial. By step 10, $q(B) = 0$ implies $q(A) = P\, q(B)\, P^{-1} = 0$. Also $q(A) = 0$ implies $q(B) = P^{-1} \cdot 0 \cdot P = 0$.
13. So $A$ and $B$ have the same annihilating polynomials.
14. The [[minimal polynomial|0V58FPM3EQ]] is the monic annihilating polynomial of least degree. It depends only on the set of annihilating polynomials, so it is the same for $A$ and $B$. This proves part 5. $\blacksquare$

## Idea

Write $B = P^{-1} A P$ and move the factors $P$ and $P^{-1}$ together.
For the trace this uses the cyclic property, and for the determinant it uses commutativity of $F$.
For polynomials, the factors $P P^{-1}$ in the middle of each power cancel.

## Variants

- One can define each invariant for an endomorphism $T$ without a basis: $\rank T = \dim \operatorname{im} T$, $\det T$ through alternating forms, and $m_T$ directly. Then the theorem says that the matrix invariants equal the invariants of $T$.
- The rank part also follows from the fact that multiplication by an invertible matrix is an isomorphism. It maps $\operatorname{Col}(AP) = \operatorname{Col}(A)$ onto $\operatorname{Col}(P^{-1} A P)$.
