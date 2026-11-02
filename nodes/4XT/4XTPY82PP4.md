---
tag: 4XTPY82PP4
kind: statement
role: theorem
name: Poincaré–Hopf theorem
msc: [57R25, 55M25]
uses: [F45VQ47GPV, 0299VCW1TH, RNDDWDAFJ5, TMFG2P912R]
about: [0299VCW1TH, RNDDWDAFJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Poincaré–Hopf_theorem
same_as:
  wikidata: Q1305766
  wikipedia: Poincaré–Hopf theorem
---

## Statement

Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] of dimension $n$ without boundary.
Let $v$ be a continuous [[vector field|0299VCW1TH]] on $M$ with only isolated zeros.
For a zero $x$ of $v$, choose a chart around $x$ and a small sphere $S$ around $x$ in it that encloses no other zero.
The *index* $\operatorname{ind}_x(v)$ is the [[degree|TMFG2P912R]] of the map $S \to S^{n-1}$, $u \mapsto v(u) / \norm{v(u)}$.
Then $v$ has finitely many zeros, and
$$\sum_{v(x) = 0} \operatorname{ind}_x(v) = \chi(M),$$
the [[Euler characteristic|RNDDWDAFJ5]] of $M$.

## Remarks

The index does not depend on the chart.
One proof first shows that the sum of indices does not depend on $v$.
For this it compares $v$ with a field on a tubular neighbourhood of $M$ in $\R^N$ and uses the degree of the Gauss map.
Then one computes the sum for the gradient of a Morse function, whose zeros are the critical points.
The index at a critical point of Morse index $\lambda$ is $(-1)^\lambda$, and the sum of these signs is $\chi(M)$ by Morse theory.
For a manifold with boundary the same formula holds if $v$ points outward along the boundary.

Example: on the sphere $S^2$, the gradient of the height function vanishes only at the two poles, a source and a sink, each of index $+1$, and $1 + 1 = 2 = \chi(S^2)$.
On the torus, the field tangent to one family of circles has no zero, and $\chi(T^2) = 0$.

Compactness is needed: the constant field on $\R^n$ has no zero, but $\chi(\R^n) = 1$.

## Explanations

### L1 human

Count the points where a flow on a closed surface stops, giving each one a sign or multiplicity according to how the flow turns around it.
The total does not depend on the flow; it is the Euler characteristic, a number that only depends on the shape of the surface.
On a sphere the total is $2$, so every flow on a sphere must stop somewhere.

### L2 human

The theorem links analysis, through vector fields, with topology, through the Euler characteristic.
It gives the [[hairy ball theorem|Z49RAKVCWG]] at once.
It shows that a closed manifold has a nowhere vanishing vector field only if $\chi(M) = 0$, and Hopf proved the converse for connected closed manifolds.
It can be derived from the Lefschetz fixed-point theorem applied to the flow of $v$.
It is closely related to the Gauss–Bonnet theorem and to the Euler class of the tangent bundle.
