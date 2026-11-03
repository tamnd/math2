---
tag: G8SRQ9SKQZ
kind: definition
name: Von Neumann entropy
msc: [81P17, 94A17]
defines: H53TSRFWQ4
uses: [V1JTB52E8C, 0XC1RDBY7A, FS339MCFEQ, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann_entropy
---

## Definition

Let $H$ be a complex Hilbert space of finite dimension $d$, and let $\rho$ be a [[density matrix|V1JTB52E8C]] on $H$.
Let $\lambda_1, \dots, \lambda_d$ be the [[eigenvalues|0BQAA2BK3Q]] of $\rho$, counted with multiplicity.
The *von Neumann entropy* of $\rho$ is
$$S(\rho) = -\tr(\rho \log \rho) = -\sum_{i=1}^{d} \lambda_i \log \lambda_i,$$
with the convention $0 \log 0 = 0$.
Here $\tr$ is the [[trace|0XC1RDBY7A]], and $\rho \log \rho$ is defined by functional calculus, which agrees with the [[matrix logarithm|FS339MCFEQ]] on the support of $\rho$.

## Remarks

The base of the logarithm fixes the unit: base $2$ gives bits, base $e$ gives nats.

Example: for the maximally mixed state $\rho = I/d$, all eigenvalues equal $1/d$, so $S(\rho) = -d \cdot \tfrac1d \log \tfrac1d = \log d$.
For a pure state $|\psi\rangle\langle\psi|$, the eigenvalues are $1, 0, \dots, 0$, so $S = 0$.

Non-example: the Shannon entropy of the diagonal entries is not $S(\rho)$ in general.
For $\rho = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, a pure state, the diagonal entries $\tfrac12, \tfrac12$ give $\log 2$, while $S(\rho) = 0$.

Always $0 \le S(\rho) \le \log d$, with $S(\rho) = 0$ exactly for pure states and $S(\rho) = \log d$ exactly for $\rho = I/d$.
The entropy is invariant under unitary conjugation, $S(U\rho U^*) = S(\rho)$, and it is concave in $\rho$.
