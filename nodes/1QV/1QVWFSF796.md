---
tag: 1QVWFSF796
kind: proof
name: Proof of the associativity of matrix multiplication
msc: [15A99]
proves: 073E4XC016
uses: [076JGP6R3T, 0894J980RK]
sources:
  - url: https://proofwiki.org/wiki/Matrix_Multiplication_is_Associative
---

## Proof

We compare the two sides entry by entry.

1. Write $A = (a_{ij})$, $B = (b_{jk})$ and $C = (c_{kl})$, with $1 \le i \le m$, $1 \le j \le n$, $1 \le k \le p$ and $1 \le l \le q$.
2. By the definition of the [[matrix product|076JGP6R3T]], $AB$ is $m \times p$ and $BC$ is $n \times q$. So $(AB)C$ and $A(BC)$ are both defined, and both are $m \times q$ matrices.
3. Fix $i$ and $l$. By definition, $((AB)C)_{il} = \sum_{k=1}^{p} (AB)_{ik} c_{kl} = \sum_{k=1}^{p} \Big( \sum_{j=1}^{n} a_{ij} b_{jk} \Big) c_{kl}$.
4. The distributive law of the [[ring|0894J980RK]] $R$ moves $c_{kl}$ inside the inner sum. So $((AB)C)_{il} = \sum_{k=1}^{p} \sum_{j=1}^{n} (a_{ij} b_{jk}) c_{kl}$.
5. By definition, $(A(BC))_{il} = \sum_{j=1}^{n} a_{ij} (BC)_{jl} = \sum_{j=1}^{n} a_{ij} \Big( \sum_{k=1}^{p} b_{jk} c_{kl} \Big)$.
6. The distributive law moves $a_{ij}$ inside the inner sum. So $(A(BC))_{il} = \sum_{j=1}^{n} \sum_{k=1}^{p} a_{ij} (b_{jk} c_{kl})$.
7. Multiplication in $R$ is associative, so $(a_{ij} b_{jk}) c_{kl} = a_{ij} (b_{jk} c_{kl})$ for all $j$ and $k$.
8. Addition in $R$ is associative and commutative. So a finite double sum does not depend on the order of summation. With step 7, the sums in steps 4 and 6 are equal.
9. Thus $((AB)C)_{il} = (A(BC))_{il}$ for all $i$ and $l$. Since both matrices have the same size, $(AB)C = A(BC)$.

## Idea

Both products have entry $(i, l)$ equal to the sum of $a_{ij} b_{jk} c_{kl}$ over all pairs $(j, k)$. The two ways of bracketing only add these terms in a different order, which does not change a finite sum.
