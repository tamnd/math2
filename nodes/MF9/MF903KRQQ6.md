---
tag: MF903KRQQ6
kind: definition
name: Quantum inverse scattering method
msc: [81R12, 82B23, 37K15]
defines: ZQ3ZZ9AQR1
uses: [663BP8ZHS5, 0BF2DE2SYK, 07PTPSZPME]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_inverse_scattering_method
---

## Definition

Let $V = \C^2$ be the auxiliary space and let $\mathcal{H} = V_1 \otimes \dots \otimes V_N$ be the quantum space, a [[tensor product|0BF2DE2SYK]] of copies $V_n$ of $\C^2$.
Let $R(\lambda) \in \End(V \otimes V)$, for $\lambda \in \C$, be a solution of the [[Yang–Baxter equation|663BP8ZHS5]] with spectral parameter:
$$R_{12}(\lambda - \mu) R_{13}(\lambda) R_{23}(\mu) = R_{23}(\mu) R_{13}(\lambda) R_{12}(\lambda - \mu).$$
The method consists of the following steps.

1. Choose Lax operators $L_{0n}(\lambda) \in \End(V_0 \otimes V_n)$ that satisfy $R_{00'}(\lambda - \mu) L_{0n}(\lambda) L_{0'n}(\mu) = L_{0'n}(\mu) L_{0n}(\lambda) R_{00'}(\lambda - \mu)$, where $V_0, V_{0'}$ are two copies of $V$.
2. Form the monodromy matrix $T_0(\lambda) = L_{0N}(\lambda) \cdots L_{01}(\lambda)$ and the transfer matrix $t(\lambda) = \tr_0 T_0(\lambda) \in \End(\mathcal{H})$, the partial [[trace|07PTPSZPME]] over $V_0$.
3. Write $T_0(\lambda) = \begin{pmatrix} A(\lambda) & B(\lambda) \\ C(\lambda) & D(\lambda) \end{pmatrix}$ with entries in $\End(\mathcal{H})$. Take a reference vector $\Omega$ with $C(\lambda) \Omega = 0$ for all $\lambda$. Look for eigenvectors of all $t(\mu)$ of the form $B(\lambda_1) \cdots B(\lambda_M) \Omega$.

## Remarks

From step 1 the monodromy matrix satisfies the same relation, $R(\lambda - \mu) T(\lambda) T'(\mu) = T'(\mu) T(\lambda) R(\lambda - \mu)$, and when $R(\lambda - \mu)$ is invertible taking traces gives $[t(\lambda), t(\mu)] = 0$ for all $\lambda, \mu$.
So $t(\lambda)$ is a generating function of commuting conserved quantities.
The vector $B(\lambda_1) \cdots B(\lambda_M) \Omega$ is an eigenvector exactly when the $\lambda_j$ satisfy the Bethe equations; this step is called the algebraic Bethe ansatz.
Example: for the XXX chain one takes $R(\lambda) = \lambda I + i P$, with $P$ the flip of $\C^2 \otimes \C^2$, and $L_{0n}(\lambda) = \lambda I + i P_{0n}$.
Then $L_{0n}(0) = i P_{0n}$, and the Heisenberg Hamiltonian is, up to additive and multiplicative constants, the logarithmic derivative $\frac{d}{d\lambda} \log t(\lambda)$ at $\lambda = 0$.
Non-example: an arbitrary $L_{0n}(\lambda)$ without the relation of step 1 gives transfer matrices that in general do not commute, and no conserved quantities follow.
