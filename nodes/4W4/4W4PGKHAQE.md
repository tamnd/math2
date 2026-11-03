---
tag: 4W4PGKHAQE
kind: counterexample
name: Klein paradox
msc: [81U26, 35Q41, 81R20]
uses: [XNZX7VXXR2, EPZR6H2WJN, XAQCW3D4QQ]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_paradox
same_as:
  wikidata: Q2383018
  wikipedia: Klein paradox
---

## Counterexample

Use units with $\hbar = c = 1$ and one space dimension.
Consider the [[Dirac equation|XNZX7VXXR2]] for $\psi \colon \R^2 \to \C^2$ with an electric potential $V$:
$$i\, \partial_t \psi = \left( -i\sigma_1 \partial_x + m\sigma_3 + V(x) \right)\psi.$$
Here $m \ge 0$, and $\sigma_1, \sigma_3$ are [[Pauli matrices|XAQCW3D4QQ]].
Take the potential step $V(x) = 0$ for $x < 0$ and $V(x) = V_0 > 0$ for $x > 0$.
A stationary solution $\psi = \phi(x) e^{-iEt}$ with energy $E > m$ consists of plane waves $u\, e^{ikx}$ in each region.
On such a wave the operator $\sigma_1 k + m\sigma_3$ has eigenvalues $\pm\sqrt{k^2 + m^2}$, so in the region $x > 0$ one needs $(E - V_0)^2 = k^2 + m^2$.

Claim: when $V_0 > E + m$, the wave number $k = \pm\sqrt{(E - V_0)^2 - m^2}$ in the region $x > 0$ is real, so the solution oscillates there instead of decaying.
This contradicts the expectation, true for the [[Schrödinger equation|EPZR6H2WJN]], that a barrier much higher than the energy of the particle is nearly impenetrable.
For the Schrödinger step with $V_0 > E$, the solution behind the step decays like $e^{-\kappa x}$ with $\kappa = \sqrt{2m(V_0 - E)}$, and no probability current enters the region $x > 0$.
For the Dirac step, the transmitted current stays nonzero for every $V_0 > E + m$ and does not tend to $0$ as $V_0 \to \infty$.

The massless case shows this in its simplest form.
For $m = 0$ the stationary equation is $(E - V(x))\phi = -i\sigma_1 \phi'$.
In the eigenbasis of $\sigma_1$, the component $w = \phi_1 + \phi_2$ satisfies $w' = i(E - V(x))\, w$, so $w(x) = w(0)\exp\!\left( i\int_0^x (E - V(s))\, ds \right)$ for any potential $V$.
A right-moving wave keeps its modulus everywhere: it passes through any barrier, however high, with no reflection at all.

## Explanations

### L1 human

In ordinary quantum mechanics a particle can tunnel through a wall a little, but a very high wall stops it almost completely.
Klein found in 1929 that the Dirac equation behaves differently: a very high and steep potential step lets a sizeable part of the wave through.
The explanation is that behind a step higher than twice the rest energy, negative-energy states, which describe antiparticles, line up with the energy of the incoming particle.
So the paradox shows that the Dirac equation cannot be read as a theory of a single particle; strong fields create particle–antiparticle pairs, and quantum field theory is needed.
For massless particles the effect is total transmission, which has been studied in graphene.
