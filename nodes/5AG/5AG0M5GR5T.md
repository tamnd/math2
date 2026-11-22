---
tag: 5AG0M5GR5T
kind: example
name: The plain transpose of a nonzero complex vector can give length zero
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 0DXKE10PHF
    note: for x = (1, i) the plain transpose gives xᵀx = 0, so xᵀ is not the conjugate transpose and does not measure length
uses: [0W809K6AW0, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_transpose
    locator: Properties
---

## Example

The plain transpose of a complex vector is not its conjugate transpose, and it fails to measure length.
Let
$$x = \begin{pmatrix} 1 \\ i \end{pmatrix} \in \mathbb{C}^2.$$

1. The plain [[transpose|0W809K6AW0]] writes the column as a row with no other change: $x^{\mathsf{T}} = \begin{pmatrix} 1 & i \end{pmatrix}$.
2. Multiply this row by the column $x$:
$$x^{\mathsf{T}} x = 1 \cdot 1 + i \cdot i = 1 - 1 = 0.$$
3. The vector $x$ is not zero, since its first entry is $1$. So $x^{\mathsf{T}} x$ cannot be the squared length of $x$.
4. The [[conjugate transpose|0EX045E2BP]] conjugates the second entry: $x^* = \begin{pmatrix} 1 & -i \end{pmatrix}$. Then
$$x^* x = 1 \cdot 1 + (-i) \cdot i = 1 + 1 = 2,$$
the correct squared length $|1|^2 + |i|^2$.

## Remarks

The two products differ by one sign, but the sign decides whether a length can be zero for a nonzero vector.
A nonzero vector with $x^{\mathsf{T}} x = 0$ is called isotropic for the bilinear form $(x, y) \mapsto x^{\mathsf{T}} y$.
Such vectors exist in $\mathbb{C}^n$ for every $n \ge 2$: the vector $(1, i, 0, \dots, 0)$ is one.
So $x^{\mathsf{T}} y$ is not an inner product on $\mathbb{C}^n$.
For $n = 1$ there is no isotropic vector, because $z^2 = 0$ forces $z = 0$, but $z^2$ is still not $|z|^2$: for $z = i$ it is $-1$.
Over $\mathbb{R}$ the two products agree, since every entry is its own conjugate.

## Explanations

### L1 human

Without conjugates, the squares of complex numbers can cancel each other.
Here $1^2 + i^2 = 1 + (-1) = 0$, although the vector is not zero.
A length should be zero only for the zero vector, so this formula is the wrong one for complex vectors.

### L2 human

The form $x^{\mathsf{T}} y$ on $\mathbb{C}^n$ is symmetric and bilinear, but it is not positive definite, and step 2 shows the failure.
The Hermitian form $y^* x$ is positive definite by the computation of [[the length example|THMQA9AQZK]].
That is why complex linear algebra uses $A^*$ wherever real linear algebra uses $A^{\mathsf{T}}$, for example in the definition of [[Hermitian matrices|0P17NGQQMQ]].
Watch out: a computer algebra system may use the plain transpose for a command that you expect to conjugate, so check which one it computes.
