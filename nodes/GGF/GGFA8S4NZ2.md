---
tag: GGFA8S4NZ2
kind: example
name: A Hermitian 2 × 2 matrix and its real eigenvalues
msc: ["15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0P17NGQQMQ]
uses: [0EKZCX4K3P]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Properties
---

## Example

Let $A = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix}$.

1. $A^* = \begin{pmatrix} \overline{2} & \overline{1 + i} \\ \overline{1 - i} & \overline{3} \end{pmatrix} = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix} = A$, so $A$ is [[Hermitian|0EKZCX4K3P]].
2. The diagonal entries $2$ and $3$ are real.
3. For $x = (x_1, x_2)$, $x^* A x = 2|x_1|^2 + 3|x_2|^2 + 2 \operatorname{Re}\big((1 - i)\, \overline{x_1} x_2\big)$, a real number.
4. The characteristic polynomial is $t^2 - 5t + (6 - (1 - i)(1 + i)) = t^2 - 5t + 4 = (t - 1)(t - 4)$.
5. So the eigenvalues are $1$ and $4$, both real.
6. For $\lambda = 4$, take $v = (1 - i, 2)$. Then $Av = \big(2(1 - i) + 2(1 - i),\ (1 + i)(1 - i) + 6\big) = (4 - 4i, 8) = 4v$.

## Remarks

The real eigenvalues agree with the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]], which belongs to a later topic.

## Explanations

### L1 human

The mirror entries $1 - i$ and $1 + i$ are complex conjugates, and the diagonal is real.
That is what makes the matrix Hermitian.

### L2 human

The determinant $6 - |1 - i|^2 = 4$ and the trace $5$ are real.
For a $2 \times 2$ Hermitian matrix the discriminant $(a - d)^2 + 4|b|^2$ is never negative, so the eigenvalues are always real.
