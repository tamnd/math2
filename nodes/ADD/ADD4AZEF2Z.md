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

We show that the two sides have the same size and then compare them entry by entry.

1. Write $A = (a_{ij})$ and $B = (b_{jk})$, with $1 \le i \le m$, $1 \le j \le n$ and $1 \le k \le p$.
2. The [[product|076JGP6R3T]] $AB$ is $m \times p$, so by the definition of the [[transpose|0W809K6AW0]] the matrix $(AB)^{\mathsf{T}}$ is $p \times m$.
3. The matrix $B^{\mathsf{T}}$ is $p \times n$ and $A^{\mathsf{T}}$ is $n \times m$, so the product $B^{\mathsf{T}} A^{\mathsf{T}}$ is defined and is also $p \times m$.
4. Fix $k$ and $i$; by the definition of the transpose and then of the product,
$$\bigl((AB)^{\mathsf{T}}\bigr)_{ki} = (AB)_{ik} = \sum_{j=1}^{n} a_{ij} b_{jk}.$$
5. By the definition of the product and then of the transpose,
$$(B^{\mathsf{T}} A^{\mathsf{T}})_{ki} = \sum_{j=1}^{n} (B^{\mathsf{T}})_{kj} (A^{\mathsf{T}})_{ji} = \sum_{j=1}^{n} b_{jk} a_{ij}.$$
6. The ring $R$ is commutative, so $b_{jk} a_{ij} = a_{ij} b_{jk}$ for each $j$, and the sums in steps 4 and 5 are equal.
7. The two matrices have the same size by steps 2 and 3, and the same entries by step 6, so $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$.

## Idea

Entry $(k, i)$ of each side is the sum over $j$ of the products of $a_{ij}$ and $b_{jk}$.
On the right the two factors of each product come in the other order, and commutativity of $R$ is exactly what makes the two sums equal.
The order of the matrices is reversed so that the sizes match; the order of the numbers inside each product is reversed as a side effect.

## Variants

Over a field, there is a proof by duality.
The [[matrix of the dual map is the transpose|0ZPB3180AY]] of the matrix of the map, and the dual of a composite is $(g \circ f)^* = f^* \circ g^*$ because $\varphi \circ (g \circ f) = (\varphi \circ g) \circ f$ for every linear form $\varphi$.
Taking matrices of both sides gives the theorem.

A third proof uses [[matrix units|A4HTT7JFD1]].
Both sides are bilinear in $(A, B)$, so it is enough to check the rule for $A = E_{ij}$ and $B = E_{kl}$.
There $(E_{ij} E_{kl})^{\mathsf{T}} = \delta_{jk} E_{li}$ and $E_{kl}^{\mathsf{T}} E_{ij}^{\mathsf{T}} = E_{lk} E_{ji} = \delta_{kj} E_{li}$, which agree.
