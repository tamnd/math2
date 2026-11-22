---
tag: 0ZTKJJDGR7
kind: object
name: Zero matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0VD9ZSWWJG]
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_matrix
    locator: lead section
same_as:
  wikidata: Q338028
  wikipedia: Zero matrix
---

## Description

The zero matrix is the matrix that plays the part of the number $0$: adding it changes nothing, and multiplying by it gives zero.
Let $R$ be a ring and let $m, n \ge 0$ be integers.
The $m \times n$ *zero matrix* over $R$ is the [[matrix|0VD9ZSWWJG]] $0_{m \times n}$ whose entries are all $0$, as the [[formal definition|4KY5AWGMW5]] states.
For example,
$$0_{2 \times 3} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
It is the identity element for [[matrix addition|0Y7H3SAVA1]], so $A + 0 = 0 + A = A$ for every $m \times n$ matrix $A$.
There is one zero matrix for each size, and the size is usually left out of the symbol when the context fixes it.

## Remarks

### Adding zero

Take $A = \begin{pmatrix} 1 & -2 & 0 \\ 3 & 5 & -1 \end{pmatrix}$.
Each entry of $A + 0_{2 \times 3}$ is $a_{ij} + 0 = a_{ij}$, so the sum is $A$ again.
The negative $-A$, with entries $-a_{ij}$, gives $A + (-A) = 0_{2 \times 3}$.
These are the rules for a zero vector, and indeed $0_{m \times n}$ is the zero vector of the [[vector space of m × n matrices|0RE6X3BGPN]].
The [[example with the 2 × 3 zero matrix|DXKTY3ZXK5]] checks them entry by entry.

### Multiplying by zero

The zero matrix also absorbs products.
If $B$ has $n$ rows, then every entry of $0_{m \times n} B$ is a sum of terms $0 \cdot b_{kj}$, so
$$0_{m \times n} B = 0_{m \times p}$$
when $B$ is $n \times p$.
In the same way $A \, 0 = 0$ whenever the product is defined.
The zero matrix is the matrix of the zero linear map $x \mapsto 0$, and this is why it kills every vector: $0_{m \times n} x = 0$ for all $x \in R^n$.

### Products can be zero without a zero factor

For numbers, $ab = 0$ forces $a = 0$ or $b = 0$.
For matrices of order at least 2 this fails.
With
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & -4 \\ -1 & 2 \end{pmatrix},$$
the product $AB$ has entry $(1, 1)$ equal to $1 \cdot 2 + 2 \cdot (-1) = 0$, and the other three entries also vanish.
So $AB = 0$ with $A \ne 0$ and $B \ne 0$, as worked out in [[two nonzero matrices with product zero|WP764BBPKQ]].
A single matrix can even square to zero: $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}^2 = 0$, the [[nonzero matrix with square zero|DXX58EAKG3]].
So for $n \ge 2$ the ring $M_n(R)$ has [[zero divisors|0NNRDW10RZ]] and nonzero [[nilpotent elements|0ZB2JG1M9C]] whenever $R$ is not the zero ring, even when $R$ is a field.

### Watch out

The rule "if $AB = AC$ then $B = C$" is false for matrices.
In the example above, $AB = 0 = A \cdot 0$, but $B \neq 0$.
You may cancel $A$ only when $A$ is [[invertible|0EB9N0S33C]], since then you can multiply both sides on the left by $A^{-1}$.

Also, zero matrices of different sizes are different matrices.
The sum $A + 0_{2 \times 2}$ is not defined for the $2 \times 3$ matrix $A$ above, because the sizes differ.

### Try it

Is $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$ equal to $\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$?
No, because the first is $2 \times 2$ and the second is $2 \times 3$, and equal matrices must have the same size.

Find a nonzero $2 \times 2$ matrix $B$ with $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} B = 0$.
Each column of $B$ must solve $x + y = 0$, so $B = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}$ works.

## Explanations

### L1 human

The zero matrix is the table with $0$ in every position.
It acts like the number $0$: adding it to a table of the same size changes nothing.
There is one zero matrix for each size, such as a $2 \times 2$ one and a $2 \times 3$ one.

### L2 human

The typical use is to read a matrix equation $AB = 0$.
It says that each column of $B$ is a solution of the homogeneous system $Ax = 0$.
For $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the system $x + 2y = 0$, $2x + 4y = 0$ has the solution $(2, -1)$, and any $B$ whose columns are multiples of $(2, -1)^{\mathsf{T}}$ gives $AB = 0$.
The trap is to conclude from $AB = 0$ that $A = 0$ or $B = 0$, which is true for numbers but not for matrices.

### L3 human

The zero matrix is the zero element of the abelian group $M_{m \times n}(R)$, and it is the zero morphism in the category whose morphisms are matrices.
Under the identification of matrices with linear maps $R^n \to R^m$, it is the zero map.
The existence of zero divisors in $M_n(F)$ for $n \ge 2$ is one reason why the matrix ring is not a domain, and the sub-area on [[invertible matrices|P8J6QR66TJ]] studies exactly the matrices that are not zero divisors.
