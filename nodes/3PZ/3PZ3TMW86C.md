---
tag: 3PZ3TMW86C
kind: definition
name: Boolean model
msc: [60D05, 60G55]
defines: NK3CZTVEJD
uses: [05TG0SE4HT, 00R0X1WGPX, 00MRN0FARV, 05DSV40EB9]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_model_(probability_theory)
---

## Definition

Let $d \ge 1$ and $\lambda > 0$.
Let $\Phi = \set{x_1, x_2, \ldots}$ be a homogeneous [[Poisson point process|05TG0SE4HT]] in $\R^d$ with intensity $\lambda$; its points are the *germs*.
Let $K_1, K_2, \ldots$ be [[independent and identically distributed|00MRN0FARV]] random nonempty [[compact sets|00R0X1WGPX]] in $\R^d$, independent of $\Phi$; they are the *grains*.
Let $K$ denote a random set with their common law.
Let $V_d$ be Lebesgue measure on $\R^d$, and let $B$ be the [[closed unit ball|05DSV40EB9]] centred at $0$.
Assume $E[V_d(K + B)] < \infty$, where $K + B = \set{k + b : k \in K, b \in B}$.
The *Boolean model* with these germs and grains is the random set
$$\Xi = \bigcup_{i \ge 1} (x_i + K_i).$$

## Remarks

Under the integrability assumption, only finitely many grains $x_i + K_i$ meet each bounded set almost surely, so $\Xi$ is a random closed set.
Its law is invariant under translations of $\R^d$.

Example: let $d = 2$ and let every grain be the closed disc of radius $r > 0$ centred at $0$.
Then $V_2(K + B) = \pi (r + 1)^2$ is finite, so the assumption holds.
A point $y$ is uncovered exactly when $\Phi$ has no point in the disc of radius $r$ around $y$, which has probability $e^{-\lambda \pi r^2}$.
So the covered fraction of the plane is $p = 1 - e^{-\lambda \pi r^2}$.
In general, $P(y \in \Xi) = 1 - e^{-\lambda E[V_d(K)]}$ for every $y \in \R^d$.

Non-example: put the same discs at the points of the lattice $\Z^2$ instead of a Poisson process.
The union is a union of discs, but the germs do not form a Poisson point process, so it is not a Boolean model.

The Boolean model is also called the Poisson germ-grain model.
