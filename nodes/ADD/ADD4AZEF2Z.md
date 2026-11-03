---
tag: ADD4AZEF2Z
kind: proof
name: Proof of the formula for the transpose of a product
msc: [15A99]
proves: 09GK5PS824
uses: [0W809K6AW0, 076JGP6R3T]
sources:
  - url: https://proofwiki.org/wiki/Transpose_of_Matrix_Product
---

## Proof

We compare the two sides entry by entry.

1. Write $A = (a_{ij})$ and $B = (b_{jk})$, with $1 \le i \le m$, $1 \le j \le n$ and $1 \le k \le p$.
2. The [[product|076JGP6R3T]] $AB$ is $m \times p$, so its [[transpose|0W809K6AW0]] $(AB)^T$ is $p \times m$.
3. The matrix $B^T$ is $p \times n$ and $A^T$ is $n \times m$. So $B^T A^T$ is defined and is $p \times m$.
4. Fix $k$ and $i$. By the definition of the transpose, $((AB)^T)_{ki} = (AB)_{ik} = \sum_{j=1}^{n} a_{ij} b_{jk}$.
5. By the definitions of the product and the transpose, $(B^T A^T)_{ki} = \sum_{j=1}^{n} (B^T)_{kj} (A^T)_{ji} = \sum_{j=1}^{n} b_{jk} a_{ij}$.
6. The ring $R$ is commutative, so $b_{jk} a_{ij} = a_{ij} b_{jk}$ for each $j$. So the sums in steps 4 and 5 are equal.
7. Thus $(AB)^T$ and $B^T A^T$ have the same size and the same entries, so $(AB)^T = B^T A^T$.

## Idea

Entry $(k, i)$ of each side is a sum over $j$ of the products of $a_{ij}$ and $b_{jk}$. On the right the two factors come in the other order, so commutativity of $R$ makes the two sums equal.
