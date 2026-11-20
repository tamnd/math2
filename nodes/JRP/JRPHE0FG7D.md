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
We show that $N^TN = I_2$ with the plain [[transpose|0W809K6AW0]], but $N$ is not [[unitary|0D6RMJ10M9]].

1. $N^T = \begin{pmatrix} \sqrt{2} & -i \\ i & \sqrt{2} \end{pmatrix}$.
2. $N^TN = \begin{pmatrix} 2 + (-i)(-i) & \sqrt{2}\,i - i\sqrt{2} \\ i\sqrt{2} - \sqrt{2}\,i & i \cdot i + 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
3. The [[conjugate transpose|0EX045E2BP]] is $N^* = \overline{N^T} = \begin{pmatrix} \sqrt{2} & i \\ -i & \sqrt{2} \end{pmatrix} = N$.
4. $N^*N = N^2 = \begin{pmatrix} 2 + i(-i) & \sqrt{2}\,i + i\sqrt{2} \\ -i\sqrt{2} - \sqrt{2}\,i & (-i)(i) + 2 \end{pmatrix} = \begin{pmatrix} 3 & 2\sqrt{2}\,i \\ -2\sqrt{2}\,i & 3 \end{pmatrix} \neq I_2$.
5. So $N$ is not unitary. For example, its first column $(\sqrt{2}, -i)$ has length $\sqrt{2 + 1} = \sqrt{3}$.

## Remarks

- $N$ is a complex orthogonal matrix: it satisfies $N^TN = I$ over $\C$. These matrices form the group $O(2, \C)$, which is not compact.
- The condition $N^TN = I$ uses the bilinear form $\sum_k x_ky_k$, which is not an inner product over $\C$. For example, $(1, i)$ has $1^2 + i^2 = 0$.
- $N$ is Hermitian, $N^* = N$, with eigenvalues $\sqrt{2} \pm 1$. These are not on the unit circle.

## Explanations

### L1 human

Over the complex numbers, the length of a vector uses complex conjugates.
The plain transpose forgets the conjugates.
So a test with the plain transpose can pass, while the matrix still stretches some vectors.
This matrix stretches its first column to length $\sqrt{3}$.

### L2 human

The worked check is in the Example.
The typical use: always conjugate the entries before you test a complex matrix.
A trap: for a real matrix, the two tests agree, so the error only shows with complex entries.
