---
tag: 6GJMP1MTHQ
kind: definition
name: Identical particles
msc: [81V72, 81V73, 81V74]
defines: Y64G7W4BEC
uses: [HM2HHE3J51, EY0X2NKA3S, 0515A6D2Y1, 02DKV69ZH0]
sources:
  - url: https://en.wikipedia.org/wiki/Indistinguishable_particles
---

## Definition

Let $\mathfrak{h}$ be a complex [[Hilbert space|HM2HHE3J51]], the state space of one particle, and let $n \ge 1$.
For a permutation $\sigma$ in the [[symmetric group|0515A6D2Y1]] $S_n$, let $U_\sigma$ be the unitary operator on the [[tensor product|EY0X2NKA3S]] $\mathfrak{h}^{\otimes n}$ determined by
$$U_\sigma (v_1 \otimes \cdots \otimes v_n) = v_{\sigma^{-1}(1)} \otimes \cdots \otimes v_{\sigma^{-1}(n)}.$$
The state space of $n$ *identical particles* with one-particle space $\mathfrak{h}$ is one of two closed subspaces.
The first is
$$\mathcal{H}_+^{(n)} = \set{\psi \in \mathfrak{h}^{\otimes n} : U_\sigma \psi = \psi \text{ for all } \sigma \in S_n}.$$
The second is
$$\mathcal{H}_-^{(n)} = \set{\psi \in \mathfrak{h}^{\otimes n} : U_\sigma \psi = \sgn(\sigma)\, \psi \text{ for all } \sigma \in S_n}.$$
Here $\sgn(\sigma)$ is the [[sign|02DKV69ZH0]] of $\sigma$.
The particles are *bosons* if the state space is $\mathcal{H}_+^{(n)}$ and *fermions* if it is $\mathcal{H}_-^{(n)}$.

## Remarks

The orthogonal projections onto the two subspaces are $P_\pm = \frac{1}{n!} \sum_{\sigma \in S_n} (\pm 1)^{\sigma} U_\sigma$, where $(+1)^\sigma = 1$ and $(-1)^\sigma = \sgn(\sigma)$.

Example: let $\mathfrak{h} = \C^2$ with orthonormal basis $e_1, e_2$ and $n = 2$.
The vector $\psi = (e_1 \otimes e_2 - e_2 \otimes e_1)/\sqrt{2}$ satisfies $U_{(12)} \psi = -\psi$, and $(12)$ is the only nontrivial permutation, so $\psi \in \mathcal{H}_-^{(2)}$.
In fact $\mathcal{H}_-^{(2)}$ is the line spanned by $\psi$, while $\mathcal{H}_+^{(2)}$ has dimension $3$.

Non-example: the vector $e_1 \otimes e_2$ lies in neither subspace, since $U_{(12)}(e_1 \otimes e_2) = e_2 \otimes e_1$ is not $\pm e_1 \otimes e_2$.
It describes two distinguishable particles, one in state $e_1$ and one in state $e_2$.

In wave function language, with $\mathfrak{h} = L^2(\R^3)$, bosonic wave functions satisfy $\psi(x_{\sigma(1)}, \dots, x_{\sigma(n)}) = \psi(x_1, \dots, x_n)$ and fermionic ones change by $\sgn(\sigma)$.
Spin is included by taking $\mathfrak{h} = L^2(\R^3) \otimes \C^{2s+1}$.
The spin–statistics theorem of relativistic quantum field theory says that particles of integer spin are bosons and particles of half-integer spin are fermions.
