---
tag: J8ZFANVA99
kind: statement
role: theorem
name: Knill–Laflamme conditions
msc: [81P73, 81P70]
uses: [M4BSARXSCC, 10VZYJ4552, SFX7B478FE, 0P17NGQQMQ]
about: [M4BSARXSCC]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_error_correction
---

## Statement

Let $H$ be a finite-dimensional complex Hilbert space, let $\mathcal{C} \subseteq H$ be a subspace, and let $P$ be the orthogonal projection onto $\mathcal{C}$.
Let $\mathcal{N}$ be a [[quantum channel|10VZYJ4552]] on the operators of $H$ with [[Kraus representation|SFX7B478FE]] $\mathcal{N}(\rho) = \sum_{a=1}^{r} E_a \rho E_a^*$.
Then $\mathcal{C}$ [[corrects|M4BSARXSCC]] $\mathcal{N}$ if and only if there are complex numbers $c_{ab}$ such that
$$P E_a^* E_b P = c_{ab} P \quad \text{for all } a, b \in \set{1, \dots, r}.$$
In that case the matrix $(c_{ab})$ is [[Hermitian|0P17NGQQMQ]] and positive semidefinite.

## Remarks

Proof idea: if a recovery $\mathcal{R}$ with Kraus operators $R_k$ exists, then $R_k E_a P = \lambda_{ka} P$ for scalars $\lambda_{ka}$, and $P E_a^* E_b P = \sum_k \overline{\lambda_{ka}} \lambda_{kb} P$.
Conversely, diagonalise $(c_{ab})$ by a unitary change of Kraus operators to get $F_a$ with $P F_a^* F_b P = d_a \delta_{ab} P$.
Then the subspaces $F_a \mathcal{C}$ with $d_a > 0$ are mutually orthogonal copies of $\mathcal{C}$.
The recovery measures which subspace holds the state and maps it back to $\mathcal{C}$ by the partial isometry $d_a^{-1/2} P F_a^*$.

Example: the three-qubit bit-flip code $\mathcal{C} = \operatorname{span}\set{\lvert 000 \rangle, \lvert 111 \rangle}$ and the Kraus operators $\sqrt{p_0} I$ and $\sqrt{p_i} X_i$ for $i = 1, 2, 3$.
For $i \ne j$, $X_i X_j$ and $X_i$ map $\mathcal{C}$ to a space orthogonal to $\mathcal{C}$, so $P X_i X_j P = 0$ and $P X_i P = 0$, while $P X_i X_i P = P$.
So the conditions hold, with $(c_{ab})$ diagonal.

The conditions depend only on the linear span of the $E_a$.
So a code that corrects every error in a set $\set{E_a}$ corrects every channel with Kraus operators in their span.

## Explanations

### L1 human

The theorem gives a test, using only linear algebra, for whether a quantum code can undo a given kind of noise.
The condition says that the errors may move the code space around, but they must not distort the encoded information in a way that depends on the encoded state.
In particular, no measurement of the errors can reveal anything about the encoded state.

### L2 human

The conditions are the starting point of most constructions of quantum codes.
A code has distance $d$ when the conditions hold for all Pauli errors of weight at most $d - 1$ in the role of $E_a^* E_b$.
Then it corrects arbitrary errors on any $\lfloor (d-1)/2 \rfloor$ qubits.
For [[stabilizer codes|P2TBJXVGEC]] the conditions become a simple check on the commutation of Pauli operators with the stabilizer.
When $(c_{ab})$ is not of full rank, the code is called degenerate: different errors act in the same way on it.
