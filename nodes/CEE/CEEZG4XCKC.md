---
tag: CEEZG4XCKC
kind: statement
role: theorem
name: Gleason's theorem
msc: [81P10, 81P16, 46N50]
uses: [HM2HHE3J51, 0B8KZRT28M, Z2CP530WDE, V1JTB52E8C, MF4DYZ4YAX]
about: [V1JTB52E8C, MF4DYZ4YAX]
sources:
  - url: https://en.wikipedia.org/wiki/Gleason%27s_theorem
same_as:
  wikidata: Q5567394
  wikipedia: Gleason's theorem
---

## Statement

Let $\mathcal{H}$ be a separable real or complex [[Hilbert space|HM2HHE3J51]] with $\dim \mathcal{H} \ge 3$.
Let $\mathcal{P}$ be the set of [[orthogonal projections|0B8KZRT28M]] on $\mathcal{H}$.
Let $\mu \colon \mathcal{P} \to [0, 1]$ be a map with these two properties:

1. $\mu(I) = 1$, where $I$ is the identity operator;
2. $\mu\big(\sum_k P_k\big) = \sum_k \mu(P_k)$ for every finite or countable family $(P_k)$ of mutually orthogonal projections, where $\sum_k P_k$ converges strongly.

Then there is a unique [[density operator|V1JTB52E8C]] $\rho$ on $\mathcal{H}$, that is, a positive [[trace class operator|Z2CP530WDE]] with $\tr \rho = 1$, such that
$$\mu(P) = \tr(\rho P) \quad \text{for all } P \in \mathcal{P}.$$

## Remarks

The heart of the proof is the case $\mathcal{H} = \R^3$.
There one shows that a nonnegative function $f$ on the unit sphere with $f(x) + f(y) + f(z) = 1$ for each orthonormal basis $x, y, z$ is continuous.
It follows that $f$ is a quadratic form, $f(x) = \langle x, \rho x \rangle$; the general case reduces to this one by restriction to real three-dimensional subspaces.
Example: if $\rho = \lvert \psi \rangle\langle \psi \rvert$ for a unit vector $\psi$, the theorem gives $\mu(P) = \norm{P\psi}^2$, the [[Born rule|MF4DYZ4YAX]].
The hypothesis $\dim \mathcal{H} \ge 3$ is necessary.
In $\C^2$, an orthonormal basis is a pair of opposite points $n$ and $-n$ on the Bloch sphere.
So any function $g$ on the sphere with values in $[0, 1]$ and $g(-n) = 1 - g(n)$ satisfies both conditions.
Most such functions, for instance one that is not affine in $n$, do not come from a density operator.

## Explanations

### L1 human

In quantum mechanics a yes-no question about a system is an orthogonal projection, and mutually exclusive questions are orthogonal projections.
Gleason's theorem says that any way to assign probabilities to all such questions, consistent with these exclusions, comes from a density operator by the formula $\tr(\rho P)$.
So the Born rule is not an extra choice: it is the only possible rule once the dimension is at least three.

### L2 human

The theorem shows that the states of quantum mechanics are exactly the probability measures on the lattice of projections.
It also implies the [[Kochen–Specker theorem|X2RF2WKWV9]]: a map from projections to $\set{0, 1}$ satisfying the conditions would give a density operator $\rho$ with $\tr(\rho P) \in \set{0, 1}$ for every rank one $P$.
That is impossible: $P \mapsto \tr(\rho P)$ is continuous on the connected set of rank one projections, hence constant there.
But its values on the projections onto the vectors of an orthonormal basis add up to $1$, and there are at least $3$ of them.
Generalizations replace projections by effects, as in Busch's version for [[POVMs|33BRW6TMY4]], which also works in dimension $2$.
