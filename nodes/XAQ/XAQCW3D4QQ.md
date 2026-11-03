---
tag: XAQCW3D4QQ
kind: object
name: Pauli matrices
msc: [81R05, 15B57]
uses: [0P17NGQQMQ, 0AR68JTMDT, 0XC1RDBY7A, 5JJYBJ6A8K, E5P8AG6CK7]
sources:
  - url: https://en.wikipedia.org/wiki/Pauli_matrices
same_as:
  wikidata: Q336233
  wikipedia: Pauli matrices
---

## Description

The *Pauli matrices* are the three complex $2 \times 2$ matrices
$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$
They are also written $\sigma_1, \sigma_2, \sigma_3$ or $X, Y, Z$.
Each of them is [[Hermitian|0P17NGQQMQ]] and [[unitary|0AR68JTMDT]], has [[trace|0XC1RDBY7A]] $0$ and determinant $-1$, and has eigenvalues $1$ and $-1$.

## Remarks

They satisfy $\sigma_j^2 = I$ and, for $j, k \in \set{1, 2, 3}$,
$$\sigma_j \sigma_k = \delta_{jk} I + i \sum_{l=1}^{3} \varepsilon_{jkl} \sigma_l,$$
where $\delta_{jk}$ is the Kronecker delta and $\varepsilon_{jkl}$ is the Levi-Civita symbol.
For example, $\sigma_x \sigma_y = i\sigma_z$, as a direct multiplication shows.
Hence $[\sigma_j, \sigma_k] = 2i \sum_l \varepsilon_{jkl}\sigma_l$ and $\sigma_j\sigma_k + \sigma_k\sigma_j = 2\delta_{jk} I$.

The matrices $I, \sigma_x, \sigma_y, \sigma_z$ form a basis of the complex vector space of $2 \times 2$ matrices.
They also form a basis of the real vector space of $2 \times 2$ Hermitian matrices.
The matrices $i\sigma_1, i\sigma_2, i\sigma_3$ form a basis of the [[Lie algebra|5JJYBJ6A8K]] $\mathfrak{su}(2)$ of [[SU(2)|E5P8AG6CK7]].
In quantum mechanics, $\tfrac12 \sigma_j$ are the spin observables of a spin-$\tfrac12$ particle, with $\hbar = 1$.
In quantum computing, $X$ is the bit flip, $Z$ the phase flip, and $Y = iXZ$.

## Explanations

### L1 human

The Pauli matrices are three small matrices that describe the spin of an electron along the three axes of space.
Each one squares to the identity, and any two of them anticommute.
Together with the identity, they are the building blocks of every $2 \times 2$ matrix.
In quantum computing, $X$ swaps $|0\rangle$ and $|1\rangle$, while $Z$ flips the sign of $|1\rangle$.
