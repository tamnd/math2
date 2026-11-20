---
tag: C2VQGVYVE8
kind: proof
name: Proof that a product of symmetric matrices is symmetric if and only if they commute
msc: ["15A99", "15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: YX9Z3E9SGN
methods: [0NTF6DMVAP]
uses: [0N28QN4CYA, 09GK5PS824, MX26N71ZD3]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_matrix
    locator: Properties
---

## Proof

Let $A$ and $B$ be symmetric $n \times n$ matrices over a commutative ring $R$.

1. By the [[transpose of a product|09GK5PS824]], $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$.
2. By the [[definition of a symmetric matrix|0N28QN4CYA]], $B^{\mathsf{T}} = B$ and $A^{\mathsf{T}} = A$. So $(AB)^{\mathsf{T}} = BA$.
3. Suppose that $AB$ is symmetric. Then $AB = (AB)^{\mathsf{T}} = BA$ by step 2, so $A$ and $B$ [[commute|MX26N71ZD3]].
4. Conversely, suppose that $AB = BA$. Then $(AB)^{\mathsf{T}} = BA = AB$ by step 2, so $AB$ is symmetric.
5. Steps 3 and 4 give the two directions of the equivalence.

## Idea

The transpose reverses products, and for symmetric factors it does nothing else.
So the transpose of $AB$ is $BA$, and symmetry of $AB$ is the equation $AB = BA$.
