---
tag: 0PBY4E9GQF
kind: concept
name: Skew-symmetric matrix
aliases: [antisymmetric-matrix]
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0JXZKX526R]
uses: [0JXZKX526R, 09DXWYRD43]
sources:
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: Properties
same_as:
  wikidata: Q526790
  wikipedia: Skew-symmetric matrix
inventory: [2FP1241FAJ]
---

## Summary

A skew-symmetric matrix is a [[square matrix|0JXZKX526R]] whose [[transpose|09DXWYRD43]] is its negative: $A^{\mathsf{T}} = -A$.
The [[formal definition|03RNVFDEAN]] says $a_{ji} = -a_{ij}$ for all $i$ and $j$.
Outside characteristic $2$, the diagonal of a skew-symmetric matrix is $0$.
Each square matrix is the sum of a [[symmetric|0VR671PHE5]] and a skew-symmetric matrix in one way only, [[when 2 is invertible|~3a63c44b]].

## Motivation

The cross product with a fixed vector $v \in \mathbb{R}^3$ is a linear map, and its matrix is skew-symmetric.
Skew-symmetric matrices are the infinitesimal rotations: for a real skew-symmetric $K$, the matrix $e^{tK}$ is orthogonal for every $t$.
They also give the alternating bilinear forms, such as the symplectic form.

## Notation

- Other names are *antisymmetric* and *skew*.
- Some books write $\mathfrak{so}(n)$ or $\operatorname{Skew}_n(F)$ for the set of skew-symmetric $n \times n$ matrices.

## Remarks

### Examples

- [[The cross product matrix of a vector in R³|~bb248cc8]].
- [[The symmetric and skew-symmetric parts of a 2 × 2 matrix|~c08f8568]].
- $\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}$ is skew-symmetric, and so is the zero matrix.

### Non-examples

- [[A matrix with zero diagonal that is symmetric over the reals|~dc2b7786]] is not skew-symmetric.
- $\begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix}$ is not skew-symmetric over $\mathbb{R}$, because $a_{11} = 1 \neq -a_{11}$.

### Basic properties

Let $A$ and $B$ be skew-symmetric $n \times n$ matrices over a commutative ring $R$.

- $A + B$ and $cA$ are skew-symmetric for $c \in R$.
- Each diagonal entry satisfies $2 a_{ii} = 0$. So $a_{ii} = 0$ when $2$ is not a zero divisor in $R$, for example over $\mathbb{R}$.
- The commutator $AB - BA$ is skew-symmetric, because $(AB - BA)^{\mathsf{T}} = BA - AB$ by the [[transpose of a product|09GK5PS824]].
- $A^2$ is symmetric, because $(A^2)^{\mathsf{T}} = (-A)^2 = A^2$.
- If $A$ has zero diagonal, then $x^{\mathsf{T}} A x = 0$ for each column vector $x$, because the terms $a_{ij} x_i x_j$ and $a_{ji} x_j x_i$ cancel.
- Over a field of characteristic not $2$, a skew-symmetric matrix of odd order has [[determinant|00KDZRW4C0]] $0$. The reason is $\det A = \det A^{\mathsf{T}} = \det(-A) = (-1)^n \det A$.
- Over a field of characteristic not $2$, the skew-symmetric matrices form a subspace of dimension $n(n-1)/2$.

### Common errors

- Assuming that the diagonal is $0$ in characteristic $2$. There $-1 = 1$, so skew-symmetric means symmetric, and $I$ is skew-symmetric.
- Taking a zero diagonal as enough. The off-diagonal entries must also be negatives of each other.

## Explanations

### L1 human

In a skew-symmetric matrix, the entry across the diagonal is the negative of the entry here.
Over the real numbers this forces zeros on the diagonal, because only $0$ equals its own negative.

### L2 human

The condition $A^{\mathsf{T}} = -A$ means $(Ax) \cdot y = -(x \cdot Ay)$ for all $x$ and $y$.
Taking $y = x$ gives $(Ax) \cdot x = 0$ over $\mathbb{R}$, so $Ax$ is always perpendicular to $x$.
This is why $\dot x = Ax$ keeps the length of $x$ constant: the motion is a rotation.

### L3 human

The skew-symmetric matrices are the Lie algebra $\mathfrak{so}(n)$ of the orthogonal group, with the commutator as bracket.
In general, $A$ is the matrix of an alternating form if and only if $A^{\mathsf{T}} = -A$ and the diagonal is $0$; in characteristic $2$ the second condition is extra.
