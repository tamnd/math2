---
tag: MRY9JZTK9V
kind: definition
name: Hartle–Hawking state
msc: [83C45, 83F05]
defines: TDGEHS585Q
uses: [MGPT8N01FW, TNKMDJB5FP, 7CBT4SM83Y]
sources:
  - url: https://en.wikipedia.org/wiki/Hartle–Hawking_proposal
---

## Definition

Let $\Sigma$ be a closed three-manifold with a Riemannian metric $h$ and matter field configuration $\phi_0$ on $\Sigma$.
The *Hartle–Hawking state* is the wave function
$$\Psi_{\mathrm{HH}}[h, \phi_0] = \int \mathcal{D}[g] \, \mathcal{D}[\phi] \; e^{-I[g, \phi]/\hbar},$$
where $I$ is the Euclidean action of gravity and matter as in [[Euclidean quantum gravity|MGPT8N01FW]].
The formal integral runs over compact four-manifolds $M$ with $\partial M = \Sigma$ and over [[Riemannian metrics|7CBT4SM83Y]] $g$ on $M$ inducing $h$.
It also runs over matter fields $\phi$ on $M$ restricting to $\phi_0$.

## Remarks

The integral has no other boundary, hence the name no-boundary proposal.
Formally $\Psi_{\mathrm{HH}}$ satisfies the [[Wheeler–DeWitt equation|TNKMDJB5FP]], because the integrand is invariant under diffeomorphisms and the integral over the lapse imposes the Hamiltonian constraint.
Example: take the minisuperspace model with a cosmological constant $\Lambda > 0$ and $\Sigma$ a round three-sphere of radius $a$.
For small $a$ the dominant saddle is a portion of a round four-sphere of radius $\sqrt{3/\Lambda}$ capping off $\Sigma$.
For $a > \sqrt{3/\Lambda}$ it continues as half a four-sphere glued to Lorentzian de Sitter space, and the wave function oscillates.
Non-example: a path integral over cylinders $[0,1] \times \Sigma$ with a fixed initial metric on $\set{0} \times \Sigma$ is not the Hartle–Hawking state, since it has a second boundary.
Vilenkin's tunnelling wave function is a different proposal with different boundary conditions on the same equation.
