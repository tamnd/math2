---
tag: 0M2JRW1J0N
kind: statement
role: proposition
name: Curl of a gradient is zero
aliases: [curl-grad-vanishes]
msc: [26B12]
uses: [0GDNHS9J2X, 0NS2QYVC4Y, 0NNQY8WCW6, 05R9NF2J49]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_calculus_identities
    locator: Curl of gradient is zero
---

## Statement

Let $U \subseteq \mathbb{R}^3$ be open, and let $\phi \colon U \to \mathbb{R}$ be of class $C^2$.
Then
$$\nabla \times (\nabla \phi) = 0 \quad \text{on } U.$$

## Remarks

Proof: the first component of the [[curl|0GDNHS9J2X]] of $\nabla \phi$ is $\partial_y \partial_z \phi - \partial_z \partial_y \phi$, and this is zero by [[Schwarz's theorem|0NNQY8WCW6]]. The other components are similar.
So a [[conservative|05R9NF2J49]] $C^1$ vector field is irrotational. This gives a quick test: if $\operatorname{curl} F \ne 0$ at some point, then $F$ has no scalar potential.
In $\mathbb{R}^n$, the same argument shows $\partial_i F_j = \partial_j F_i$ for all $i, j$ when $F = \nabla \phi$ with $\phi$ of class $C^2$.
The converse needs a condition on $U$. It holds on [[convex sets|0B22P010D6]], but [[not on every open set|0GRM3BS0DD]].

## Explanations

### L1 human

A gradient field has no swirl.
Going around a small loop in a landscape, you return to the same height. So the field $\nabla \phi$ has no circulation, and its curl is zero.
