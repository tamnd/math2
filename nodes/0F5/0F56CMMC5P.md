---
tag: 0F56CMMC5P
kind: statement
role: proposition
name: Divergence of a curl is zero
aliases: [div-curl-vanishes]
msc: [26B12]
uses: [02NSMQVQWK, 0GDNHS9J2X, 0NNQY8WCW6]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_calculus_identities
    locator: Divergence of curl is zero
  - url: https://en.wikipedia.org/wiki/Divergence
    locator: Properties
---

## Statement

Let $U \subseteq \mathbb{R}^3$ be open, and let $A \colon U \to \mathbb{R}^3$ be a vector field of class $C^2$.
Then
$$\nabla \cdot (\nabla \times A) = 0 \quad \text{on } U.$$

## Remarks

Proof: with $A = (A_1, A_2, A_3)$, the [[divergence|02NSMQVQWK]] of the [[curl|0GDNHS9J2X]] is $\partial_x (\partial_y A_3 - \partial_z A_2) + \partial_y (\partial_z A_1 - \partial_x A_3) + \partial_z (\partial_x A_2 - \partial_y A_1)$. The six terms cancel in pairs by [[Schwarz's theorem|0NNQY8WCW6]].
So a field that has a vector potential is divergence-free. On an open ball, the converse is also true: a $C^1$ divergence-free field is the curl of some field.
The identity is a special case of the rule [[d d = 0|0X308R2DBE]] for the exterior derivative.

## Explanations

### L1 human

The curl of a field describes rotation, and pure rotation does not create or destroy anything.
So the curl of any smooth field has no sources or sinks, which means its divergence is zero.
