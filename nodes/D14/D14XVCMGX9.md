---
tag: D14XVCMGX9
kind: definition
name: Extremally disconnected space
msc: [54G05]
defines: 370PJ5BF70
uses: [0CQHFPGJ45, 0QEAJB91GZ, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Extremally_disconnected_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
The space $X$ is *extremally disconnected* if for every [[open set|02BH3MCBQB]] $U \subseteq X$, the [[closure|0QEAJB91GZ]] $\overline{U}$ is open in $X$.

## Remarks

Example: a discrete space is extremally disconnected.
Every subset is open, so in particular every closure is open.

Non-example: $\R$ with the usual topology is not extremally disconnected.
The set $(0, 1)$ is open, and its closure $[0, 1]$ is not open.

An equivalent condition: for all disjoint open sets $U, V \subseteq X$, the closures $\overline{U}$ and $\overline{V}$ are disjoint.
Some authors also require $X$ to be Hausdorff.
An extremally disconnected Hausdorff space is [[totally disconnected|0RJSBR9GW1]].
