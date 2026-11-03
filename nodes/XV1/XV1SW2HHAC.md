---
tag: XV1SW2HHAC
kind: definition
name: Channel capacity of a quantum channel
msc: [81P47, 94A40, 81P45]
defines: JYHQQGGZJZ
uses: [10VZYJ4552, V1JTB52E8C, A8D05RKX8M, H53TSRFWQ4, CDXS11AEW9]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_capacity
---

## Definition

Let $H_A$ and $H_B$ be finite-dimensional complex Hilbert spaces.
Let $\mathcal{N}$ be a [[quantum channel|10VZYJ4552]] from the operators on $H_A$ to the operators on $H_B$.
Let $n \ge 1$ and $M \ge 1$.
An $(n, M)$ *quantum code* for $\mathcal{N}$ is a pair $(\mathcal{E}_n, \mathcal{D}_n)$ of quantum channels.
The encoding $\mathcal{E}_n$ maps the operators on $\C^M$ to those on $H_A^{\otimes n}$.
The decoding $\mathcal{D}_n$ maps the operators on $H_B^{\otimes n}$ to those on $\C^M$.
Its minimum [[fidelity|A8D05RKX8M]] is
$$f_n = \min_{\psi} \langle \psi \rvert (\mathcal{D}_n \circ \mathcal{N}^{\otimes n} \circ \mathcal{E}_n)(\lvert \psi \rangle\langle \psi \rvert) \lvert \psi \rangle,$$
where $\psi$ runs over the unit vectors of $\C^M$.
A rate $R \ge 0$ is *achievable* if there are $(n, M_n)$ quantum codes with $\liminf_{n \to \infty} \frac1n \log_2 M_n \ge R$ and $f_n \to 1$.
The *quantum capacity* $Q(\mathcal{N})$ is the supremum of the achievable rates.

## Remarks

Example: for the identity channel on one qubit, $H_A = H_B = \C^2$, take $M_n = 2^n$ and let $\mathcal{E}_n$ and $\mathcal{D}_n$ be the identity.
Then $f_n = 1$, so the rate $1$ is achievable and $Q \ge 1$; in fact $Q = 1$.

Non-example of a positive rate: for the completely depolarizing channel $\mathcal{N}(\rho) = \tr(\rho)\, I/d$, the output does not depend on the input.
No decoding can recover a qubit, so no rate $R > 0$ is achievable and $Q(\mathcal{N}) = 0$.

The Lloyd–Shor–Devetak theorem gives
$$Q(\mathcal{N}) = \lim_{n \to \infty} \frac1n \max_{\rho} I_c(\rho, \mathcal{N}^{\otimes n}),$$
where the coherent information is $I_c(\rho, \mathcal{N}) = S(\mathcal{N}(\rho)) - S((\mathrm{id} \otimes \mathcal{N})(\lvert \phi \rangle\langle \phi \rvert))$ for a [[purification|CDXS11AEW9]] $\phi$ of $\rho$, and $S$ is the [[von Neumann entropy|H53TSRFWQ4]].
The limit is needed in general, because the coherent information is not additive.
Replacing the minimum fidelity by the average or entanglement fidelity gives the same capacity.
