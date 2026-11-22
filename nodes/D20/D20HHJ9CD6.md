---
tag: D20HHJ9CD6
kind: example
name: A family of involutory 2 × 2 matrices with a free parameter
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [NH2QE3671N]
uses: [1GVCRBXQT8, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Involutory_matrix
    locator: lead section
---

## Example

For a real number $c$, let
$$A_c = \begin{pmatrix} 1 & 0 \\ c & -1 \end{pmatrix}.$$
We show that every $A_c$ is involutory and find the two lines it acts on.

1. Multiply row by column:
$$A_c^2 = \begin{pmatrix} 1 \cdot 1 + 0 \cdot c & 1 \cdot 0 + 0 \cdot (-1) \\ c \cdot 1 + (-1) \cdot c & c \cdot 0 + (-1)(-1) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.$$
2. So $A_c$ is [[involutory|1GVCRBXQT8]] for every $c$.
3. For a vector, $A_c (x, y) = (x, cx - y)$. So $A_c (2, c) = (2, 2c - c) = (2, c)$, and the line spanned by $(2, c)$ is fixed.
4. Also $A_c (0, 1) = (0, -1)$, so the $y$-axis is reversed.
5. So $A_c$ is the reflection that fixes the line spanned by $(2, c)$ and reverses the $y$-axis.

## Remarks

For $c = 0$ we get $\operatorname{diag}(1, -1)$, the reflection in the $x$-axis.
For $c \ne 0$ the two lines are not perpendicular, since $(2, c) \cdot (0, 1) = c$.
Then $A_c$ is an oblique reflection: it is not symmetric, and it is not an orthogonal matrix.

The family shows that the equation $A^2 = I$ has infinitely many solutions among real $2 \times 2$ matrices, while the only real numbers with $x^2 = 1$ are $\pm 1$.
Check one case, $c = 4$: the vector $(1, 1)$ goes to $(1, 3)$, and then to $(1, 4 - 3) = (1, 1)$.

## Explanations

### L1 human

The square of each of these matrices is the identity, whatever the number $c$ is.
So there are many matrices that undo themselves, one for each $c$, and not only $I$ and $-I$.

### L2 human

A reflection of the plane is fixed by its two eigenlines, the $+1$ line and the $-1$ line, and these can be any two different lines through $0$.
Here the $-1$ line stays on the $y$-axis while the $+1$ line turns with $c$.
Watch out: a reflection in this wide sense need not preserve lengths; $A_4$ sends $(1, 1)$, of length $\sqrt 2$, to $(1, 3)$, of length $\sqrt{10}$.
