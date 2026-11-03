---
tag: JT8G0FWR01
kind: statement
role: theorem
name: Chiral anomaly
msc: [81T50, 81V10, 58J20]
uses: [FGASZ29SFV, V329C7A1QP, TDPX0D7ZD0, 3DXGJTEQZH]
about: [FGASZ29SFV]
sources:
  - url: https://en.wikipedia.org/wiki/Chiral_anomaly
same_as:
  wikidata: Q5101826
  wikipedia: Chiral anomaly
---

## Statement

Consider [[quantum electrodynamics|V329C7A1QP]] in four dimensions with one Dirac fermion $\psi$ of mass $m$ and charge $e$, with a gauge-invariant regularization.
Let $\gamma^\mu$ and $\gamma^5$ be the [[gamma matrices|TDPX0D7ZD0]], $F_{\mu\nu}$ the field strength and $\epsilon^{0123} = +1$.
Then the axial current $j^{\mu 5} = \bar\psi\gamma^\mu\gamma^5\psi$ satisfies the operator equation
$$\partial_\mu j^{\mu 5} = 2im\,\bar\psi\gamma^5\psi + \frac{e^2}{16\pi^2}\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}.$$
In particular, for $m = 0$ the classically conserved axial current is not conserved.

## Remarks

The first term is the classical one, from the Dirac equation; the second is the [[anomaly|FGASZ29SFV]].
It was found by Adler and by Bell and Jackiw, from the triangle diagram with one axial and two vector vertices.
No regularization can keep both the vector and the axial current conserved for this diagram.
The coefficient is exact: Adler and Bardeen showed that higher orders give no correction.

In the Euclidean path integral, the anomaly is the Jacobian of the fermion measure under a chiral rotation, as computed by Fujikawa.
Integrated over a compact four-manifold, it gives the index of the [[Dirac operator|3DXGJTEQZH]] coupled to the gauge field.
This index is the number of zero modes of positive chirality minus the number of negative chirality, and the Atiyah–Singer index theorem computes it from the field strength.

Example: the anomaly gives the rate of the decay of the neutral pion into two photons.
Without it, the decay would be strongly suppressed in the limit of massless quarks.

## Explanations

### L1 human

For massless electrons, classical physics conserves separately the number of left-handed and of right-handed particles.
Quantum effects break this: parallel electric and magnetic fields convert one kind into the other.
The rate of conversion is fixed exactly by the fields and does not depend on details of the theory.

### L2 human

The chiral anomaly is the basic example of an [[anomaly|FGASZ29SFV]].
In non-abelian gauge theories the analogous anomalies of gauge currents must cancel, which explains why each generation of the Standard Model contains both quarks and leptons with their charges.
The anomaly is topological: its integral is an integer index, which is why it receives no perturbative corrections.
It also appears in condensed matter physics, in Weyl semimetals.
