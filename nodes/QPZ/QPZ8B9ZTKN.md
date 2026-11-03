---
tag: QPZ8B9ZTKN
kind: definition
name: Robust control
msc: [93B35, 93D09, 93B36]
defines: 5MGHZRFCVR
uses: [86JKV3TRFD, 6J9MPVHSMF, 1CF728E75M]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_control
---

## Definition

Let $\mathcal{P}$ be a set of plants, each a finite-dimensional [[linear time-invariant system|6J9MPVHSMF]].
Each plant is given by a proper real-rational [[transfer function|86JKV3TRFD]] matrix of size $p \times m$.
Let $P_0 \in \mathcal{P}$ be the *nominal plant*.
A controller is a proper real-rational transfer function matrix $K$ of size $m \times p$, connected in negative feedback with the plant.
The controller $K$ achieves *robust stability* for $\mathcal{P}$ if the feedback loop of $K$ and $P$ is internally stable for every $P \in \mathcal{P}$.
Given a performance requirement on the closed loop, $K$ achieves *robust performance* if it achieves robust stability and the requirement holds for every $P \in \mathcal{P}$.
*Robust control* is the design of controllers that achieve robust stability, and robust performance, for a given uncertainty set $\mathcal{P}$.

## Remarks

Typical uncertainty sets are $\mathcal{P} = \set{P_0 (I + W \Delta) : \Delta \text{ stable}, \norm{\Delta}_\infty \le 1}$, with a fixed stable weight $W$; these are multiplicative uncertainty sets.
Example: let $P_0(s) = 1/(s + 1)$, $K = k$ a constant gain with $k > 0$, and $\mathcal{P} = \set{a/(s + 1) : 1/2 \le a \le 2}$.
The closed-loop characteristic polynomial is $s + 1 + k a$, whose root $-1 - k a$ is negative for all $a$ in the set, so $K$ is robustly stabilizing.
Non-example: for the set $\mathcal{P} = \set{a/(s - 1) : 1/2 \le a \le 2}$, the gain $k = 1$ stabilizes $a = 2$ but not $a = 1/2$, since the root $1 - k a = 1/2$ is positive.
Let $T = P_0 K/(1 + P_0 K)$ be the complementary sensitivity function.
For multiplicative uncertainty as above with scalar plants, a controller stabilizing $P_0$ is robustly stabilizing if $\norm{W T}_\infty < 1$, by the [[small-gain theorem|1CF728E75M]], and this condition is also necessary.
The concept is broader than this setting: nonlinear plants and parametric uncertainty are also treated.
