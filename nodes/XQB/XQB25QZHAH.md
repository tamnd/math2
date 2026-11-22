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

The simplest matrices give the simplest maps, and every linear map is built from them.
Let $V = \mathbb{R}^3$ with the standard basis $(e_1, e_2, e_3)$, and let $W = \mathbb{R}^2$ with the standard basis $(f_1, f_2)$.
For $1 \le i \le 2$ and $1 \le j \le 3$, let $E_{ij}$ be the $2 \times 3$ [[matrix unit|4H93XF4RVH]] with entry $1$ in place $(i, j)$ and $0$ elsewhere.

1. The only nonzero column of $E_{ij}$ is column $j$, and it equals $f_i$, so the [[linear map of E_ij|009892PZ30]] sends $e_j$ to $f_i$ and $e_k$ to $0$ for $k \ne j$; call it $T_{ij}$.
2. For example, $E_{21} = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}$ gives $T_{21}(x, y, z) = x f_2 = (0, x)$.
3. Each $2 \times 3$ matrix is $A = \sum_{i,j} a_{ij} E_{ij}$ in exactly one way, with the entries of $A$ as coefficients, as in this case:
$$\begin{pmatrix} 1 & 0 & 4 \\ 2 & -1 & 0 \end{pmatrix} = E_{11} + 4E_{13} + 2E_{21} - E_{22}.$$
4. The map of $A$ is the same combination of the $T_{ij}$, which in the example gives:
$$(T_{11} + 4T_{13} + 2T_{21} - T_{22})(x, y, z) = (x, 0) + (4z, 0) + (0, 2x) - (0, y) = (x + 4z, 2x - y).$$
5. Check: the matrix product gives $A(x, y, z)^{\mathsf{T}} = (x + 0y + 4z, 2x - y + 0z)^{\mathsf{T}}$, the same vector.
6. Steps 3 and 4 show that the six maps $T_{ij}$ span the [[space of linear maps|0VPCJWGMP9]] $\Hom(\mathbb{R}^3, \mathbb{R}^2)$.
7. They are also independent: if $\sum c_{ij} T_{ij} = 0$, then applying it to $e_j$ gives $c_{1j} f_1 + c_{2j} f_2 = 0$, so every $c_{ij} = 0$.
8. So the $T_{ij}$ form a basis, and $\dim \Hom(\mathbb{R}^3, \mathbb{R}^2) = 6 = 3 \cdot 2$.

## Remarks

The example shows the [[theorem on linear maps and matrices|Q3EDKTZ6TA]] at work.
The step from matrices to maps keeps sums and scalar multiples, as in step 4, and an isomorphism sends a basis to a basis.
The matrix units are the standard basis of $M_{2 \times 3}(\mathbb{R})$, so their maps are a basis of $\Hom(\mathbb{R}^3, \mathbb{R}^2)$.

Each $T_{ij}$ has rank $1$, since its image is the line through $f_i$.
Not every map of rank $1$ is a multiple of one $T_{ij}$: the map of $\begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \end{pmatrix}$ has rank $1$ but needs the four units $E_{11}$, $E_{12}$, $E_{21}$ and $E_{22}$.
In general, for spaces of dimensions $n$ and $m$ with any bases, the same construction gives $mn$ maps, and so $\dim \Hom(V, W) = mn$.

## Explanations

### L1 human

The simplest matrices have one entry $1$ and all others $0$.
Their maps send one basis vector to one basis vector and send the others to zero.
For example, one of them sends $(x, y, z)$ to $(0, x)$.
Every other linear map from $\mathbb{R}^3$ to $\mathbb{R}^2$ is a combination of these six simple maps, with the entries of its matrix as the amounts.

### L2 human

The isomorphism between linear maps and matrices sends a basis to a basis.
The standard basis of the matrix space is the set of matrix units, so their maps $T_{ij}$ form a basis of the space of linear maps, and $\dim \Hom(V, W) = \dim V \cdot \dim W$.
Steps 6 to 8 check this directly, without the theorem.
Watch out: the map $T_{ij}$ goes from $e_j$ to $f_i$, so the column index $j$ belongs to the domain and the row index $i$ to the target.
