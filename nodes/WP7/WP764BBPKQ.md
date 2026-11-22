---
tag: WP764BBPKQ
kind: example
name: Two nonzero matrices with product zero
msc: ["15A99", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0NNRDW10RZ]
uses: [4KY5AWGMW5, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Zero_divisor
    locator: Examples
---

## Example

For numbers, a product is zero only when one factor is zero, and two real $2 \times 2$ matrices show that this rule fails for matrices.
Let
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & -4 \\ -1 & 2 \end{pmatrix}$$
over $\mathbb{R}$.
Both matrices are nonzero, since $a_{11} = 1$ and $b_{11} = 2$.

1. Row 1 of $A$ is $(1, 2)$. Multiply it by the two columns of $B$:
$$1 \cdot 2 + 2 \cdot (-1) = 0, \qquad 1 \cdot (-4) + 2 \cdot 2 = 0.$$
2. Row 2 of $A$ is $(2, 4)$. Multiply it by the two columns of $B$:
$$2 \cdot 2 + 4 \cdot (-1) = 0, \qquad 2 \cdot (-4) + 4 \cdot 2 = 0.$$
3. So $AB$ is the [[zero matrix|4KY5AWGMW5]] $0_{2 \times 2}$, and $A$ is a left [[zero divisor|0NNRDW10RZ]] in $M_2(\mathbb{R})$, with $B$ as a right zero divisor.
4. In the other order, row times column gives
$$BA = \begin{pmatrix} 2 - 8 & 4 - 16 \\ -1 + 4 & -2 + 8 \end{pmatrix} = \begin{pmatrix} -6 & -12 \\ 3 & 6 \end{pmatrix} \neq 0.$$
5. Cancellation fails: $AB = 0 = A \cdot 0$, but $B \neq 0$.

## Remarks

Why does it work?
The second row of $A$ is twice the first, so both rows are multiples of $(1, 2)$.
Each column of $B$ is a multiple of $(2, -1)^{\mathsf{T}}$, and $(1, 2) \cdot (2, -1) = 0$.
So every row of $A$ is perpendicular to every column of $B$, and every entry of $AB$ is zero.

In the language of later pages, $A$ is not [[invertible|0EB9N0S33C]], and the columns of $B$ lie in the null space of $A$.
If we change the entry $a_{22}$ from $4$ to $5$, the rows of $A$ are no longer proportional, $A$ becomes invertible, and $AB = 0$ then forces $B = 0$.
Step 4 also shows that $AB$ and $BA$ can differ even when one of them is zero.

## Explanations

### L1 human

For numbers, if a product is zero, then one of the factors is zero.
For matrices this rule fails.
Here neither table is all zeros, but each row of the first table cancels against each column of the second, and the product is all zeros.

### L2 human

To build such a pair yourself, start with a matrix $A$ whose rows are proportional, so that $Ax = 0$ has a nonzero solution.
For $A$ above, the equation $x + 2y = 0$ gives the solution $(2, -1)$.
Any $B$ whose columns are multiples of $(2, -1)^{\mathsf{T}}$ then gives $AB = 0$, because the product is computed one column of $B$ at a time.
The typical use of the example is as a warning: from $AB = AC$ you may not conclude $B = C$ unless $A$ is invertible.
