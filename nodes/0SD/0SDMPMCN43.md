---
tag: 0SDMPMCN43
kind: definition
name: Multilinear map
msc: [15A69]
defines: 0443XNARDV
uses: [0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Multilinear_map
    locator: lead section
---

## Definition

Let $F$ be a field, let $n \ge 1$, and let $V_1, \dots, V_n$ and $W$ be vector spaces over $F$.
A map $f \colon V_1 \times \cdots \times V_n \to W$ is *multilinear* when it is linear in each variable separately.
That is, for each $i$ and each fixed choice of $v_j \in V_j$ for $j \ne i$, the map $v \mapsto f(v_1, \dots, v_{i-1}, v, v_{i+1}, \dots, v_n)$ is a [[linear map|0NRYHJPQG2]] $V_i \to W$.

## Remarks

For $n = 1$, a multilinear map is a linear map, and for $n = 2$ it is a *bilinear map*.
The dot product on $\R^n$ and the matrix product $M_n(F) \times M_n(F) \to M_n(F)$ are bilinear.
The [[determinant|00KDZRW4C0]] is multilinear in the $n$ columns of a matrix.
A multilinear map is in general not linear on the product space: $f(2v_1, 2v_2) = 4 f(v_1, v_2)$ for a bilinear $f$.

## Explanations

### L1 human

A multilinear map takes several vectors and is linear in each one, while the others stay fixed.
The product $xy$ of two real numbers is a simple example: it is linear in $x$ and linear in $y$.
It is not linear in the pair $(x, y)$.
