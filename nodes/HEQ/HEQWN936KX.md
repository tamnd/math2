---
tag: HEQWN936KX
kind: definition
name: Matrix product state
msc: [81P40, 82B20, 15A69]
defines: H578T160KS
uses: [EY0X2NKA3S, 09VMDSRXWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_product_state
---

## Definition

Let $N \ge 1$ and $d \ge 1$, and let $\mathcal{H} = (\C^d)^{\otimes N}$ be the [[tensor product|EY0X2NKA3S]] with basis vectors $\lvert i_1 i_2 \cdots i_N \rangle$, $i_k \in \set{1, \dots, d}$.
Let $D_0 = D_N = 1$ and let $D_1, \dots, D_{N-1}$ be positive integers.
For $1 \le k \le N$ and $1 \le i \le d$, let $A_k^{[i]}$ denote a complex matrix of size $D_{k-1} \times D_k$.
A vector $\psi \in \mathcal{H}$ is a *matrix product state* (with open boundary conditions) with bond dimensions $D_1, \dots, D_{N-1}$ if there are such matrices with
$$\psi = \sum_{i_1, \dots, i_N = 1}^{d} A_1^{[i_1]} A_2^{[i_2]} \cdots A_N^{[i_N]} \, \lvert i_1 i_2 \cdots i_N \rangle.$$
The product of matrices in each term is a $1 \times 1$ matrix, that is, a number.
The number $D = \max_k D_k$ is the *bond dimension*.
For periodic boundary conditions, all matrices are $D \times D$ and the coefficient is $\tr(A_1^{[i_1]} \cdots A_N^{[i_N]})$.

## Remarks

Every vector of $\mathcal{H}$ is a matrix product state with $D_k = \min(d^k, d^{N-k})$, obtained by successive [[singular value|09VMDSRXWJ]] decompositions.
The least possible $D_k$ for a given $\psi$ is the rank of $\psi$ seen as a $d^k \times d^{N-k}$ matrix.
This is the Schmidt rank of $\psi$ across the cut between sites $k$ and $k+1$.

Example: the vector $\lvert 0 \cdots 0 \rangle + \lvert 1 \cdots 1 \rangle$ in $(\C^2)^{\otimes N}$, with basis labels $0, 1$, is a periodic matrix product state with $D = 2$.
Take $A_k^{[0]} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $A_k^{[1]} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ for every $k$.
The product $A^{[i_1]} \cdots A^{[i_N]}$ is zero unless all $i_k$ are equal, and then its trace is $1$.
The ground state of the [[AKLT model|WDHPPAGR65]] is another standard example, with $d = 3$ and $D = 2$.

Non-example: the same vector, for $N \ge 2$, is not a matrix product state with $D = 1$.
With $D = 1$ the coefficient factorises as $A_1^{[i_1]} \cdots A_N^{[i_N]}$, so $\psi$ is a product vector, and the coefficient matrix of $\psi$ across the first cut has rank $2$, not $1$.
