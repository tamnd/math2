---
tag: CDXS11AEW9
kind: statement
role: theorem
name: Purification of a quantum state
msc: [81P16, 81P40]
uses: [EY0X2NKA3S, V1JTB52E8C, SQ3J7AVMKM, 0DGZBQWZWN, MM0EJ2GDE4, NXQKCMH7NN]
about: [V1JTB52E8C, SQ3J7AVMKM]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_state_purification
same_as:
  wikidata: Q133816092
  wikipedia: Quantum state purification
---

## Statement

Let $H_A$ be a complex Hilbert space of finite dimension, and let $\rho$ be a [[density matrix|V1JTB52E8C]] on $H_A$ of rank $r$.
Let $H_B$ be a complex Hilbert space with $\dim H_B \ge r$.

1. There is a unit vector $\psi \in H_A \otimes H_B$ with $\tr_B |\psi\rangle\langle\psi| = \rho$, where $\tr_B$ is the [[partial trace|SQ3J7AVMKM]] over $H_B$.
2. If $\psi$ and $\varphi$ are two unit vectors in $H_A \otimes H_B$ with $\tr_B |\psi\rangle\langle\psi| = \tr_B |\varphi\rangle\langle\varphi| = \rho$, then $\varphi = (I \otimes U)\psi$ for some [[unitary operator|MM0EJ2GDE4]] $U$ on $H_B$.

Such a vector $\psi$ is called a *purification* of $\rho$.

## Remarks

By the [[spectral theorem|0DGZBQWZWN]], $\rho = \sum_{i=1}^{r} p_i |e_i\rangle\langle e_i|$ with $p_i > 0$ and $e_i$ orthonormal.
Choose orthonormal $f_1, \dots, f_r$ in $H_B$ and put $\psi = \sum_i \sqrt{p_i} \, e_i \otimes f_i$; a direct computation gives $\tr_B |\psi\rangle\langle\psi| = \rho$.
For uniqueness, the [[Schmidt decomposition|NXQKCMH7NN]] of any purification has the form $\sum_i \sqrt{p_i} \, e_i \otimes f_i'$, up to a choice of eigenbasis.
A unitary on $H_B$ that maps the family $f_i$ to the family $f_i'$ then relates the two purifications.

Example: the maximally mixed qubit state $\tfrac12 I$ on $\C^2$ is purified by $(|00\rangle + |11\rangle)/\sqrt{2}$ in $\C^2 \otimes \C^2$.

The bound $\dim H_B \ge r$ is necessary.
If $\dim H_B < r$, every vector of $H_A \otimes H_B$ has Schmidt rank at most $\dim H_B$, so its reduced state has rank less than $r$.

## Explanations

### L1 human

A mixed state describes a system about which we lack full knowledge.
This theorem says that such a state can always be seen as one part of a larger system that is in a pure state.
The missing knowledge is then hidden in the correlations with the extra part.
Two such larger pictures differ only by a change of basis on the extra part.

### L2 human

Purification lets one replace mixed states by pure states on a larger space, which often simplifies proofs.
It underlies the Stinespring picture of quantum channels and Uhlmann's formula for the fidelity.
The uniqueness clause is also the reason why a party holding the purifying system can steer the other party's state.
