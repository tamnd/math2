---
tag: DC9NJQPF1S
kind: statement
role: theorem
name: Day's fixed point theorem
msc: ["43A07", "47H10", "46A55"]
uses: [G5S1M9, B6GY2KJMWW, 02AS45T3H9, 0R6EWFKRCF, 0JF0TVYGWT, CEAT9BESKK, H9AFGFG4RB]
about: [CEAT9BESKK]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_group
---

## Statement

Let $G$ be a [[group|G5S1M9]], with no topology.
Then $G$ is [[amenable|CEAT9BESKK]] if and only if the following fixed point property holds.
Let $K$ be a nonempty [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]] in a Hausdorff [[locally convex space|B6GY2KJMWW]].
Let $G$ act on $K$ so that each map $x \mapsto g \cdot x$ is continuous and [[affine|0JF0TVYGWT]].
Then there is a point $x \in K$ with $g \cdot x = x$ for all $g \in G$.

## Remarks

Suppose $G$ has the fixed point property.
Let $K$ be the weak-$*$ compact convex set of means on $\ell^\infty(G)$, with the action $(g \cdot m)(f) = m(g^{-1} \cdot f)$.
A fixed point is an invariant mean.
Conversely, let $m$ be an invariant mean and fix $x_0 \in K$.
For each continuous affine function $\varphi$ on $K$, the bounded function $g \mapsto \varphi(g \cdot x_0)$ has a mean.
In a locally convex space this defines a barycenter $x \in K$ with $\varphi(x) = m(g \mapsto \varphi(g \cdot x_0))$.
The invariance of $m$ makes $x$ fixed.

Example: for an abelian group, the theorem follows from the [[Markov–Kakutani fixed-point theorem|H9AFGFG4RB]].
For the free group $F_2$ the fixed point property fails, since the set of means on $\ell^\infty(F_2)$ has no fixed point.

For a locally compact group, the same equivalence holds when the action $G \times K \to K$ is jointly continuous.

## Explanations

### L1 human

A group is amenable exactly when every way it can act by affine maps on a compact convex set has a common fixed point.
The fixed point is a kind of center of mass of an orbit, taken with respect to an invariant average on the group.
So amenability means "one can always average".

### L2 human

Day's theorem is a standard tool to produce invariant objects for actions of amenable groups.
Examples are invariant probability measures for continuous actions on compact spaces, obtained by taking $K$ to be the probability measures on the space.
For a non-amenable group, some action on a compact space has no invariant probability measure, and this is one way to detect non-amenability.
