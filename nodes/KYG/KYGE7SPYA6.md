---
tag: KYGE7SPYA6
kind: definition
name: Topological transformation group
msc: [54H15, 22F05]
defines: 2B8KYPCPAS
uses: [92700QAB5Y, 0CQHFPGJ45, 0WCY42EV9V, 0GBG8B49AA, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_group_action
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]] and let $X$ be a [[topological space|0CQHFPGJ45]].
A *topological transformation group* is a triple $(G, X, \alpha)$ where $\alpha \colon G \times X \to X$ is a [[group action|0WCY42EV9V]] of $G$ on $X$, written $\alpha(g, x) = g \cdot x$, such that $\alpha$ is [[continuous|0VGFHTM75Y]].
Here $G \times X$ carries the [[product topology|0GBG8B49AA]].
One also says that $G$ acts continuously on $X$.

## Remarks

Example: the group $\mathrm{SO}(3)$ of rotations of $\R^3$, with the topology from the matrix entries, acting on the unit sphere $S^2$ by $(A, x) \mapsto Ax$.
The map is given by polynomials in the entries of $A$ and the coordinates of $x$, so it is continuous.
Non-example: $(\R, +)$ with the usual topology acting on $\R$ with the discrete topology by $(t, x) \mapsto t + x$.
This is a group action, but it is not continuous: for fixed $x$, the map $t \mapsto t + x$ from $\R$ to the discrete space is not continuous.
For each $g \in G$ the map $x \mapsto g \cdot x$ is a homeomorphism of $X$, with inverse $x \mapsto g^{-1} \cdot x$.
