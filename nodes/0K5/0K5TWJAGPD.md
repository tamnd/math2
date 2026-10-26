---
tag: 0K5TWJAGPD
kind: example
name: Action by left multiplication
msc: [20B05]
instance_of: [0WCY42EV9V]
uses: [0YSE802YCQ, 0QP2YYR79N, 0B0WE1GKTK]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Examples
---

## Example

Let $G$ be a [[group|G5S1M9]].
The map $G \times G \to G$, $(g, x) \mapsto gx$, is an [[action|0WCY42EV9V]] of $G$ on the set $G$.
The two axioms are $ex = x$ and $g(hx) = (gh)x$, and they follow from the group axioms.
This action is [[transitive|02GK6HZYBT]], because $(yx^{-1})x = y$ for all $x, y \in G$.
The [[stabiliser|0AYMP41THN]] of each point is $\{e\}$, because $gx = x$ implies $g = e$.
In particular, the action is [[faithful|0P7G9NGG2G]], and this gives [[Cayley's theorem|0151VYVX27]].
