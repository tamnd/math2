---
tag: 8B8Y3DYGYT
kind: example
name: The entrywise square is not the matrix square
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
not_instance_of:
  - target: 032Q9FB8MT
    note: squaring each entry of (1, 2; 3, 4) gives (1, 4; 9, 16), but the matrix product of the matrix with itself is (7, 10; 15, 22)
uses: [076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
    locator: lead section
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ over $\mathbb{R}$.
We show that squaring each entry does not give the [[matrix product|032Q9FB8MT]] $A^2 = AA$.

1. Squaring each entry gives
$$\begin{pmatrix} 1^2 & 2^2 \\ 3^2 & 4^2 \end{pmatrix} = \begin{pmatrix} 1 & 4 \\ 9 & 16 \end{pmatrix}.$$
2. By the [[product rule|076JGP6R3T]], each entry of $A^2$ is a row of $A$ times a column of $A$:
$$A^2 = \begin{pmatrix} 1 \cdot 1 + 2 \cdot 3 & 1 \cdot 2 + 2 \cdot 4 \\ 3 \cdot 1 + 4 \cdot 3 & 3 \cdot 2 + 4 \cdot 4 \end{pmatrix} = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}.$$
3. The two results differ in every entry, so the entrywise square is not the matrix square.

## Remarks

The entrywise product is a different operation, the [[Hadamard product|SQT6QCEXZ8]] $A \circ A$.
The two squares agree for [[diagonal matrices|044JNC7ZAA]]: for $D = \operatorname{diag}(2, 5)$ both give $\operatorname{diag}(4, 25)$, because the off-diagonal terms are all zero.
That special case is one reason the error is common.

The general entry shows what the entrywise square leaves out:
$$(A^2)_{11} = a_{11} a_{11} + a_{12} a_{21}.$$
The term $a_{12} a_{21}$ mixes entries from different places, and the entrywise square has no such term.
In some software, `A^2` or `A**2` means the entrywise power and a separate command gives the matrix power, so check the convention before you compute.

## Explanations

### L1 human

Squaring a matrix does not mean squaring its numbers one by one.
It means multiplying the matrix by itself with the row-times-column rule.
For the matrix with rows $(1, 2)$ and $(3, 4)$, the top-left entry of the square is $1 \cdot 1 + 2 \cdot 3 = 7$, not $1$.

### L2 human

To see the difference in a use, let $A$ describe one step of a process, such as moving between two states.
Then $A^2$ describes two steps, and an entry of $A^2$ adds up all the ways to go through an intermediate state.
The entrywise square only squares the weight of each single step, and that number has no meaning as two steps.
Watch out: the same mistake in reverse also fails, since $\sqrt{A}$ is not found by taking the square root of each entry.
