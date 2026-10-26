---
tag: 0MM45BT6HC
kind: definition
name: One-point compactification
msc: [54D35]
defines: 0GWN3CMRK8
uses: [0CNQXVBHCX, 00R0X1WGPX, 0G5AV9Q4RR, 0EQMWQ4WMJ, 0MXB4CKHFW]
sources:
  - url: https://en.wikipedia.org/wiki/Alexandroff_extension
    locator: The Alexandroff extension
---

## Definition

Let $(X, \tau)$ be a [[topological space|0CNQXVBHCX]] and let $\infty$ be a point not in $X$. Let $X^* = X \cup \{\infty\}$.
The one-point compactification, or Alexandroff extension, of $X$ is the set $X^*$ with the following topology.
The open sets are the sets $U \in \tau$ and the sets $X^* \setminus C$, where $C \subseteq X$ is [[closed|0G5AV9Q4RR]] and [[compact|00R0X1WGPX]] in $X$.

## Remarks

The space $X^*$ is compact, and $X$ is an open subspace of $X^*$.
The space $X^*$ is Hausdorff if and only if $X$ is [[locally compact|0EQMWQ4WMJ]] and [[Hausdorff|0MXB4CKHFW]].
The one-point compactification of $\mathbb{R}^n$ is homeomorphic to the sphere $S^n$, by stereographic projection. For $n = 1$, it is the circle.

## Explanations

### L1 human

You make a non-compact space compact by adding one point, and you declare that the new point is near everything outside large compact sets.
The real line becomes a circle: both ends meet at the new point.
