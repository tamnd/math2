---
tag: 2E4BS58WEV
kind: definition
name: Evolution algebra
msc: [17D92, 17D99]
defines: DNK00D7M6F
uses: [60W3THKGA7, HFXWYNFB9A, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Genetic_algebra
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] and let $A$ be a [[nonassociative algebra|60W3THKGA7]] over $K$.
The algebra $A$ is an *evolution algebra* if it has a basis $(e_i)_{i \in I}$ such that:

1. $e_i e_j = 0$ for all $i, j \in I$ with $i \ne j$.
2. For each $i \in I$, $e_i^2 = \sum_{k \in I} a_{ik} e_k$ for scalars $a_{ik} \in K$, only finitely many of them nonzero.

Such a basis is a *natural basis*, and the $a_{ik}$ are the [[structure constants|HFXWYNFB9A]] of $A$ in it.

## Remarks

Example: $A = K^2$ with basis $e_1, e_2$, products $e_1 e_2 = e_2 e_1 = 0$ and $e_1^2 = e_2$, $e_2^2 = e_1$.
Both clauses hold by construction.
This algebra is not associative: $(e_1 e_1) e_2 = e_2^2 = e_1$, while $e_1 (e_1 e_2) = 0$.

Non-example: the algebra $M_2(K)$ of $2 \times 2$ matrices.
In an evolution algebra the products of basis vectors satisfy $e_i e_j = e_j e_i$, so by bilinearity the algebra is commutative.
Matrix multiplication is not commutative, so no basis of $M_2(K)$ satisfies the clauses.

A real evolution algebra is called nonnegative when all its structure constants $a_{ik}$ are nonnegative.
