---
tag: SF3EBT2Z4F
kind: example
name: The Fourier matrix of size three
aliases: [dft-matrix-of-size-three]
msc: ["15B57", "42A38"]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [0AR68JTMDT]
illustrates: [GZ7NG7J3J8]
uses: [0D6RMJ10M9, 0EX045E2BP, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/DFT_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Unitary_matrix
    locator: Properties
---

## Example

Let $\omega = e^{2\pi i/3} = -\frac{1}{2} + \frac{\sqrt{3}}{2} i$, so that $\omega^3 = 1$, $\overline{\omega} = \omega^2$ and $1 + \omega + \omega^2 = 0$.
The Fourier matrix of size three is
$$F = \frac{1}{\sqrt{3}} \begin{pmatrix} 1 & 1 & 1 \\ 1 & \omega & \omega^2 \\ 1 & \omega^2 & \omega \end{pmatrix},$$
with entries $F_{jk} = \frac{1}{\sqrt{3}} \omega^{jk}$ for $j, k = 0, 1, 2$; the entry $\omega^4$ is written as $\omega$.
We show that $F$ is [[unitary|0D6RMJ10M9]], and we find its eigenvalues and its determinant.

1. Column $k$ is $c_k = \frac{1}{\sqrt{3}} (1, \omega^k, \omega^{2k})$. Each entry has absolute value $\frac{1}{\sqrt{3}}$, so $\lVert c_k \rVert^2 = 3 \cdot \frac{1}{3} = 1$.
2. For $j \ne k$, the inner product of two columns is
$$\langle c_k, c_j \rangle = \frac{1}{3} \sum_{m=0}^{2} \omega^{mk} \, \overline{\omega^{mj}} = \frac{1}{3} \sum_{m=0}^{2} \left( \omega^{k - j} \right)^m.$$
3. Here $\omega^{k - j}$ is $\omega$ or $\omega^2$, and in both cases the sum is $1 + \omega + \omega^2 = 0$, because $\omega^4 = \omega$.
4. So the columns are orthonormal, and $F$ is unitary.
5. The entry in position $(j, k)$ of $F^2$ is $\frac{1}{3} \sum_m \omega^{m(j + k)}$, which is $1$ when $3$ divides $j + k$ and $0$ otherwise, by the same sum. So
$$F^2 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix},$$
the swap of the second and third coordinates, and $F^4 = (F^2)^2 = I_3$.
6. The swap has the eigenvalues $1$, $1$ and $-1$. Since $F$ is unitary, it is diagonalizable, and the eigenvalues of $F^2$ are the squares of those of $F$. So two eigenvalues of $F$ lie in $\{1, -1\}$, and one lies in $\{i, -i\}$.
7. The trace is the sum of the eigenvalues, and
$$\operatorname{tr} F = \frac{1}{\sqrt{3}} (1 + \omega + \omega) = \frac{1 + 2\omega}{\sqrt{3}} = \frac{i\sqrt{3}}{\sqrt{3}} = i.$$
8. The two eigenvalues in $\{1, -1\}$ add up to $2$, $0$ or $-2$, and the third adds $\pm i$, so the only way to get $i$ is $1$, $-1$ and $i$.
9. So the eigenvalues of $F$ are $1$, $-1$ and $i$, and $\det F = 1 \cdot (-1) \cdot i = -i$.

## Remarks

The example illustrates [[the properties of unitary matrices|GZ7NG7J3J8]]: the eigenvalues and the [[determinant|0C3CFHDN6R]] $-i$ all lie on the unit circle.
It also shows that the determinant of a unitary matrix need not be $\pm 1$.

The map $x \mapsto Fx$ is the discrete Fourier transform of length $3$, with the scaling $\frac{1}{\sqrt{3}}$ that makes it unitary.
The matrix is symmetric, $F^{\mathsf{T}} = F$, but it is not Hermitian, because $F^* = \overline{F} \ne F$.
For each $n$ the Fourier matrix $\frac{1}{\sqrt{n}} (\omega_n^{jk})$ with $\omega_n = e^{2\pi i/n}$ is unitary by the same computation, and its fourth power is $I_n$.

## Explanations

### L1 human

The Fourier matrix splits a list of three numbers into three waves.
Each column is one wave, made from the cube roots of $1$.
The three waves are perpendicular in complex space, and each has length $1$.
So the matrix keeps the length of every list.

### L2 human

The typical use of a unitary transform is that it keeps the energy $\sum_k \lvert x_k \rvert^2$ of a signal.
For $x = (1, 0, 0)$ we get $Fx = \frac{1}{\sqrt{3}} (1, 1, 1)$, and both vectors have squared length $1$.
For $x = (1, 1, 1)$ we get $Fx = (\sqrt{3}, 0, 0)$, by step 3, and both have squared length $3$.
Watch out: without the factor $\frac{1}{\sqrt{3}}$ the columns have length $\sqrt{3}$, so the matrix is not unitary, although its columns are still orthogonal.
