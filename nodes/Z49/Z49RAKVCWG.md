---
tag: Z49RAKVCWG
kind: statement
role: theorem
name: Hairy ball theorem
msc: [57R25, 55M25]
uses: [T62369RFH6, 0299VCW1TH, TMFG2P912R, F2F143KQ2M]
about: [T62369RFH6, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Hairy_ball_theorem
same_as:
  wikidata: Q1077741
  wikipedia: Hairy ball theorem
---

## Statement

Let $n \ge 1$ and let $S^{2n} = \set{x \in \R^{2n+1} : \norm{x} = 1}$ be the [[sphere|T62369RFH6]] of even dimension $2n$.
Let $v \colon S^{2n} \to \R^{2n+1}$ be a continuous tangent [[vector field|0299VCW1TH]], that is, a continuous map with $v(x) \cdot x = 0$ for all $x \in S^{2n}$.
Then $v(x) = 0$ for some $x \in S^{2n}$.

## Remarks

Suppose $v$ has no zero, and put $w = v / \norm{v}$.
Then $H(x, t) = \cos(\pi t) \, x + \sin(\pi t) \, w(x)$ lies on the sphere and is a homotopy from the identity to the antipodal map.
The identity has [[degree|TMFG2P912R]] $1$ and the antipodal map of $S^{2n}$ has degree $(-1)^{2n+1} = -1$, which contradicts the homotopy invariance of degree.

Example: model the wind on the Earth as a continuous tangent vector field on the sphere $S^2$.
Then at any moment there is a point where the horizontal wind speed is zero.

The dimension must be even: on $S^{2n-1} \subset \R^{2n}$, the field $v(x_1, x_2, \ldots, x_{2n-1}, x_{2n}) = (-x_2, x_1, \ldots, -x_{2n}, x_{2n-1})$ is tangent and has no zero.

## Explanations

### L1 human

You cannot comb the hair on a ball flat without leaving a cowlick or a bald spot.
In mathematical terms, every continuous field of tangent arrows on an ordinary sphere has a point where the arrow is zero.

### L2 human

The theorem follows from the degree of the antipodal map.
It is also the special case of the [[Poincaré–Hopf theorem|4XTPY82PP4]] for $S^{2n}$, since the Euler characteristic of $S^{2n}$ is $2 \neq 0$.
It is the first case of the question how many linearly independent vector fields exist on a sphere, which Adams answered in the theorem on [[vector fields on spheres|3ES79NWRS7]].
It also implies that $S^{2n}$ carries no structure of a Lie group, since left translates of a nonzero tangent vector at the identity would give a nowhere vanishing vector field.
