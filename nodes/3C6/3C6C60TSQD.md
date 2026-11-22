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

We write $B = P^{-1}AP$ with $P$ invertible and treat the six parts in turn, each time moving $P$ and $P^{-1}$ next to each other.

1. Rank, first inequality.
   The rank of a product is at most the rank of each factor, by the theorem on the [[rank of a product|02FDWY55AS]], so
   $$\operatorname{rank} B = \operatorname{rank}\bigl(P^{-1}(AP)\bigr) \le \operatorname{rank}(AP) \le \operatorname{rank} A.$$
2. Rank, second inequality.
   By [[associativity|073E4XC016]], $PBP^{-1} = (PP^{-1})A(PP^{-1}) = A$, so $A$ is similar to $B$ by the matrix $P^{-1}$.
   Step 1 with the roles exchanged gives $\operatorname{rank} A \le \operatorname{rank} B$.
3. Steps 1 and 2 give $\operatorname{rank} B = \operatorname{rank} A$, which is part 1.
4. Trace.
   The [[cyclic property|0Y4NF1DRKD]] $\operatorname{tr}(XY) = \operatorname{tr}(YX)$ with $X = P^{-1}$ and $Y = AP$ gives
   $$\operatorname{tr} B = \operatorname{tr}\bigl(P^{-1}(AP)\bigr) = \operatorname{tr}\bigl((AP)P^{-1}\bigr) = \operatorname{tr}\bigl(A(PP^{-1})\bigr) = \operatorname{tr} A,$$
   which is part 2.
5. Determinant.
   By [[multiplicativity of the determinant|04CPJ6AF00]], $\det B = \det(P^{-1})\,\det A\,\det P$.
6. These are elements of the commutative field $F$, so we may reorder them:
   $$\det B = \det A \cdot \det(P^{-1})\det P = \det A \cdot \det(P^{-1}P) = \det A \cdot \det I_n = \det A,$$
   which is part 3.
7. Characteristic polynomial.
   Part 4 is the theorem that the [[characteristic polynomial does not depend on the basis|0TYMASG33Y]].
   The eigenvalues in $F$ are the roots of this polynomial, so they agree with their algebraic multiplicities.
8. Powers.
   We show $B^k = P^{-1}A^kP$ by induction on $k$.
   For $k = 0$, both sides equal $I_n$.
9. If $B^k = P^{-1}A^kP$, then associativity gives
   $$B^{k+1} = B^kB = P^{-1}A^k(PP^{-1})AP = P^{-1}A^{k+1}P.$$
10. Polynomials.
    Let $q = \sum_k c_k x^k$.
    By steps 8 and 9 and the distributive law,
    $$q(B) = \sum_k c_k P^{-1}A^kP = P^{-1}\Bigl(\sum_k c_k A^k\Bigr)P = P^{-1}q(A)P.$$
11. So $q(B)$ is similar to $q(A)$, and step 3 applied to $q(A)$ gives $\operatorname{rank} q(B) = \operatorname{rank} q(A)$, which is part 6.
12. Minimal polynomial.
    By step 10, if $q(B) = 0$, then $q(A) = P\,q(B)\,P^{-1} = 0$, and if $q(A) = 0$, then $q(B) = P^{-1} \cdot 0 \cdot P = 0$.
    So $A$ and $B$ have the same annihilating polynomials.
13. The [[minimal polynomial|0V58FPM3EQ]] is the monic annihilating polynomial of least degree.
    It depends only on the set of annihilating polynomials, so it is the same for $A$ and $B$, which is part 5.

## Idea

Write $B = P^{-1}AP$ and bring the factors $P$ and $P^{-1}$ together until they cancel.
For the trace, the cyclic property moves $P^{-1}$ to the end.
For the determinant, the product of numbers can be reordered.
For powers and polynomials, the factors $PP^{-1}$ in the middle of each power cancel at once.
The rank needs a different trick: it can only go down under multiplication, and similarity works in both directions, so it cannot go down at all.

## Variants

Each invariant can be defined for an endomorphism $T$ without a basis.
The rank is $\dim \operatorname{im} T$, the determinant comes from the action of $T$ on alternating forms of top degree, and the minimal polynomial is the monic generator of the polynomials $q$ with $q(T) = 0$.
Then the theorem says that the matrix invariants equal the invariants of $T$, since $A$ and $B$ are matrices of the same map.
The rank part also follows from the fact that multiplication by an invertible matrix is an isomorphism: $\operatorname{Col}(AP) = \operatorname{Col}(A)$, and $P^{-1}$ maps $\operatorname{Col}(A)$ isomorphically onto $\operatorname{Col}(P^{-1}AP)$.
