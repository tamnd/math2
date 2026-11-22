---
tag: 9ZQ1GV2F0G
kind: example
name: Nonnegative leading minors do not give semidefiniteness
msc: [15B57, 15A15]
topics: [SS4EVPKT3A]
audience: ug1
not_instance_of:
  - target: 01MMVW8CKC
    note: diag(0, -1) is symmetric, but the form is -1 at (0, 1), so it is not positive semidefinite
illustrates: [0WKEF78PMV]
uses: [0SD528P0EK, 0880F9EQCP]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_criterion
    locator: Proof for the case of positive semidefinite matrices
---

## Example

Let $A = \begin{pmatrix} 0 & 0 \\ 0 & -1 \end{pmatrix}$.
Its leading minors are both $0$, so they pass the test "all leading minors are $\ge 0$", but $A$ is not positive semidefinite.

1. $A$ is real and symmetric.
2. The leading principal [[minors|0SD528P0EK]] are
$$\Delta_1 = a_{11} = 0, \qquad \Delta_2 = 0 \cdot (-1) - 0 \cdot 0 = 0,$$
and both are nonnegative.
3. For $x = e_2 = (0, 1)$ we get $x^{\mathsf{T}} A x = a_{22} = -1 < 0$.
4. So $A$ is not [[positive semidefinite|0880F9EQCP]].
5. The principal minors are $a_{11} = 0$, $a_{22} = -1$ and $\det A = 0$. The minor $a_{22} = -1$ is negative, so the test with all principal minors finds the failure.

## Remarks

The example shows that part 2 of [[Sylvester's criterion|0WKEF78PMV]] needs all principal minors, and not only the leading ones.
The zero in the top left corner hides the entry $-1$ from the $2 \times 2$ minor, since $0 \cdot (-1) = 0$.
Only the principal minor of the bottom right corner looks at $a_{22}$ alone.

The matrix is in fact negative semidefinite, with eigenvalues $0$ and $-1$.
The positive definite test has no such problem, because there a leading minor equal to $0$ already fails the test "all leading minors are positive".
If we change $a_{11}$ from $0$ to $1$, the leading minors become $1$ and $-1$, and now the leading minors detect the failure.

## Explanations

### L1 human

For semidefiniteness, the leading minors can mislead.
Here both leading minors are $0$, which looks harmless.
But the vector $(0, 1)$ gives the value $-1$.

### L2 human

The leading minors look only at the top left corners, and a zero corner can hide everything below it.
For a $2 \times 2$ symmetric $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$, the correct semidefinite test is $a \ge 0$, $c \ge 0$ and $ac - b^2 \ge 0$, with three minors rather than two.
Watch out: the failure needs a leading minor equal to $0$, so it never happens for the positive definite test with strict inequalities.
