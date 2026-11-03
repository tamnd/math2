---
tag: Y75WQ84PTC
kind: statement
role: theorem
name: PBR theorem
msc: [81P05, 81P16]
uses: [QRW6NE1VY7, 059TJN0NZ1, EY0X2NKA3S, 4NQN47A92F]
about: [QRW6NE1VY7, 4NQN47A92F]
sources:
  - url: https://en.wikipedia.org/wiki/Pusey%E2%80%93Barrett%E2%80%93Rudolph_theorem
same_as:
  wikidata: Q17099549
  wikipedia: Pusey–Barrett–Rudolph theorem
---

## Statement

Consider a [[hidden-variable theory|QRW6NE1VY7]] for a finite-dimensional quantum system and for all its finite collections of copies.
Let $\Lambda$ be the space of hidden variables of one copy, and let $\Lambda^n$ be that of $n$ copies.
Assume preparation independence: for pure [[states|4NQN47A92F]] $\psi_1, \dots, \psi_n$, the measure of the product state $\psi_1 \otimes \dots \otimes \psi_n$ is $\mu_{\psi_1} \times \dots \times \mu_{\psi_n}$.
Let $\psi$ and $\varphi$ be unit vectors in the same space that define different rays.
Then the [[probability measures|059TJN0NZ1]] $\mu_\psi$ and $\mu_\varphi$ are mutually singular: some measurable set has $\mu_\psi$-measure $1$ and $\mu_\varphi$-measure $0$.

## Remarks

Mutually singular measures mean that the hidden variable determines the quantum state, so the state is *ontic* rather than a mere description of knowledge.
The key case is $\psi = e_0$ and $\varphi = (e_0 + e_1)/\sqrt2$ in $\C^2$.
Prepare two independent copies, so that one of the four product states $e_0 \otimes e_0$, $e_0 \otimes \varphi$, $\varphi \otimes e_0$, $\varphi \otimes \varphi$ is present.
There is an entangled measurement on $\C^2 \otimes \C^2$ whose $k$-th outcome is orthogonal to the $k$-th of these product states.
Suppose $\mu_\psi$ and $\mu_\varphi$ overlap.
By preparation independence, with positive probability the hidden variable of the pair is compatible with all four states.
Then some outcome has positive probability for a state orthogonal to it, which is impossible.
Non-orthogonal states that are closer together need more copies and a similar argument.
Without preparation independence the conclusion fails: there are models in which distinct quantum states share hidden variables.

## Explanations

### L1 human

A quantum state could be a real physical property of a system, or only a summary of what an observer knows about it.
The PBR theorem says that, under a natural independence assumption, two different pure states can never come from the same underlying physical state.
So, in any hidden-variable picture of this kind, the quantum state is a real feature of the system.

### L2 human

The theorem was published by Pusey, Barrett and Rudolph in 2012, in the framework of ontological models.
It distinguishes "psi-ontic" models, such as de Broglie–Bohm theory, from "psi-epistemic" ones, in which distributions for different states overlap.
Preparation independence is essential, and it plays a role similar to that of measurement independence in Bell's theorem.
Unlike Bell's theorem, the PBR theorem concerns preparations of independent systems rather than correlations of entangled ones.
