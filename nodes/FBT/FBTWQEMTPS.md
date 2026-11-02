---
tag: FBTWQEMTPS
kind: definition
name: Contact structure on a jet bundle
msc: [58A20, 58A30, 35A30]
defines: GCS702QT54
uses: [HC3VBBCJQP, BMCCQ8JXNE, 02Z5B2HA3F, 0E3G0GRPZ6, HBQ8BZ7XB5]
sources:
  - url: https://en.wikipedia.org/wiki/Jet_bundle
---

## Definition

Let $\pi \colon E \to M$ be a smooth fiber bundle, let $k \ge 1$, and let $J^k\pi$ be its $k$-th [[jet bundle|HC3VBBCJQP]].
A [[one-form|02Z5B2HA3F]] $\theta$ on an open set of $J^k\pi$ is a *contact form* if
$$(j^k s)^* \theta = 0$$
for every local section $s$ of $\pi$.
Here $j^k s$ is the [[prolongation|BMCCQ8JXNE]] of $s$, and the pullback is taken where it is defined.
The *contact distribution*, or Cartan distribution, of $J^k\pi$ is the subbundle $\mathcal{C} \subseteq T J^k\pi$ of vectors on which every contact form vanishes.
The contact forms, or equivalently the distribution $\mathcal{C}$, form the *contact structure* of $J^k\pi$.

## Remarks

In adapted coordinates $(x^i, u^\alpha, u^\alpha_I)$, the contact forms are the combinations with smooth coefficients of
$$\theta^\alpha_I = du^\alpha_I - \sum_{i} u^\alpha_{I + i}\, dx^i, \qquad 0 \le \abs{I} \le k - 1,$$
where $u^\alpha_\emptyset = u^\alpha$ and $I + i$ is the multi-index $I$ with $i$ added once.

A local section $\sigma$ of $J^k\pi \to M$ is holonomic, that is, of the form $j^k s$, exactly when $\sigma^*\theta = 0$ for every contact form $\theta$.
For $k = 1$, $M = \R$ and one fiber coordinate this is a direct check: if $\sigma(x) = (x, s(x), q(x))$ then $\sigma^*(du - q\, dx) = (s'(x) - q(x))\, dx$, which vanishes exactly when $q = s'$.

Example: for $\pi \colon \R \times \R \to \R$, $J^1\pi = \R^3$ with coordinates $(x, u, q)$ and $\theta = du - q\, dx$.
Then $d\theta = dx \wedge dq$ and $\theta \wedge d\theta = du \wedge dx \wedge dq \ne 0$.
So $\theta$ is a contact form in the sense of [[contact geometry|HBQ8BZ7XB5]], and $J^1\pi$ is a contact manifold.

Non-example: on the same space the [[form|0E3G0GRPZ6]] $du$ is not a contact form.
For $s(x) = x$ one gets $(j^1 s)^* du = dx \ne 0$.

For $k = 1$ and one fiber coordinate, $J^1\pi$ is a contact manifold for every $\dim M$, with contact form $du - \sum_i u_i\, dx^i$.
For $k > 1$ or more than one fiber coordinate, the contact distribution has codimension greater than $1$.
So it is not a contact structure in the sense of contact geometry, though the name is the same.
