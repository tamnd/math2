---
tag: XMCAHWK1YB
kind: problem
name: Equilibrium problem with an external field
msc: [31A15, 30C85]
uses: [46NHWJHW44, DBQXRTC0VN, 059TJN0NZ1, 464NN2K4FZ]
about: [464NN2K4FZ, 46NHWJHW44]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_theory
history:
  posed_by: "Carl Friedrich Gauss"
  first_stated: "1840"
---

## Problem

Let $E \subseteq \C$ be a closed set.
Let $w \colon E \to [0, \infty)$ be an upper semicontinuous weight such that the set $\set{z \in E : w(z) > 0}$ has positive [[logarithmic capacity|DBQXRTC0VN]].
If $E$ is unbounded, assume also that $\abs{z}\, w(z) \to 0$ as $\abs{z} \to \infty$ in $E$.
Let $Q = -\log w$ be the *external field*.
For a Borel [[probability measure|059TJN0NZ1]] $\mu$ with support in $E$, set
$$I_w(\mu) = \int \int \log \frac{1}{\abs{z - t}\, w(z)\, w(t)}\, d\mu(z)\, d\mu(t).$$
The problem is to find $V_w = \inf_\mu I_w(\mu)$, a measure $\mu_w$ that attains it, and its support $S_w$.

## Remarks

The weighted energy equals $I(\mu) + 2\int Q\, d\mu$, where $I(\mu)$ is the logarithmic energy.
So the field $Q$ pushes the charge away from where $Q$ is large.
For $w = 1$ on a compact set $E$ this is the problem of the [[equilibrium measure|464NN2K4FZ]] of $E$.
Gauss considered the analogous problem for the Newtonian kernel in space.
The weighted logarithmic version in the plane is the subject of the book of Saff and Totik (1997).
Existence and uniqueness are known under the hypotheses above: $V_w$ is finite, there is a unique minimiser $\mu_w$, and $S_w$ is compact with positive capacity.
The minimiser is characterised by Frostman-type conditions on its [[logarithmic potential|46NHWJHW44]] $U^{\mu_w}$.
For a constant $F_w$, one has $U^{\mu_w} + Q \ge F_w$ quasi-everywhere on $E$ and $U^{\mu_w} + Q \le F_w$ on $S_w$.
Finding $S_w$ for a given weight is the hard part, and it is done explicitly only for special weights.
Example: on $E = \R$ with $w(x) = e^{-x^2}$, the support is $[-1, 1]$ and $\mu_w$ has the semicircle density $\frac{2}{\pi}\sqrt{1 - x^2}$.

## Explanations

### L1 human

Put a unit of charge on a conductor in the plane, but add an outside force that pulls the charge towards some places and pushes it from others.
The charge settles in the arrangement of least total energy.
The question is what this arrangement is, and in particular which part of the conductor it covers.
Such arrangements describe where zeros of orthogonal polynomials and eigenvalues of large random matrices accumulate.
