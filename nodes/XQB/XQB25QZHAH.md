---
tag: XQB25QZHAH
kind: example
name: The linear maps of the matrix units form a basis of Hom(V, W)
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
instance_of: [06HMCTAQH3]
illustrates: [Q3EDKTZ6TA]
uses: [009892PZ30, 4H93XF4RVH, 0VPCJWGMP9]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_unit
    locator: lead section
---

## Example

Let $V = \R^3$ with the standard basis $(e_1, e_2, e_3)$, and $W = \R^2$ with the standard basis $(f_1, f_2)$.
For $1 \le i \le 2$ and $1 \le j \le 3$, let $E_{ij}$ be the [[matrix unit|4H93XF4RVH]] with entry $1$ at $(i, j)$ and $0$ elsewhere.

1. The [[linear map of $E_{ij}$|009892PZ30]] sends $e_j$ to $f_i$, and $e_k$ to $0$ for $k \ne j$. Call it $T_{ij}$.
2. For example, $E_{21} = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}$ gives $T_{21}(x, y, z) = (0, x)$.
3. Each $2 \times 3$ matrix is $A = \sum_{i,j} a_{ij} E_{ij}$ in exactly one way. For example, $\begin{pmatrix} 1 & 0 & 4 \\ 2 & -1 & 0 \end{pmatrix} = E_{11} + 4E_{13} + 2E_{21} - E_{22}$.
4. The map of $A$ is the same combination of the $T_{ij}$. In the example, $(T_{11} + 4T_{13} + 2T_{21} - T_{22})(x, y, z) = (x + 4z,\ 2x - y)$.
5. Check: $A(x, y, z) = (x + 0y + 4z,\ 2x - y + 0z)$, the same.
6. So the six maps $T_{ij}$ form a basis of the [[space of linear maps|0VPCJWGMP9]] $\Hom(\R^3, \R^2)$, and its dimension is $6 = 3 \cdot 2$.

## Remarks

- The step from matrices to maps preserves sums and scalar multiples, as in step 4. This is the linearity in the [[theorem on linear maps and matrices|Q3EDKTZ6TA]].
- $T_{ij}$ has rank $1$. Every map of rank $1$ is a sum of such maps, but in general not a multiple of one $T_{ij}$.

## Explanations

### L1 human

The simplest matrices have one entry $1$ and all others $0$.
Their maps send one basis vector to one basis vector and kill the others.
Every other linear map is a combination of these simple maps.

### L2 human

The isomorphism between linear maps and matrices sends a basis to a basis.
The standard basis of the matrix space is the set of matrix units.
So their maps $T_{ij}$ are a basis of the space of linear maps, and $\dim \Hom(V, W) = \dim V \cdot \dim W$.
