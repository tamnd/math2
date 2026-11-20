---
tag: ADD4AZEF2Z
kind: proof
name: Proof of the formula for the transpose of a product
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: 09GK5PS824
methods: [0NTF6DMVAP]
uses: [0W809K6AW0, 076JGP6R3T]
sources:
  - url: https://proofwiki.org/wiki/Transpose_of_Matrix_Product
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: Properties
---

## Proof

We compare the two sides entry by entry.

1. Write $A = (a_{ij})$ and $B = (b_{jk})$, with $1 \le i \le m$, $1 \le j \le n$ and $1 \le k \le p$.
2. The [[product|076JGP6R3T]] $AB$ is $m \times p$, so its [[transpose|0W809K6AW0]] $(AB)^{\mathsf{T}}$ is $p \times m$.
3. The matrix $B^{\mathsf{T}}$ is $p \times n$ and $A^{\mathsf{T}}$ is $n \times m$. So $B^{\mathsf{T}} A^{\mathsf{T}}$ is defined and is $p \times m$.
4. Fix $k$ and $i$. By the definitions of the transpose and of the product, $((AB)^{\mathsf{T}})_{ki} = (AB)_{ik} = \sum_{j=1}^{n} a_{ij} b_{jk}$.
5. By the same definitions, $(B^{\mathsf{T}} A^{\mathsf{T}})_{ki} = \sum_{j=1}^{n} (B^{\mathsf{T}})_{kj} (A^{\mathsf{T}})_{ji} = \sum_{j=1}^{n} b_{jk} a_{ij}$.
6. The ring $R$ is commutative, so $b_{jk} a_{ij} = a_{ij} b_{jk}$ for each $j$. So the sums in steps 4 and 5 are equal.
7. Thus $(AB)^{\mathsf{T}}$ and $B^{\mathsf{T}} A^{\mathsf{T}}$ have the same size and the same entries, so $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$.

## Idea

Entry $(k, i)$ of each side is a sum over $j$ of the products of $a_{ij}$ and $b_{jk}$.
On the right the two factors come in the other order.
Commutativity of $R$ makes the two sums equal.

## Variants

- Over a field, a proof by duality is possible. The matrix of a dual map is the transpose, and $(g \circ f)^* = f^* \circ g^*$; see [[this statement|0ZPB3180AY]].
- A proof by matrix units checks the rule on $E_{ij} E_{kl} = \delta_{jk} E_{il}$ and extends it by bilinearity; see [[matrix units|A4HTT7JFD1]].
