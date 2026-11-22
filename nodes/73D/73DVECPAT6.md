---
tag: 73DVECPAT6
kind: statement
role: theorem
name: Four fundamental subspaces
aliases: [four-fundamental-subspaces, fundamental-theorem-of-linear-algebra]
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
about: [03AJKXH1AV, 069MCGX635, 0PHDYNR24D]
uses: [0F0RPPJ2TT, 0EP73HK4C4, 0PQ2GGY1QV, 0EWQEYRVA8, 0W809K6AW0, 079D68S3AW]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_linear_algebra
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Relation to the null space
  - book: isbn:9781733146678
    locator: Chapter 3
---

## Statement

Every matrix carries four subspaces, two in the space of inputs and two in the space of outputs, and the rank alone fixes all four dimensions.
Let $F$ be a field, let $A$ be an $m \times n$ matrix over $F$, and let $r = \operatorname{rank} A$.
The four fundamental subspaces of $A$ are the [[column space|03AJKXH1AV]] $\operatorname{Col}(A) \subseteq F^m$, the [[null space|0PHDYNR24D]] $\operatorname{Null}(A) \subseteq F^n$, the [[row space|069MCGX635]] $\operatorname{Row}(A) \subseteq F^n$ and the left null space $\operatorname{Null}(A^{\mathsf{T}}) \subseteq F^m$.

1. Their dimensions are $r$, $n - r$, $r$ and $m - r$, in this order.
2. For $F = \mathbb{R}$ with the dot product, $\operatorname{Null}(A) = \operatorname{Row}(A)^\perp$ and $\operatorname{Null}(A^{\mathsf{T}}) = \operatorname{Col}(A)^\perp$.
3. For $F = \mathbb{R}$, $\mathbb{R}^n = \operatorname{Row}(A) \oplus \operatorname{Null}(A)$ and $\mathbb{R}^m = \operatorname{Col}(A) \oplus \operatorname{Null}(A^{\mathsf{T}})$.
4. For $F = \mathbb{R}$, the map $x \mapsto Ax$ restricts to a linear isomorphism from $\operatorname{Row}(A)$ onto $\operatorname{Col}(A)$.

## Remarks

### Why each hypothesis is needed

Part 1 holds over every field, but parts 2 to 4 need the real dot product, or another positive definite product.
Over $\mathbb{F}_2$, the matrix $A = \begin{pmatrix} 1 & 1 \end{pmatrix}$ has its row $(1, 1)$ in its own null space, since $1 + 1 = 0$.
So $\operatorname{Row}(A) \cap \operatorname{Null}(A) \ne \{0\}$, and the direct sum of part 3 fails.

The same happens over $\mathbb{C}$ if we keep the bilinear product $x^{\mathsf{T}} y$.
For $A = \begin{pmatrix} 1 & i \end{pmatrix}$, the row $(1, i)$ satisfies $1 \cdot 1 + i \cdot i = 0$, so it lies in the null space.
Over $\mathbb{C}$, parts 2 to 4 hold again once $A^{\mathsf{T}}$ is replaced by the [[conjugate transpose|0DXKE10PHF]] $A^*$ and the dot product by the Hermitian product.

### What it gives you

The theorem collects several results of the sub-area in one place.
Part 1 contains the [[rank-nullity theorem for matrices|TR48YQGCCA]], $r + (n - r) = n$, and the theorem that [[row rank equals column rank|0TZAG60ZYT]].
Part 2 contains the theorem that the [[orthogonal complement of the column space is the null space of the transpose|J4SZVFBHS5]].
With part 3 it gives the [[Fredholm alternative|4HH8C9V8JQ]]: $Ax = b$ is solvable exactly when $b$ is orthogonal to $\operatorname{Null}(A^{\mathsf{T}})$.

For a worked use, take the [[3 by 4 matrix of rank 2|7GTMB5E3TA]] with rows $(1, 2, 0, 1)$, $(2, 4, 1, 4)$ and $(3, 6, 1, 5)$.
Its four subspaces have dimensions $2, 2, 2, 1$, and the check $2 + 2 = 4$ and $2 + 1 = 3$ confirms part 1.
The left null space is the line through $(-1, -1, 1)$, so $Ax = b$ is solvable exactly when $b_3 = b_1 + b_2$.

### The converse

The four dimensions depend only on $m$, $n$ and $r$.
So two $m \times n$ matrices have subspaces of the same four dimensions exactly when they have the same rank, which means that they are [[equivalent matrices|0CMHSGTWXB]].
The four subspaces themselves do not determine $A$, since $A$ and $2A$ have the same four subspaces.

### Generalizations

For a linear map $T \colon V \to W$, the four spaces become $\operatorname{im} T$, $\ker T$, and the image and kernel of the [[dual map|0AZ5ARP287]] $T^*$.
The orthogonality of part 2 becomes the statement that $\ker T^*$ is the annihilator of $\operatorname{im} T$, and in that form it holds over every field.
For a map between inner product spaces, the [[adjoint|0R9NMSM1ZP]] plays the role of $A^{\mathsf{T}}$.

## History

Strang made the four subspaces and the picture of part 4 the organizing idea of his textbooks, and he called the whole result the fundamental theorem of linear algebra.

## Explanations

### L1 human

Every matrix has four subspaces attached to it.
Two live in the input space: the row space and the null space.
Two live in the output space: the column space and the left null space.
Their sizes are fixed by the rank and by the shape of the matrix.
For a $3 \times 4$ matrix of rank $2$, the sizes are $2$ and $2$ in the input space and $2$ and $1$ in the output space.

### L2 human

Here is the picture of parts 3 and 4 with numbers, for the $3 \times 4$ matrix above.
The row space has the basis $u_1 = (1, 2, 0, 1)$ and $u_2 = (0, 0, 1, 2)$, so we split $x = (1, 0, 0, 0)$ as a row space part plus a null space part.
The row space part $a u_1 + b u_2$ must have the same dot products with $u_1$ and $u_2$ as $x$, which gives
$$6a + 2b = 1, \qquad 2a + 5b = 0,$$
so $a = \tfrac{5}{26}$ and $b = -\tfrac{1}{13}$.
The row space part is $\tfrac{1}{26}(5, 10, -2, 1)$, and the null space part is $\tfrac{1}{26}(21, -10, 2, -1)$.
Check: $A$ sends the null space part to $0$, for example row 2 gives $42 - 40 + 2 - 4 = 0$, and it sends the row space part to $(1, 2, 3) = Ax$.
The matrix kills the null space part and carries the row space part to the column space, one to one.
Watch out: this splitting uses the dot product, so it is a real picture and has no meaning over $\mathbb{F}_2$.

### L3 human

The four subspaces are the images and kernels of $A$ and of $A^{\mathsf{T}}$.
Over any field, $\operatorname{Null}(A^{\mathsf{T}})$ is the annihilator of $\operatorname{Col}(A)$ under the standard pairing $(y, b) \mapsto y^{\mathsf{T}} b$ of $F^m$ with itself.
Over $\mathbb{R}$ this pairing is positive definite, so the annihilator is a complement, and that is the only place where the real numbers enter.
The isomorphism of part 4 is the starting point of the pseudoinverse and of the singular value decomposition, which choose orthonormal bases of the row space and the column space adapted to $A$.
