---
tag: AVTQZC769M
kind: example
name: A matrix with eigenvalues in {0, 1} that is not idempotent
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 0KCE8CG86P
    note: diag(1, (0, 1; 0, 0)) has eigenvalues 1, 0, 0, but its square differs from it in the entry (2, 3)
uses: [0K7TD9BV2D, 0M0SNKZ482]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: Properties
---

## Example

Let
$$M = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$
over the real numbers.
Its eigenvalues are those of a projection, and yet $M$ is not [[idempotent|0K7TD9BV2D]].

1. The matrix is upper triangular, so its eigenvalues are its diagonal entries $1, 0, 0$, all in $\{0, 1\}$.
2. The matrix is [[block diagonal|0M0SNKZ482]], with the $1 \times 1$ block $(1)$ and the $2 \times 2$ block $J = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. Block diagonal matrices square block by block.
3. The blocks square to $(1)$ and $J^2 = 0$, so
$$M^2 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
4. The entry $(2, 3)$ of $M^2$ is $0$, and that of $M$ is $1$. So $M^2 \ne M$, and $M$ is not idempotent.

## Remarks

The block $J$ is nilpotent, and it hides behind the eigenvalue $0$.
It also stops $M$ from being diagonalizable, while every idempotent matrix over a field is diagonalizable.
So eigenvalues in $\{0, 1\}$ are necessary for idempotency, but not sufficient; the matrix must also be diagonalizable.

The rule "trace equals rank" fails as well: $\operatorname{tr} M = 1$, but $M$ has the two independent nonzero rows $(1, 0, 0)$ and $(0, 0, 1)$, so its rank is $2$.
If we replace the entry $1$ in position $(2, 3)$ by $0$, we get $\operatorname{diag}(1, 0, 0)$, which is idempotent.

## Explanations

### L1 human

The eigenvalues of $M$ are $1$, $0$ and $0$, the same as for the projection $\operatorname{diag}(1, 0, 0)$.
But squaring $M$ removes the $1$ above the diagonal, so $M$ changes when we apply it twice.
A projection never changes when we apply it twice, so $M$ is not a projection.

### L2 human

The eigenvalues control only the diagonal part of a triangular matrix.
A nilpotent part above the diagonal is invisible to them.
Watch out: to prove that a matrix is idempotent, compute $P^2$, or show that it is diagonalizable with eigenvalues in $\{0, 1\}$; the eigenvalues alone prove nothing.
