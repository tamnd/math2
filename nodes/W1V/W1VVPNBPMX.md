---
tag: W1VVPNBPMX
kind: definition
name: Properly discontinuous action
msc: [57S30, 54H15, 20H15]
defines: J5X5ED0B2Y
uses: [0WCY42EV9V, 0QT00PB5G2, 0TVJZYB6SH, MDH7VXDCVF, 0S2TEHX4E1]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_space
---

## Definition

Let $\Gamma$ be a group and let $X$ be a topological space.
Let $\Gamma$ [[act|0WCY42EV9V]] on $X$ by [[homeomorphisms|0QT00PB5G2]].
The action is *properly discontinuous* if, for all [[compact|0TVJZYB6SH]] subsets $K, L \subseteq X$, the set
$$\set{\gamma \in \Gamma : (\gamma \cdot K) \cap L \ne \emptyset}$$
is finite.

## Remarks

When $X$ is Hausdorff and locally compact, the action is properly discontinuous if and only if the action of $\Gamma$ with the [[discrete topology|0S2TEHX4E1]] is [[proper|MDH7VXDCVF]].
In covering space theory, some authors use the term for the weaker condition that each point has a neighbourhood $U$ with $\gamma U \cap U = \emptyset$ for all $\gamma \ne 1$.

Example: let $\Z^n$ act on $\R^n$ by translations.
If $K$ and $L$ lie in the ball of radius $R$ about $0$, then $(v + K) \cap L \ne \emptyset$ forces $\norm{v} \le 2R$.
Only finitely many $v \in \Z^n$ satisfy this, so the action is properly discontinuous.

Non-example: let $\Z$ act on $\R$ by $n \cdot x = 2^n x$.
For $K = L = \set{0}$, every $n \in \Z$ satisfies $(n \cdot K) \cap L \ne \emptyset$, so the set is infinite.
So the action is not properly discontinuous.
