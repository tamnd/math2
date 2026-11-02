---
tag: M9B7X8F6TN
kind: definition
name: Homoclinic bifurcation
msc: [37G20, 34C37, 37C29]
defines: JQYCTY3Q8V
uses: [D9TW46P19Y, 6DBSQKZK4W, 01TPMXM6NM, 0AAQ73WRFB, WF22KK7C3R]
sources:
  - url: https://en.wikipedia.org/wiki/Bifurcation_theory
---

## Definition

Let $\dot x = F(x, \mu)$, $\mu \in \R$, be a smooth one-parameter family of vector fields on $\R^n$.
Assume that for $\mu$ near $\mu_0$ the system has a [[hyperbolic equilibrium|01TPMXM6NM]] $x_\mu$ of saddle type, depending smoothly on $\mu$.
The family has a *homoclinic bifurcation* at $\mu_0$ if the following hold.

1. At $\mu = \mu_0$ there is a [[homoclinic orbit|6DBSQKZK4W]] $\Gamma$ to $x_{\mu_0}$: an orbit with $x(t) \to x_{\mu_0}$ as $t \to +\infty$ and as $t \to -\infty$.
2. For $\mu \ne \mu_0$ close to $\mu_0$ there is no homoclinic orbit to $x_\mu$ near $\Gamma$.

## Remarks

The orbit $\Gamma$ lies in both the stable and the unstable manifold of $x_{\mu_0}$, given by the [[stable manifold theorem|WF22KK7C3R]].
It is a global bifurcation in the sense of [[bifurcation theory|D9TW46P19Y]], since it depends on a whole orbit and not only on the equilibrium.
In the plane, let $\lambda_1 < 0 < \lambda_2$ be the eigenvalues at the saddle and $\sigma = \lambda_1 + \lambda_2$.
If $\sigma \ne 0$ and the loop splits transversally in $\mu$, a unique [[limit cycle|0AAQ73WRFB]] appears near $\Gamma$ on one side of $\mu_0$, stable if $\sigma < 0$ and unstable if $\sigma > 0$.
Example: for $\dot x = y$, $\dot y = x - x^2 + \mu y$, let $H = y^2/2 - x^2/2 + x^3/3$.
Along solutions $\dot H = \mu y^2$.
At $\mu = 0$ the level set $H = 0$ contains a homoclinic loop to the saddle $(0, 0)$, in the half-plane $x > 0$.
For $\mu \ne 0$, $H$ is strictly monotone along nonconstant orbits, so no orbit can leave and return to the saddle, and the loop is broken.
Here $\sigma = \mu$ vanishes at $\mu_0 = 0$, so this example is degenerate and no limit cycle is born.
Non-example: the constant family $\dot x = y$, $\dot y = x - x^2$, which does not depend on $\mu$, fails clause 2, since the loop persists for every $\mu$.
