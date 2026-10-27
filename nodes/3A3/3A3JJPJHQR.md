---
tag: 3A3JJPJHQR
kind: example
name: A translation of the integers is not a homomorphism
msc: [20A05]
not_instance_of:
  - target: 0JYTG5K9Y4
    note: it sends the identity 0 to 1
uses: [0C4JS9RF5M, 0HV9Y7WG5R]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Properties
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[integers|0C4JS9RF5M]] with addition. Define $t : G \to G$ by $t(u) = u + 1$.
A [[homomorphism|0HV9Y7WG5R]] sends the identity to the identity. But $t(0) = 1$, and $1$ is not the identity $0$.
We can also compute directly: $t(0 + 0) = 1$, but $t(0) + t(0) = 2$.
Thus $t$ is not a homomorphism.

## Remarks

$t$ is a bijection, so a bijection between groups need not be an isomorphism.
