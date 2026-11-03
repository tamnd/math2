---
tag: F8ZKQEQDCQ
kind: definition
name: Second quantization
msc: [81V70, 81S05, 81T05]
defines: SZWQ1A69V6
uses: [1TJ8TNH331, Y64G7W4BEC, MM0EJ2GDE4, 0NEGN5CRSC, DVGQB92HPJ, 7N0J4DF8N5]
sources:
  - url: https://en.wikipedia.org/wiki/Second_quantization
---

## Definition

Let $\mathfrak{h}$ be a complex Hilbert space.
Let $\mathcal{F}_\pm(\mathfrak{h}) = \widehat{\bigoplus}_{n \ge 0} \mathcal{H}^{(n)}_\pm$ be its bosonic ($+$) or fermionic ($-$) [[Fock space|1TJ8TNH331]].
Here $\mathcal{H}^{(n)}_\pm \subseteq \mathfrak{h}^{\otimes n}$ is the space of $n$ [[identical particles|Y64G7W4BEC]].
*Second quantization* is the passage from $\mathfrak{h}$ to $\mathcal{F}_\pm(\mathfrak{h})$ together with the following maps on operators.

1. For a [[unitary operator|MM0EJ2GDE4]] $U$ on $\mathfrak{h}$, $\Gamma(U)$ is the unitary operator on $\mathcal{F}_\pm(\mathfrak{h})$ that acts on $\mathcal{H}^{(n)}_\pm$ as $U^{\otimes n}$.
   On $\mathcal{H}^{(0)}_\pm = \C$ it acts as the identity.
2. For a [[self-adjoint operator|0NEGN5CRSC]] $A$ on $\mathfrak{h}$, let $D_n = \mathcal{H}^{(n)}_\pm \cap D(A)^{\otimes n}$.
   Here $D(A)^{\otimes n}$ is the algebraic tensor power of the domain of $A$.
   On $D_n$ let $A_n = \sum_{k=1}^n I^{\otimes (k-1)} \otimes A \otimes I^{\otimes (n-k)}$, and let $A_0 = 0$ on $\C$.
   Then $d\Gamma(A)$ is the closure of the operator that acts as $A_n$ on each $D_n$ and is extended linearly to finite sums over $n$.

## Remarks

The operator $d\Gamma(A)$ is self-adjoint, and $\Gamma(e^{itA}) = e^{it\, d\Gamma(A)}$ for all $t \in \R$, so $d\Gamma(A)$ is the generator given by [[Stone's theorem|DVGQB92HPJ]].
Also $\Gamma(UV) = \Gamma(U)\Gamma(V)$.

Example: $d\Gamma(I) = N$ is the number operator, which acts on $\mathcal{H}^{(n)}_\pm$ as multiplication by $n$.
If $A e_j = \lambda_j e_j$ for an orthonormal basis $(e_j)$ of $\mathfrak{h}$, then $d\Gamma(A) = \sum_j \lambda_j\, a^*(e_j)\, a(e_j)$ on finite-particle vectors in the span of the basis tensors, with the [[creation and annihilation operators|7N0J4DF8N5]].

Non-example: $d\Gamma(A)$ is additive over the particles, not multiplicative.
For $A = \lambda I$ with $\lambda \in \R$, the operator $d\Gamma(A)$ acts on $\mathcal{H}^{(2)}_\pm$ as $2\lambda$, while $A \otimes A$ acts as $\lambda^2$.
So $A \otimes A$ is not the second quantization of $A$ on two particles unless $\lambda \in \set{0, 2}$.

If $H_1 = -\frac{\hbar^2}{2m}\Delta$ on $\mathfrak{h} = L^2(\R^3)$, then $d\Gamma(H_1)$ is the total kinetic energy of a free gas of identical particles with any number of particles.
