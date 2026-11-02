---
tag: QWAZ4DK5AD
kind: definition
name: Domain of finite type
msc: [32T25, 32F18]
defines: ZJ0GBPREMB
uses: [5S30FAJNGM, 3MQTWKBBBT, 0V33BNKZ9S, Z7RVXBA2KB]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Definition

Let $\Omega \subseteq \C^n$ be a domain with $C^\infty$ boundary.
Let $\rho$ be a [[smooth|0V33BNKZ9S]] defining function of $\Omega$, as in the [[definition of the Levi form|5S30FAJNGM]].
Let $D \subseteq \C$ be the unit disc.
For a function $g$ of class $C^\infty$ near $0 \in \C$, let $\nu(g)$ be its order of vanishing at $0$.
This is the smallest $k$ such that some partial derivative of $g$ of order $k$ is nonzero at $0$, and $\nu(g) = \infty$ if there is none.
For $p \in \partial\Omega$, the *type* of $\partial\Omega$ at $p$ is
$$\Delta(p) = \sup_{\gamma} \frac{\nu(\rho \circ \gamma)}{\nu(\gamma - p)},$$
where $\gamma \colon D \to \C^n$ runs over the nonconstant [[holomorphic maps|3MQTWKBBBT]] with $\gamma(0) = p$.
Here $\nu(\gamma - p)$ is the least order of vanishing of the components of $\gamma - p$.
The domain $\Omega$ is *of finite type* if $\Delta(p) < \infty$ for every $p \in \partial\Omega$.

## Remarks

The number $\Delta(p)$ does not depend on the choice of $\rho$, since two defining functions differ by a smooth positive factor.
It is also called the D'Angelo type, or the $1$-type.
Example: at a strongly pseudoconvex point $\Delta(p) = 2$, so a bounded [[strongly pseudoconvex domain|Z7RVXBA2KB]] is of finite type.
For $\Omega = \set{\abs{z}^2 + \abs{w}^{2m} < 1}$ in $\C^2$, with $m \ge 1$ an integer, the disc $\gamma(t) = (1, t)$ gives $\rho \circ \gamma(t) = \abs{t}^{2m}$, so $\Delta((1, 0)) \ge 2m$.
Non-example: if $\partial\Omega$ contains a nonconstant holomorphic disc $\gamma$ through $p$, then $\rho \circ \gamma = 0$, so $\Delta(p) = \infty$.
When $n = 2$, the type agrees with the type of Kohn, which is defined by iterated brackets of complex tangent vector fields.
