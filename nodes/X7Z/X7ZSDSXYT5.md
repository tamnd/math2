---
tag: X7ZSDSXYT5
kind: definition
name: Marsden–Weinstein reduction
msc: [53D20]
defines: SBJVATVH44
uses: [CAN490EPRT, ZARM34FZ6Z, 0BR3FY5Q8M]
sources:
  - url: https://en.wikipedia.org/wiki/Momentum_map
---

## Definition

Let $(M, \omega)$ be a [[symplectic manifold|CAN490EPRT]] with a Hamiltonian action of a [[Lie group|7JBRGCVJRB]] $G$ and a [[moment map|ZARM34FZ6Z]] $\mu \colon M \to \mathfrak{g}^*$.
Assume that $G$ acts freely and properly on the level set $Z = \mu^{-1}(0)$.
Then $Z$ is a submanifold of $M$, the [[quotient|0BR3FY5Q8M]] $M /\!\!/ G = Z / G$ is a smooth manifold, and the quotient map $\pi \colon Z \to Z / G$ is smooth.
Let $i \colon Z \to M$ be the inclusion.
The *Marsden–Weinstein reduction* (or *symplectic quotient*) of $M$ by $G$ is the manifold $M /\!\!/ G$ with the unique $2$-form $\omega_{\mathrm{red}}$ such that
$$\pi^* \omega_{\mathrm{red}} = i^* \omega.$$

## Remarks

The Marsden–Weinstein–Meyer theorem says that $\omega_{\mathrm{red}}$ exists, is unique, and is symplectic, and that $\dim M /\!\!/ G = \dim M - 2 \dim G$.
Freeness of the action on $Z$ implies that $0$ is a regular value of $\mu$, which is why $Z$ is a submanifold.
Properness holds automatically when $G$ is compact.
Reduction at another value $\lambda \in \mathfrak{g}^*$ uses $\mu^{-1}(\lambda)$ divided by the stabilizer of $\lambda$ under the coadjoint action.

Example: let $S^1$ act on $\C^{n+1}$ by $e^{i\theta} \cdot z = e^{i\theta} z$, with the standard symplectic form.
A moment map is $\mu(z) = -\frac{1}{2}\abs{z}^2 + \frac{1}{2}$.
Then $\mu^{-1}(0)$ is the unit sphere $S^{2n+1}$, the circle acts freely on it, and the reduction is $\mathbb{CP}^n$ with a multiple of the Fubini–Study form.

Non-example: take the same circle action on $\C$ with $\mu(z) = -\frac{1}{2}\abs{z}^2$.
The level set $\mu^{-1}(0) = \set{0}$ is a fixed point, so the action on it is not free and the definition does not apply.
