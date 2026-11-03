---
tag: N3HMVPF808
kind: definition
name: POVM
msc: [81P15, 81P16, 46N50]
defines: 33BRW6TMY4
uses: [HM2HHE3J51, 77020CY5ZW, ATGT25E5FF, V1JTB52E8C]
sources:
  - url: https://en.wikipedia.org/wiki/POVM
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] and let $(\Omega, \Sigma)$ be a measurable space.
A *positive operator-valued measure*, or *POVM*, on $(\Omega, \Sigma)$ is a map $F$ from $\Sigma$ to the bounded operators on $\mathcal{H}$ such that:

1. $F(E)$ is a [[positive operator|77020CY5ZW]] for every $E \in \Sigma$;
2. $F(\Omega) = I$, the identity operator;
3. for every sequence $(E_k)$ of pairwise disjoint sets in $\Sigma$ and all $\psi, \varphi \in \mathcal{H}$, $\langle \psi, F(\bigcup_k E_k)\varphi \rangle = \sum_k \langle \psi, F(E_k)\varphi \rangle$.

When $\Omega = \set{1, \dots, n}$, a POVM is the same as a list of positive operators $F_1, \dots, F_n$ with $F_1 + \dots + F_n = I$.
For a [[density operator|V1JTB52E8C]] $\rho$, the probability of an outcome in $E$ is $\tr(\rho F(E))$.

## Remarks

Example: on $\C^2$ let $u_k = (\cos(2\pi k/3), \sin(2\pi k/3))$ for $k = 0, 1, 2$, and $F_k = \tfrac{2}{3} u_k u_k^T$.
Each $F_k$ is positive, and $\sum_k u_k u_k^T = \tfrac{3}{2} I$ because the three unit vectors are equally spaced, so $F_0 + F_1 + F_2 = I$.
This is the trine POVM; it has $3$ outcomes on a space of dimension $2$, so it is not projection-valued.
Non-example: the three operators $u_k u_k^T$ are positive but sum to $\tfrac{3}{2} I$, so clause 2 fails.
A POVM with $F(E)^2 = F(E)$ for all $E$ is a [[projection-valued measure|ATGT25E5FF]].
The operators $F(E)$, which satisfy $0 \le F(E) \le I$, are called effects.
