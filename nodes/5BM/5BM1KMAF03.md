---
tag: 5BM1KMAF03
kind: definition
name: Proper group action
msc: [54H15, 57S20, "22F05"]
defines: MDH7VXDCVF
uses: [92700QAB5Y, 0WCY42EV9V, 15XEBGNGHC, 0TVJZYB6SH, 0FE2SB8WVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Proper_map
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]] and let $X$ be a topological space.
Let $G$ act continuously on $X$, that is, let a [[group action|0WCY42EV9V]] $G \times X \to X$, $(g, x) \mapsto g \cdot x$, be continuous.
The action is *proper* if the map
$$\theta \colon G \times X \to X \times X, \qquad (g, x) \mapsto (g \cdot x, x)$$
is a [[proper map|15XEBGNGHC]], that is, continuous, closed, and with compact fibres.

## Remarks

When $G$ and $X$ are Hausdorff and [[locally compact|0FE2SB8WVJ]], $\theta$ is proper if and only if the preimage of every [[compact|0TVJZYB6SH]] set is compact.
Then the action is proper if and only if, for every compact $K \subseteq X$, the set $\set{g \in G : (g \cdot K) \cap K \ne \emptyset}$ is compact.

Example: let $G = \Z$ act on $X = \R$ by $n \cdot x = x + n$.
For compact $K \subseteq [-R, R]$, the condition $(n + K) \cap K \ne \emptyset$ forces $\abs{n} \le 2R$, so the set of such $n$ is finite, hence compact in $\Z$.
So the action is proper.

Non-example: let $G = (0, \infty)$ under multiplication act on $X = \R$ by $t \cdot x = tx$.
For $K = [-1, 1]$, the point $0$ lies in $t \cdot K \cap K$ for every $t$, so the set of such $t$ is all of $(0, \infty)$, which is not compact.
So the action is not proper.

Every continuous action of a compact Hausdorff group on a Hausdorff space is proper.
