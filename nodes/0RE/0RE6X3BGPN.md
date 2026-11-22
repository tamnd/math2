---
tag: 0RE6X3BGPN
kind: example
name: Space of matrices
msc: ["15A03"]
topics: [MVH97H8B2J, Y1ESNQ2V52]
audience: ug1
instance_of: [000AYPA9AJ, 0Y7H3SAVA1]
uses: [0N1MY1T0W9, 0BVXADM10P, 0K28YXMS7Q, 05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Examples_of_vector_spaces
    locator: Matrices
  - book: isbn:9780134860244
    locator: Section 1.2
---

## Example

The matrices of one fixed size form a vector space, because they are added and scaled one entry at a time, just like lists of numbers.
Let $F$ be a field, let $m, n \ge 1$, and let $M_{m \times n}(F)$ be the set of $m \times n$ [[matrices|0VD9ZSWWJG]] with entries in $F$.
The operations are [[matrix addition|0Y7H3SAVA1]] and [[scalar multiplication|09V6DDACXR]], both entry by entry:
$$(A + B)_{ij} = A_{ij} + B_{ij}, \qquad (aA)_{ij} = a A_{ij}.$$
For $1 \le i \le m$ and $1 \le j \le n$, the *matrix unit* $E_{ij}$ has entry $1$ in position $(i, j)$ and $0$ in every other position.
We show that $M_{m \times n}(F)$ is a [[vector space|000AYPA9AJ]] over $F$ and that the $mn$ matrix units form a [[basis|0KCQ9Y3QKA]].

1. Closure: by the [[definition of the sum|0BVXADM10P]] and the [[definition of the scalar multiple|0K28YXMS7Q]], both results are again $m \times n$ matrices over $F$.
2. Axioms: each of the eight axioms of the [[definition|05EGHEQZAW]] is an equation between matrices, so it holds when it holds in every entry $(i, j)$. In each entry it is a rule of the field $F$, as in the check for the [[coordinate space|713F6AM1X1]] $F^{mn}$.
3. Zero and negatives: the zero vector is the [[zero matrix|0ZTKJJDGR7]], and the negative of $A$ is $-A$, with entries $-A_{ij}$. So $M_{m \times n}(F)$ is a vector space over $F$.
4. Spanning: every matrix is $A = \sum_{i, j} A_{ij} E_{ij}$. Both sides have the entry $A_{ij}$ in position $(i, j)$, since only $E_{ij}$ is nonzero there.
5. Independence: if $\sum_{i, j} c_{ij} E_{ij} = 0$, then the entry of the left side in position $(i, j)$ is $c_{ij}$. So every $c_{ij} = 0$.
6. Dimension: the basis has $mn$ elements, so $\dim M_{m \times n}(F) = mn$ by the definition of [[dimension|03GSZ8RTZJ]].

For $2 \times 2$ matrices the basis expansion reads
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} = aE_{11} + bE_{12} + cE_{21} + dE_{22},$$
so the dimension is $4$.

## Remarks

### Matrices are coordinate vectors in a square

The map that lists the entries of a matrix row by row is a [[linear isomorphism|0B8T10CE7N]] $M_{m \times n}(F) \to F^{mn}$.
For example, it sends $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ to $(1, 2, 3, 4)$.
So every fact about $F^{mn}$ as a vector space holds for matrices, and only the layout differs.
The space $M_{m \times n}(F)$ is also isomorphic to the [[space of linear maps|0X9MBPP2Z3]] from $F^n$ to $F^m$, which is the reason to arrange the entries in a rectangle.

### Subspaces cut out by linear conditions

A set of matrices given by linear equations in the entries is a subspace.
The [[symmetric matrices|0VR671PHE5]] in $M_{n \times n}(F)$ form a subspace of dimension $n(n + 1)/2$, with basis $E_{ii}$ and $E_{ij} + E_{ji}$ for $i < j$.
For $n = 2$ that basis is $E_{11}$, $E_{22}$ and $E_{12} + E_{21}$, and $3 = 2 \cdot 3/2$.
The matrices with [[trace|0XC1RDBY7A]] $0$ form a subspace of dimension $n^2 - 1$, since the single equation $a_{11} + \dots + a_{nn} = 0$ removes one dimension.

### What is not a subspace

The invertible matrices do not form a subspace, because they do not contain the zero matrix.
They are not closed under addition either: $I_2 + (-I_2) = 0$.
Matrix multiplication is not part of the vector space structure; with it, $M_{n \times n}(F)$ becomes an algebra, the [[matrix ring|AB2MD5CD13]].

## Explanations

### L1 human

Matrices of one fixed size can be added and scaled, entry by entry, so they form a vector space.
A $2 \times 2$ matrix holds four numbers, so this space has dimension $4$.
It is $F^4$ written as a square instead of a row.

### L2 human

We find the coordinates of $A = \begin{pmatrix} 3 & -1 \\ 0 & 2 \end{pmatrix}$ in the basis of matrix units.

1. The entries are $A_{11} = 3$, $A_{12} = -1$, $A_{21} = 0$ and $A_{22} = 2$.
2. So $A = 3E_{11} - E_{12} + 0E_{21} + 2E_{22}$.
3. Check the position $(1, 2)$: only $E_{12}$ has a nonzero entry there, and its coefficient is $-1$.

The typical use is to treat sets of matrices with linear conditions as subspaces, as in the remarks above.
A trap: the dimension of $M_{m \times n}(F)$ is $mn$, not $m + n$ and not $\max(m, n)$.

### L3 human

In terms of tensor products, $M_{m \times n}(F) \cong F^m \otimes F^n$, with $E_{ij} = e_i \otimes e_j$; see [[tensor product of vector spaces|0BF2DE2SYK]].
The matrix units multiply by the rule $E_{ij} E_{kl} = \delta_{jk} E_{il}$, which describes the algebra $M_n(F)$ completely.
