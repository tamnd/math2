---
tag: STN15FJ43Z
kind: statement
role: theorem
name: Ward–Takahashi identity
msc: [81T15, 81V10]
uses: [V329C7A1QP, K9SR95P4NJ, TDPX0D7ZD0, XHPDM5T2JG]
about: [V329C7A1QP]
sources:
  - url: https://en.wikipedia.org/wiki/Ward%E2%80%93Takahashi_identity
same_as:
  wikidata: Q353202
  wikipedia: Ward–Takahashi identity
---

## Statement

Consider [[quantum electrodynamics|V329C7A1QP]] of a Dirac field of mass $m$, with a gauge-invariant regularization.
Let $S(p)$ be the full electron [[propagator|K9SR95P4NJ]] in momentum space, normalized so that $S(p) = i(\gamma^\mu p_\mu - m)^{-1}$ at tree level.
Let $\Gamma^\mu(p', p)$ be the full one-particle-irreducible electron-photon vertex, normalized so that $\Gamma^\mu = \gamma^\mu$ at tree level.
Then, to all orders of perturbation theory, for all momenta $p$ and $k$,
$$-i k_\mu \Gamma^\mu(p + k, p) = S^{-1}(p + k) - S^{-1}(p).$$

## Remarks

The identity follows from current conservation, $\partial_\mu j^\mu = 0$, by [[Noether's theorem|XHPDM5T2JG]] for the global phase symmetry.
Inside time-ordered products, $\partial_\mu$ acting on $j^\mu(x)$ produces only contact terms where $x$ meets a charged field.
These contact terms give the right-hand side.

Tree-level check: with $\Gamma^\mu = \gamma^\mu$ and $S^{-1}(p) = -i(\gamma^\mu p_\mu - m)$, both sides equal $-i\gamma^\mu k_\mu$.

Consequences: setting $k \to 0$ gives $\Gamma^\mu(p, p) = i\,\partial S^{-1}(p)/\partial p_\mu$, the Ward identity.
It implies that the vertex and the electron field strength renormalization constants are equal, $Z_1 = Z_2$.
So the electric charge renormalizes only through the photon field, and all charged particles keep equal charges after renormalization.
For on-shell amplitudes with an external photon of momentum $k$, written $\mathcal{M}^\mu \epsilon_\mu$, the identity gives $k_\mu \mathcal{M}^\mu = 0$.
This is why the unphysical photon polarizations decouple.

## Explanations

### L1 human

Charge conservation has precise consequences for quantum amplitudes.
The Ward–Takahashi identity is one of them: it ties the way an electron couples to light to the way the electron propagates.
It guarantees, for example, that the measured charge of an electron and of a muon remain equal after quantum corrections.

### L2 human

The identity is the quantum form of gauge invariance in QED, and it is a [[Schwinger–Dyson equation|B1021FRSPZ]] for a symmetry variation.
It is used to check calculations and to show that QED is renormalizable with a gauge-invariant set of counterterms.
In non-abelian gauge theories, the analogous identities are the Slavnov–Taylor identities, which involve the ghost fields.
