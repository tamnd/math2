---
tag: BD6BJ0PSB5
kind: definition
name: Anomaly
msc: [81T50]
defines: FGASZ29SFV
uses: [XHPDM5T2JG, 1X0W3AEBEJ, V329C7A1QP]
sources:
  - url: https://en.wikipedia.org/wiki/Anomaly_(physics)
---

## Definition

Let $S[\phi]$ be the action of a classical field theory, and let $\delta\phi = \epsilon K(\phi)$ be a continuous infinitesimal transformation with $\delta S = 0$.
Let $j^\mu$ be the associated [[Noether|XHPDM5T2JG]] current, so $\partial_\mu j^\mu = 0$ when the equations of motion hold.
Quantize the theory with a regularization, as in [[renormalization|1X0W3AEBEJ]].
The symmetry is *anomalous* if the following holds.

1. For every choice of regularization and of local counterterms, the quantum Ward identities of the symmetry fail.
2. Equivalently, the renormalized current satisfies $\partial_\mu j^\mu = \mathcal{A}$ as an operator equation, with $\mathcal{A} \ne 0$.

The local expression $\mathcal{A}$ is called the *anomaly*.
An anomaly of a global symmetry is called an anomaly of a global current.
An anomaly of a gauge symmetry is called a gauge anomaly.

## Remarks

Example: in [[quantum electrodynamics|V329C7A1QP]] with one massless Dirac fermion, the axial transformation $\psi \mapsto e^{i\alpha\gamma^5}\psi$ leaves the classical action invariant.
Its current $j^{\mu 5} = \bar\psi\gamma^\mu\gamma^5\psi$ satisfies, with $\epsilon^{0123} = +1$,
$$\partial_\mu j^{\mu 5} = \frac{e^2}{16\pi^2}\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}.$$
The right side is not removable by a local counterterm compatible with gauge invariance, so the axial symmetry is anomalous.

Non-example: the vector current $j^\mu = \bar\psi\gamma^\mu\psi$ of the same theory stays conserved with a gauge-invariant regularization.
So the phase symmetry $\psi \mapsto e^{i\alpha}\psi$ is not anomalous.

In the path integral, Fujikawa's view is that the anomaly is the Jacobian of the transformation of the fermion measure.
In the presence of several currents one can often move the anomaly from one current to another, but not remove it from all of them.
