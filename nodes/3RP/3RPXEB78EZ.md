---
tag: 3RPXEB78EZ
kind: proof
name: Proof that the endomorphisms of a vector space form an associative algebra
msc: ["15A04", "16S50"]
topics: [9080WQTZ3M]
audience: ug1
proves: 7BDGQ1Q46E
methods: [0NTF6DMVAP, 41JZ39GE3F]
uses: [PB7N4R8C6X, FSXBBV9C76, 1TZSV19D85, 0R8X9XA83A, 0YYMY95FWS, 05Q1B7MH0M]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism_ring
    locator: Description
  - book: isbn:9780135367971
    locator: Section 3.2
---

## Proof

We check the axioms of an [[associative algebra|1TZSV19D85]] one at a time by evaluating both sides at a vector, and then we compare with matrices.

1. By the [[vector space theorem|PB7N4R8C6X]] with $W = V$, the set $\End(V)$ is a vector space over $F$.
2. By the [[theorem on composites|FSXBBV9C76]], $S \circ T$ is linear for $S, T \in \End(V)$, so composition is an operation on $\End(V)$.
3. For associativity, note that $((RS)T)(v) = R(S(T(v))) = (R(ST))(v)$ for each $v \in V$.
4. For the unit, note that $\id_V$ is linear and $\id_V(T(v)) = T(v) = T(\id_V(v))$ for each $v$.
5. For right distributivity, the definition of the sum gives $((R + S)T)(v) = R(T(v)) + S(T(v)) = (RT + ST)(v)$.
6. For left distributivity, $R$ is additive, so $(R(S + T))(v) = R(S(v) + T(v)) = R(S(v)) + R(T(v))$.
7. The right side of step 6 is $(RS + RT)(v)$, so $R(S + T) = RS + RT$.
8. For scalars, $(a(ST))(v) = a\,S(T(v))$, and $((aS)T)(v) = a\,S(T(v))$ by the definition of $aS$.
9. Since $S$ is homogeneous, $(S(aT))(v) = S(a\,T(v)) = a\,S(T(v))$, so $a(ST) = (aS)T = S(aT)$.
10. Steps 1 to 9 prove part 1.
11. For part 2, let $B = (b_1, \dots, b_n)$ and $\mu(T) = [T]_B$, whose column $j$ holds the coordinates of $T(b_j)$.
12. The map $\mu$ is linear, since the coordinates of $(S + aT)(b_j)$ are those of $S(b_j)$ plus $a$ times those of $T(b_j)$.
13. The map $\mu$ is bijective, since for each matrix $A$ the [[theorem on bases|0R8X9XA83A]] gives exactly one $T$ with $T(b_j) = \sum_i a_{ij} b_i$.
14. We have $\mu(ST) = \mu(S)\,\mu(T)$, since the [[matrix of a composite is the product|05Q1B7MH0M]] of the matrices.
15. Finally $\mu(\id_V) = I_n$, since $\id_V(b_j) = b_j$, so $\mu$ is an algebra isomorphism, which proves part 2.

## Idea

Each algebra axiom is an identity between maps.
Evaluate both sides at a vector $v$, and use the definitions of the sum, the scalar multiple and the composite.
Linearity of the left factor is used exactly twice, for left distributivity and for $S(aT) = a(ST)$.

## Variants

For finite-dimensional $V$, one can prove part 2 first and transfer the axioms from $M_n(F)$, but this needs the algebra axioms for matrices, proved directly from the entries.
In the other direction, associativity of matrix multiplication follows from step 3 and part 2, which is the [[proof by composition|KC9SCPKS2G]].
