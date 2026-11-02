---
tag: M5AKNYC4QQ
kind: example
name: Hopf fibration
msc: [55R10, 55Q40, 55R05]
instance_of: [PB9JXQ2KC3]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_fibration
---

## Example

Let $S^3 = \set{(z_0, z_1) \in \C^2 : \abs{z_0}^2 + \abs{z_1}^2 = 1}$, and identify $\R^3$ with $\C \times \R$.
Define $h \colon S^3 \to \R^3$ by
$$h(z_0, z_1) = \bigl(2 z_0 \overline{z_1}, \ \abs{z_0}^2 - \abs{z_1}^2\bigr).$$
The image lies in the unit sphere $S^2$, because
$$\abs{2 z_0 \overline{z_1}}^2 + \bigl(\abs{z_0}^2 - \abs{z_1}^2\bigr)^2 = \bigl(\abs{z_0}^2 + \abs{z_1}^2\bigr)^2 = 1.$$
Two points of $S^3$ have the same image if and only if one is $(\lambda z_0, \lambda z_1)$ for the other $(z_0, z_1)$ and some $\lambda \in \C$ with $\abs{\lambda} = 1$.
So each fibre of $h \colon S^3 \to S^2$ is a circle.
The map $h$ is a fibre bundle with fibre $S^1$, hence a [[Serre fibration|PB9JXQ2KC3]].
Equivalently, $h$ is the quotient map $S^3 \to \C P^1 \cong S^2$, $(z_0, z_1) \mapsto [z_0 : z_1]$.

## Remarks

The [[long exact sequence of homotopy groups|E0RV5D1GQ0]] of $S^1 \to S^3 \to S^2$ gives $\pi_2(S^2) \cong \Z$ and $\pi_3(S^2) \cong \pi_3(S^3) \cong \Z$.
The class of $h$ generates $\pi_3(S^2)$, and $h$ has [[Hopf invariant|TEGTSY7XMX]] $\pm 1$.
Any two fibres are linked circles in $S^3$, with linking number $\pm 1$.
Similar fibrations $S^3 \to S^7 \to S^4$ and $S^7 \to S^{15} \to S^8$ come from the quaternions and the octonions.

## Explanations

### L1 human

The Hopf fibration splits the $3$-sphere into circles, one circle over each point of the ordinary sphere.
No two of these circles are separate: every pair is linked like two rings of a chain.
It was the first example of a map from a sphere to a lower-dimensional sphere that cannot be deformed to a constant map.
