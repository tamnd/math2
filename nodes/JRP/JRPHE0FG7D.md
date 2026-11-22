---
tag: JRPHE0FG7D
kind: example
name: A complex orthogonal matrix that is not unitary
msc: ["15B57", "15B10"]
topics: [AZS5BPF5H3]
audience: ug2
not_instance_of:
  - target: 0AR68JTMDT
    note: the plain transpose gives the identity, but the conjugate transpose does not
uses: [0D6RMJ10M9, 0EX045E2BP, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_matrix
    locator: lead section
---

## Example

Let $N = \begin{pmatrix} \sqrt{2} & i \\ -i & \sqrt{2} \end{pmatrix}$.
We show that $N^TN = I_2$ with the plain [[transpose|0W809K6AW0]], and that $N$ is still not [[unitary|0D6RMJ10M9]].

1. The transpose is $N^T = \begin{pmatrix} \sqrt{2} & -i \\ i & \sqrt{2} \end{pmatrix}$.
2. Multiply, using $i^2 = -1$: $N^TN = \begin{pmatrix} 2 + (-i)(-i) & \sqrt{2}\,i - i\sqrt{2} \\ i\sqrt{2} - \sqrt{2}\,i & i \cdot i + 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
3. The [[conjugate transpose|0EX045E2BP]] conjugates every entry of $N^T$, so $N^* = \begin{pmatrix} \sqrt{2} & i \\ -i & \sqrt{2} \end{pmatrix} = N$.
4. Then $N^*N = N^2 = \begin{pmatrix} 2 + i(-i) & \sqrt{2}\,i + i\sqrt{2} \\ -i\sqrt{2} - \sqrt{2}\,i & (-i)(i) + 2 \end{pmatrix} = \begin{pmatrix} 3 & 2\sqrt{2}\,i \\ -2\sqrt{2}\,i & 3 \end{pmatrix} \ne I_2$.
5. So $N$ is not unitary. For example, its first column $(\sqrt{2}, -i)$ has length $\sqrt{\abs{\sqrt 2}^2 + \abs{-i}^2} = \sqrt{3}$, not $1$.

## Remarks

The matrix $N$ is a complex orthogonal matrix, since $N^TN = I$ over $\C$.
These matrices form the group $O(2, \C)$, and that group is not compact, because its entries can be as large as we like.
The condition $N^TN = I$ uses the bilinear form $\sum_k x_ky_k$, which is not an inner product over $\C$.
For example, $(1, i)$ has $1^2 + i^2 = 0$ although it is not the zero vector.

The matrix is also Hermitian, $N^* = N$.
Its trace is $2\sqrt 2$ and its determinant is $2 - i(-i) = 2 - 1 = 1$, so its eigenvalues are the roots of $t^2 - 2\sqrt 2\, t + 1$, namely $\sqrt{2} \pm 1$.
These are real and off the unit circle, which confirms again that $N$ is not unitary.
For a real matrix the two tests $Q^TQ = I$ and $Q^*Q = I$ agree, so the difference only shows with complex entries.

## Explanations

### L1 human

Over the complex numbers, the length of a vector uses complex conjugates, as in $\abs{a + bi}^2 = a^2 + b^2$.
The plain transpose forgets the conjugates.
So a test with the plain transpose can pass while the matrix still stretches some vectors.
This matrix stretches its first column to length $\sqrt{3}$.

### L2 human

Compare the two tests on the first column $c = (\sqrt 2, -i)$ alone.
The bilinear test multiplies the entries without conjugation, and the Hermitian test conjugates one factor:
$$c^T c = 2 + (-i)^2 = 1, \qquad c^* c = 2 + \overline{(-i)}(-i) = 2 + 1 = 3.$$
The first number looks like a unit length, but only the second number is a squared length.
So before you call a complex matrix unitary, conjugate its entries and then test.
Watch out: the bilinear "length" $c^Tc$ can even be $0$ for a nonzero vector, as for $(1, i)$.
