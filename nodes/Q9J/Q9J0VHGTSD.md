---
tag: Q9J0VHGTSD
kind: definition
name: Quantum invariant of 3-manifolds
msc: [57K16, 57K31]
defines: YGPR4VR3GP
uses: [R20TB2KEQQ, ZA405B0Z1S, 4SPC17FPXE, AVQ9WN1MDV]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_invariant
---

## Definition

Let $\mathcal{C}$ be a modular tensor category.
An example is the category of tilting representations of the quantum group $U_q(\mathfrak{sl}_2)$ at a root of unity $q$, modulo negligible morphisms.
The Reshetikhin–Turaev functor of $\mathcal{C}$ assigns a number $\langle L \rangle$ to each framed link $L$ in $S^3$ whose components are colored by objects of $\mathcal{C}$.

The *quantum invariant* $\tau_{\mathcal{C}}(M)$ of a closed oriented [[3-manifold|R20TB2KEQQ]] $M$ is obtained as follows.

1. Present $M$ by integral [[Dehn surgery|ZA405B0Z1S]] on a framed link $L \subset S^3$ with $n$ components.
2. Color each component of $L$ by the Kirby color $\omega = \sum_i \dim(V_i)\, V_i$, and evaluate $\langle L \rangle$ by linearity.
   Here $\dim$ is the quantum dimension, and the sum runs over the isomorphism classes of simple objects $V_i$.
3. Multiply by a normalising factor that depends only on $\mathcal{C}$, on $n$ and on the signature of the linking matrix of $L$.

The normalising factor is chosen so that the result does not change under the [[Kirby moves|AVQ9WN1MDV]], and hence depends only on $M$.

## Remarks

Let $\mathcal{C}$ come from $U_q(\mathfrak{sl}_2)$ with $q = e^{2\pi i / r}$.
Then the evaluation in step 2 is a combination of colored [[Jones polynomials|4SPC17FPXE]] of $L$, and $\tau_{\mathcal{C}}$ is the $SU(2)$ Witten–Reshetikhin–Turaev invariant at level $r - 2$.
Suitably normalised, the invariant is multiplicative under connected sum.
Step 3 is needed: the links $\emptyset$ and the $(\pm 1)$-framed unknot both present $S^3$, while their colored evaluations differ in general.
Normalisation conventions differ between authors.
