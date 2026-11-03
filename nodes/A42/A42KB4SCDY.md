---
tag: A42KB4SCDY
kind: example
name: Schwinger model
msc: [81T40, 81V10, 81T13]
illustrates: [V329C7A1QP, JT8G0FWR01]
uses: [M85BQEPQ7B, TDPX0D7ZD0]
sources:
  - url: https://en.wikipedia.org/wiki/Schwinger_model
same_as:
  wikidata: Q3318083
  wikipedia: Schwinger model
---

## Example

The *Schwinger model* is [[quantum electrodynamics|V329C7A1QP]] in two spacetime dimensions with one massless Dirac fermion.
Work on $\R^{1,1}$ with signature $(+,-)$.
Let $\gamma^0, \gamma^1$ be $2 \times 2$ [[gamma matrices|TDPX0D7ZD0]] with $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2\eta^{\mu\nu} I_2$.
Let $\psi$ be a field with values in $\C^2$, and let $A_\mu$ be a real gauge field.
Its Lagrangian density is
$$\mathcal{L} = \bar\psi \, i\gamma^\mu (\partial_\mu + i e A_\mu) \psi - \frac{1}{4} F_{\mu\nu} F^{\mu\nu}.$$
In two dimensions the coupling $e$ has the dimension of a mass.

Check of the main fact: the model can be solved exactly.
Its spectrum consists of a single free boson of mass
$$m = \frac{e}{\sqrt{\pi}}$$
in units with $\hbar = c = 1$.
The classical theory has a massless photon and a massless fermion, and the axial current $j^\mu_5 = \bar\psi\gamma^\mu\gamma^5\psi$ is conserved classically.
In the quantum theory the axial current has an [[anomaly|JT8G0FWR01]], $\partial_\mu j^\mu_5 = \frac{e}{\pi} \epsilon^{\mu\nu} \partial_\mu A_\nu$ up to sign convention, and this anomaly is what gives the photon its mass.
In the language of bosonization, the fermion is equivalent to a free scalar, and the gauge field gives that scalar the mass $e/\sqrt\pi$.

## Remarks

Julian Schwinger introduced and solved the model in 1962.
It shows that a gauge field can become massive without any Higgs field, and that charged particles can be confined: no state carries the charge of a single fermion.
It is a standard test case for methods in lattice and constructive field theory.

## Explanations

### L1 human

The Schwinger model is the theory of electrons and light squeezed into a world with one space dimension and one time dimension.
It is one of the rare interacting quantum field theories that can be solved completely.
The surprise is that the light particle of the theory becomes heavy, with a mass fixed by the strength of the charge.
At the same time, single electrons can never be found alone, which makes the model a toy version of quark confinement.
