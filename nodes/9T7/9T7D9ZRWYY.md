---
tag: 9T7D9ZRWYY
kind: statement
role: theorem
name: Liouville's theorem on phase-space volume
msc: [37J39, 70H05, 53D05]
uses: [0EDKGA2FAK, 06738GGWWK, 0MWV6ZTK6S, 2Z2QVWZ262, C5EH3B4BEP]
about: [0EDKGA2FAK]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(Hamiltonian)
same_as:
  wikidata: Q766722
  wikipedia: Liouville's theorem (Hamiltonian)
---

## Statement

Let $U \subseteq \R^{2n}$ be open, with coordinates $(q_1, \ldots, q_n, p_1, \ldots, p_n)$, and let $H \colon U \to \R$ be twice continuously differentiable.
Let $\varphi_t$ be the [[flow|06738GGWWK]] of the [[Hamiltonian system|0EDKGA2FAK]]
$$q_i' = \frac{\partial H}{\partial p_i}, \qquad p_i' = -\frac{\partial H}{\partial q_i}, \qquad i = 1, \ldots, n.$$
Let $D \subseteq U$ be a measurable set and $t \in \R$ such that $\varphi_t(x)$ is defined for every $x \in D$.
Then $\varphi_t(D)$ has the same [[Lebesgue measure|2Z2QVWZ262]] as $D$.

## Remarks

The vector field $X = (\partial H / \partial p, -\partial H / \partial q)$ has [[divergence|0MWV6ZTK6S]]
$$\sum_{i=1}^n \left( \frac{\partial^2 H}{\partial q_i \partial p_i} - \frac{\partial^2 H}{\partial p_i \partial q_i} \right) = 0.$$
The derivative in $t$ of the volume of $\varphi_t(D)$ is the integral of this divergence over $\varphi_t(D)$, so the volume is constant.
In symplectic language, the flow of a [[Hamiltonian vector field|C5EH3B4BEP]] preserves the symplectic form $\omega$, hence also the volume form $\omega^n / n!$.

Example: for $H = \frac{1}{2}(q^2 + p^2)$ the flow rotates the plane, and rotations preserve area.
For a damped oscillator $q' = p$, $p' = -q - p$ the divergence is $-1$, so areas shrink like $e^{-t}$; this system is not Hamiltonian.

An equivalent form concerns a density $\rho(t, q, p)$ carried by the flow: it satisfies $\frac{\partial \rho}{\partial t} + \{\rho, H\} = 0$, where $\{\cdot, \cdot\}$ is the [[Poisson bracket|2S0MXDT4YH]].

## Explanations

### L1 human

Take a blob of possible initial states of a frictionless mechanical system and let each state move by the equations of motion.
The blob changes shape, often wildly, but its volume in phase space never changes.
This is the reason why a Hamiltonian system cannot have an attracting fixed point.

### L2 human

The theorem is the first sign that Hamiltonian flows preserve geometric structure: they preserve the symplectic form, and volume is its top power.
It is the base of statistical mechanics, since it shows that the Liouville measure is invariant.
With the Poincaré recurrence theorem it shows that if the motion stays in a region of finite volume, then almost every state returns arbitrarily close to where it started.
In dimension $2n \ge 4$, preserving volume is much weaker than preserving $\omega$; [[Gromov's non-squeezing theorem|RDX55HQ3XT]] shows the difference.
