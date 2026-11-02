---
tag: 902X7EHFSC
kind: statement
role: theorem
name: Hopf degree theorem
msc: [55M25, 55Q05]
uses: [TMFG2P912R, F2F143KQ2M, F45VQ47GPV, T62369RFH6, 913WEQERBE]
about: [TMFG2P912R, F2F143KQ2M]
sources:
  - url: https://en.wikipedia.org/wiki/Degree_of_a_continuous_mapping
---

## Statement

Let $n \ge 1$ and let $M$ be a compact connected [[oriented|913WEQERBE]] [[smooth manifold|F45VQ47GPV]] of dimension $n$ without boundary.
Let $f, g \colon M \to S^n$ be continuous maps to the [[$n$-sphere|T62369RFH6]].
Then $f$ and $g$ are [[homotopic|F2F143KQ2M]] if and only if $\deg f = \deg g$.
Moreover, every integer is the [[degree|TMFG2P912R]] of some continuous map $M \to S^n$.

## Remarks

One direction is the homotopy invariance of degree.
For the other, one may take $f$ and $g$ smooth and use a regular value.
By the Pontryagin–Thom construction, the homotopy class of a map $M \to S^n$ is determined by the framed cobordism class of the preimage of a regular value.
This preimage is a finite set of signed points, and in dimension $0$ such a class is determined by the sum of the signs.
In other words, the degree gives a bijection from the set $[M, S^n]$ of homotopy classes to $\Z$.

Example: for $M = S^1$ and $n = 1$, the theorem says that loops in the circle are classified up to homotopy by their winding number, which recovers $\pi_1(S^1) \cong \Z$.

The dimensions must agree: the Hopf map $S^3 \to S^2$ is not null-homotopic, though $H_3(S^2; \Z) = 0$ so that no degree can distinguish it from a constant map.
If $M$ is not orientable, the same holds with the degree replaced by the degree modulo $2$.

## Explanations

### L1 human

Take two maps from a closed oriented manifold to a sphere of the same dimension, for example from a closed surface to $S^2$.
One can be deformed into the other exactly when both wrap around the sphere the same number of times.
So a single integer tells all about such maps up to deformation.

### L2 human

The theorem computes $[M, S^n] \cong \Z \cong H^n(M; \Z)$ for closed connected oriented $n$-manifolds.
It is a first case of the representability of cohomology by Eilenberg–MacLane spaces.
The reason is that a map $S^n \to K(\Z, n)$ representing a generator induces isomorphisms on $\pi_i$ for $i \le n$, which is enough for maps out of an $n$-dimensional $M$.
It is used to define indices of vector fields and to prove the Poincaré–Hopf theorem, and it is the base case of obstruction theory for maps into spheres.
