---
tag: BWMB87Q6DM
kind: statement
role: theorem
name: Kelvin's circulation theorem
msc: [76B47, 76A02]
uses: [BTHH4Y71QR, ZJH90RWYQ5, CJW50K5HZB, RW0JK9VDZE]
about: [BTHH4Y71QR]
sources:
  - url: https://en.wikipedia.org/wiki/Kelvin%27s_circulation_theorem
same_as:
  wikidata: Q3661294
  wikipedia: Kelvin's circulation theorem
---

## Statement

Let a fluid flow smoothly in an open set of $\R^3$ with velocity $u$, density $\rho > 0$ and pressure $p$.
Assume that:

1. the flow is [[inviscid|ZJH90RWYQ5]], so it satisfies the [[Euler equations|RW0JK9VDZE]] $Du/Dt = -\nabla p / \rho + f$;
2. the fluid is barotropic, that is $\rho$ is a function of $p$ alone (for example $\rho$ is constant);
3. the body force per unit mass is conservative, $f = -\nabla \Phi$.

Let $C(t)$ be a closed curve that moves with the fluid, and let $\Gamma(t) = \oint_{C(t)} u \cdot dx$ be the [[circulation|BTHH4Y71QR]] around it.
Then $\Gamma(t)$ is constant in time.

## Remarks

Since $C(t)$ moves with the fluid, $\dfrac{d\Gamma}{dt} = \oint_{C(t)} \dfrac{Du}{Dt} \cdot dx + \oint_{C(t)} u \cdot du$, where $D/Dt$ is the [[material derivative|CJW50K5HZB]].
The second integral is $\oint d(\abs{u}^2/2) = 0$.
By the hypotheses, $Du/Dt = -\nabla (P + \Phi)$ with $P(p) = \int dp / \rho(p)$, so the first integral is the integral of a gradient around a closed curve, which is $0$.

Example: a fluid that starts at rest has zero circulation around every closed curve, so under the hypotheses it keeps zero circulation, and by Stokes' theorem it stays irrotational.

Each hypothesis is needed.
Viscosity diffuses vorticity and changes circulation, as in the starting vortex shed by a wing.
In a baroclinic fluid, where $\rho$ is not a function of $p$, the term $\oint dp/\rho$ need not vanish; this is how sea breezes are created.

## Explanations

### L1 human

Draw a loop of dye in a moving ideal fluid and follow it as the fluid carries it along.
The loop gets bent and stretched, but the total amount by which the fluid swirls around it stays the same.
So an ideal fluid can neither create nor destroy swirl by itself.

### L2 human

Kelvin's theorem is the integral form of the conservation of [[vorticity|B3SXT9TWFA]] flux in ideal barotropic flow.
It implies [[Helmholtz's theorems on vortices|D2KCKEP0N4]], including the fact that vortex lines move with the fluid.
It also explains why the potential flow model is consistent: irrotational flow stays irrotational.
To produce lift, the circulation around a wing must come from viscous effects at the trailing edge, which is the role of the Kutta condition.
