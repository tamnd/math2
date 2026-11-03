---
tag: 77W6HN6BPG
kind: proof
name: Proof of the distributivity of matrix multiplication
msc: [15A99]
proves: 0RXD6EZYBK
uses: [076JGP6R3T, 0BVXADM10P, 0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Distributivity
---

## Proof

We compare entries, using the definitions of [[matrix multiplication|076JGP6R3T]] and [[matrix addition|0BVXADM10P]].

1. Write $A = (a_{ij})$, $B = (b_{jk})$ and $C = (c_{jk})$, with $1 \le i \le m$, $1 \le j \le n$ and $1 \le k \le p$.
2. The matrix $B + C$ is $n \times p$, so $A(B + C)$ is $m \times p$. The matrices $AB$ and $AC$ are $m \times p$, so $AB + AC$ is $m \times p$.
3. Fix $i$ and $k$. By definition, $(A(B + C))_{ik} = \sum_{j=1}^{n} a_{ij} (b_{jk} + c_{jk})$.
4. By the left distributive law of the [[ring|0894J980RK]] $R$, each term equals $a_{ij} b_{jk} + a_{ij} c_{jk}$.
5. Addition in $R$ is associative and commutative, so the finite sum splits: $(A(B + C))_{ik} = \sum_{j} a_{ij} b_{jk} + \sum_{j} a_{ij} c_{jk}$.
6. The right side of step 5 is $(AB)_{ik} + (AC)_{ik} = (AB + AC)_{ik}$. So $A(B + C) = AB + AC$.
7. For the second identity, write $D = (d_{ij})$, $E = (e_{ij})$ and $G = (g_{jk})$, with the same index ranges. Both $(D + E)G$ and $DG + EG$ are $m \times p$.
8. Fix $i$ and $k$. By definition, $((D + E)G)_{ik} = \sum_{j=1}^{n} (d_{ij} + e_{ij}) g_{jk}$.
9. By the right distributive law of $R$, each term equals $d_{ij} g_{jk} + e_{ij} g_{jk}$.
10. Splitting the finite sum as in step 5 gives $((D + E)G)_{ik} = (DG)_{ik} + (EG)_{ik} = (DG + EG)_{ik}$. So $(D + E)G = DG + EG$.

## Idea

Each entry of a matrix product is a finite sum of products of entries. The distributive law in $R$ splits each product, and the finite sum then splits in two. Both laws are needed because the ring need not be commutative.
