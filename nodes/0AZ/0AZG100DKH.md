---
tag: 0AZG100DKH
kind: example
name: Action on left cosets
msc: [20B05]
instance_of: [0WCY42EV9V]
uses: [0YSE802YCQ, 05FD317V2W, 0QP2YYR79N, 0T0KMZPYV9]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Examples
---

## Example

Let $G$ be a [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
Let $G/H$ be the set of the [[left cosets|03DEH43F4H]] of $H$ in $G$.
The map $G \times G/H \to G/H$, $(g, aH) \mapsto gaH$, is an [[action|0WCY42EV9V]] of $G$ on $G/H$.
The map is well defined, because $aH = bH$ implies $gaH = gbH$.
The action is [[transitive|02GK6HZYBT]], because $(ba^{-1}) \cdot aH = bH$.
The [[stabiliser|0AYMP41THN]] of the coset $aH$ is the conjugate subgroup $aHa^{-1}$.
The kernel of the associated homomorphism $G \to \operatorname{Sym}(G/H)$ is the [[normal core|0GETX79CJN]] of $H$, the intersection of all conjugates of $H$.
For $H = \{e\}$, this is the [[action by left multiplication|0K5TWJAGPD]].
