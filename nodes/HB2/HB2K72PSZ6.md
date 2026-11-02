---
tag: HB2K72PSZ6
kind: statement
role: theorem
name: Gromov's systolic inequality
msc: [53C23, 53C20]
uses: [PZCJV40M4K, Q61VFHCH2J, 1Y9X1YW6GH]
about: [PZCJV40M4K]
sources:
  - url: https://en.wikipedia.org/wiki/Gromov%27s_systolic_inequality_for_essential_manifolds
same_as:
  wikidata: Q5610194
  wikipedia: Gromov's systolic inequality for essential manifolds
---

## Statement

Let $n \ge 1$ be an integer.
Let $M$ be a closed connected manifold of dimension $n$ with fundamental group $\pi$.
Let $f \colon M \to K(\pi, 1)$ be a map that induces an isomorphism of fundamental groups.
Let $A = \Z$ if $M$ is orientable and $A = \Z/2\Z$ otherwise.
Call $M$ *essential* if $f$ sends the fundamental class of $M$ to a nonzero class of $H_n(K(\pi, 1); A)$.

There is a constant $C_n > 0$, depending only on $n$, with the following property.
For every essential $M$ of dimension $n$ and every [[Riemannian metric|Q61VFHCH2J]] $g$ on $M$,
$$\operatorname{sys}(M, g)^n \le C_n \operatorname{vol}(M, g),$$
where $\operatorname{sys}$ is the [[systole|PZCJV40M4K]].

## Remarks

Gromov's proof goes through the filling radius.
One embeds $M$ isometrically into the Banach space $L^\infty(M)$ by the Kuratowski embedding.
For essential $M$ the filling radius is at least $\operatorname{sys}(M, g)/6$.
On the other hand, a filling inequality bounds the filling radius by a constant times $\operatorname{vol}(M, g)^{1/n}$.

The tori $T^n$, the real projective spaces $\R P^n$ and all closed aspherical manifolds are essential.
For $T^2$ the inequality is a weak form of [[Loewner's torus inequality|1Y9X1YW6GH]].

The hypothesis that $M$ is essential cannot be dropped.
On $S^2 \times S^1$ take the product of a round metric of small area $\varepsilon$ on $S^2$ and a circle of length $1$.
Every noncontractible loop winds around the circle factor, so the systole is $1$, while the volume $\varepsilon$ tends to $0$.

## Explanations

### L1 human

For many manifolds, the shortest loop that cannot be shrunk to a point controls the volume.
If every such loop has length at least $L$, then the volume is at least a fixed multiple of $L^n$.
The theorem gives this for a large class of manifolds, the essential ones, in every dimension.

### L2 human

This is the higher-dimensional extension of Loewner's and Pu's inequalities in [[systolic geometry|PZCJV40M4K]].
The constant $C_n$ from the proof is not optimal, and optimal constants are unknown in most cases.
The notion of essential manifold is topological: it asks that the fundamental class survive in the homology of the classifying space of the fundamental group.
