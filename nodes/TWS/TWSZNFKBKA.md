---
tag: TWSZNFKBKA
kind: definition
name: Deck transformation group
msc: [57M10, 55R05]
defines: BH32RQBX6A
uses: [3XZRRE165N, 0QT00PB5G2, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_space
---

## Definition

Let $p \colon \tilde X \to X$ be a [[covering map|3XZRRE165N]].
A *deck transformation* of $p$ is a [[homeomorphism|0QT00PB5G2]] $f \colon \tilde X \to \tilde X$ such that $p \circ f = p$.
The *deck transformation group* of $p$ is the set of all deck transformations of $p$, with composition of maps as the [[group|G5S1M9]] operation.

## Remarks

Example: for $p \colon \R \to S^1$, $p(t) = (\cos 2\pi t, \sin 2\pi t)$, each translation $t \mapsto t + n$ with $n \in \Z$ is a homeomorphism with $p(t + n) = p(t)$.
These are all the deck transformations, so the group is isomorphic to $\Z$.

Non-example: the translation $t \mapsto t + \tfrac12$ is a homeomorphism of $\R$, but $p(t + \tfrac12) = -p(t) \ne p(t)$, so it is not a deck transformation.

The group is also called the covering transformation group and is written $\operatorname{Deck}(p)$ or $G(\tilde X)$.
If $\tilde X$ is connected, a deck transformation that fixes one point is the identity.
The covering is called normal, or regular, when the group acts transitively on each fibre.
