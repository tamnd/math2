---
tag: AGCF7KC5V0
kind: definition
name: Quantum relative entropy
msc: [81P17, 94A17]
defines: 4V9R81KPF7
uses: [V1JTB52E8C, 0XC1RDBY7A, FS339MCFEQ, PQBW43X5RE, H53TSRFWQ4]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_relative_entropy
---

## Definition

Let $H$ be a finite-dimensional complex Hilbert space, and let $\rho$ and $\sigma$ be [[density matrices|V1JTB52E8C]] on $H$.
The support of a positive semidefinite operator is the orthogonal complement of its kernel.
The *quantum relative entropy* of $\rho$ with respect to $\sigma$ is
$$S(\rho \| \sigma) = \tr\big(\rho \log \rho\big) - \tr\big(\rho \log \sigma\big)$$
if the support of $\rho$ is contained in the support of $\sigma$.
Otherwise $S(\rho \| \sigma) = +\infty$.
Here $\tr$ is the [[trace|0XC1RDBY7A]], and $\log \sigma$ is the [[matrix logarithm|FS339MCFEQ]] of $\sigma$ on its support.

## Remarks

Example: for $\sigma = I/d$ with $d = \dim H$, one has $\log \sigma = -(\log d) I$.
So $S(\rho \| I/d) = \log d - S(\rho)$, where $S$ is the [[von Neumann entropy|H53TSRFWQ4]].

Non-example of finiteness: for $\rho = |0\rangle\langle 0|$ and $\sigma = |1\rangle\langle 1|$ on $\C^2$, the support of $\rho$ is not contained in that of $\sigma$, so $S(\rho \| \sigma) = +\infty$.

If $\rho$ and $\sigma$ commute, they are diagonal in a common basis with eigenvalues $p_i$ and $q_i$.
Then $S(\rho\|\sigma) = \sum_i p_i \log(p_i / q_i)$, the [[Kullback–Leibler divergence|PQBW43X5RE]] of the two distributions.

Klein's inequality gives $S(\rho \| \sigma) \ge 0$, with equality exactly when $\rho = \sigma$.
For every quantum channel $\Phi$, $S(\Phi(\rho) \| \Phi(\sigma)) \le S(\rho \| \sigma)$; this is the monotonicity, or data processing inequality.
