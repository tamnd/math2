---
tag: CHP0QWHFWM
kind: definition
name: Path homotopy
msc: [55Q05, 57M05]
defines: CCNKA8C711
uses: [ADDS6HE5SV, 0Q1D85B8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy
---

## Definition

Let $X$ be a topological space and let $I = [0, 1]$ be the unit [[interval|0Q1D85B8G6]].
A *path* in $X$ is a continuous map $\gamma \colon I \to X$, from $\gamma(0)$ to $\gamma(1)$.
Let $\gamma_0, \gamma_1 \colon I \to X$ be paths with $\gamma_0(0) = \gamma_1(0) = x_0$ and $\gamma_0(1) = \gamma_1(1) = x_1$.
A *path homotopy* from $\gamma_0$ to $\gamma_1$ is a continuous map $H \colon I \times I \to X$ such that:

1. $H(s, 0) = \gamma_0(s)$ and $H(s, 1) = \gamma_1(s)$ for all $s \in I$;
2. $H(0, t) = x_0$ and $H(1, t) = x_1$ for all $t \in I$.

The paths are *path homotopic*, written $\gamma_0 \simeq_p \gamma_1$, if a path homotopy exists.

## Remarks

A path homotopy is the same as a [[homotopy relative|ADDS6HE5SV]] to $\set{0, 1}$.
Path homotopy is an equivalence relation on paths from $x_0$ to $x_1$.
Example: in a convex set $C \subseteq \R^n$, the map $H(s, t) = (1 - t)\gamma_0(s) + t \gamma_1(s)$ is a path homotopy, since $H(0, t) = x_0$ and $H(1, t) = x_1$.
Non-example: in $S^1$, the loop $s \mapsto e^{2\pi i s}$ and the constant loop at $1$ are not path homotopic; the [[fundamental group of the circle|6SQXPE0JPN]] tells them apart.
