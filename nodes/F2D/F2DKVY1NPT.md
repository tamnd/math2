---
tag: F2DKVY1NPT
kind: statement
role: theorem
name: No-cloning theorem
msc: [81P50, 81P45]
uses: [HM2HHE3J51, EY0X2NKA3S, MM0EJ2GDE4, 4NQN47A92F]
about: [4NQN47A92F]
sources:
  - url: https://en.wikipedia.org/wiki/No-cloning_theorem
same_as:
  wikidata: Q1751823
  wikipedia: No-cloning theorem
---

## Statement

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]] of dimension at least $2$, and let $e \in H$ be a unit vector.
There is no [[unitary operator|MM0EJ2GDE4]] $U$ on the [[tensor product|EY0X2NKA3S]] $H \otimes H$ such that
$$U(\psi \otimes e) = \psi \otimes \psi$$
for every unit vector $\psi \in H$.

## Remarks

Suppose such a $U$ exists, and let $\psi$, $\varphi$ be unit vectors.
Since $U$ preserves inner products, $\langle \varphi, \psi \rangle \langle e, e\rangle = \langle \varphi, \psi \rangle^2$.
So $\langle \varphi, \psi \rangle$ is $0$ or $1$ for all unit vectors, which fails for $\psi = |0\rangle$ and $\varphi = (|0\rangle + |1\rangle)/\sqrt2$, whose inner product is $1/\sqrt2$.

Allowing global phases, $U(\psi \otimes e) = e^{i\alpha(\psi)} \psi \otimes \psi$, does not help: the same argument gives $\abs{\langle\varphi,\psi\rangle} \in \set{0, 1}$.
The theorem also holds for quantum channels: no completely positive trace-preserving map sends every pure state $|\psi\rangle\langle\psi|$ to $|\psi\rangle\langle\psi| \otimes |\psi\rangle\langle\psi|$.

The requirement "for every $\psi$" is essential.
Any single orthonormal basis can be cloned: on qubits, the controlled-NOT gate maps $|0\rangle|0\rangle$ to $|0\rangle|0\rangle$ and $|1\rangle|0\rangle$ to $|1\rangle|1\rangle$.

## Explanations

### L1 human

There is no machine that makes a perfect copy of an unknown quantum state.
A photocopier for classical data works on any input, but a quantum copier can work only on states that are known to be perpendicular to each other.
This follows from the linearity of quantum mechanics alone.

### L2 human

No-cloning separates quantum from classical information.
It is the basis of the security of quantum key distribution, since an eavesdropper cannot copy the transmitted qubits and keep a copy.
It is consistent with teleportation, where the original state is destroyed at the sender's side.
It also explains why quantum error correction must protect information without copying it, by spreading it over entangled qubits.
