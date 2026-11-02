---
tag: KWRF0DEYA2
kind: statement
role: theorem
name: Kontinuitätssatz
msc: [32D05, 32T05]
uses: [4487CSC0MB, 1XCBCB3MD7, 0R6EWFKRCF]
about: [4487CSC0MB]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Statement

Let $D \subseteq \C^n$ be a connected open set that is a [[domain of holomorphy|4487CSC0MB]].
Let $\bar\Delta$ be the closed unit disc in $\C$, with boundary circle $\partial\Delta$.
For $j = 1, 2, \dots$ let $\varphi_j \colon \bar\Delta \to D$ be a continuous map that is holomorphic on the open disc.
If there is a [[compact set|0R6EWFKRCF]] $K \subseteq D$ with $\varphi_j(\partial\Delta) \subseteq K$ for all $j$, then there is a compact set $L \subseteq D$ with $\varphi_j(\bar\Delta) \subseteq L$ for all $j$.

## Remarks

Let $f$ be holomorphic on $D$.
By the maximum principle applied to $f \circ \varphi_j$, the values of $\abs{f}$ on $\varphi_j(\bar\Delta)$ are at most $\max_K \abs{f}$.
So every disc lies in the holomorphically convex hull $\hat K_D$, which is compact by the [[Cartan–Thullen theorem|1XCBCB3MD7]].
Take $L = \hat K_D$.

Example: the Hartogs figure $H = \set{(z_1, z_2) : \abs{z_1} < 1, \abs{z_2} < 1, \ \abs{z_1} < r \text{ or } \abs{z_2} > s}$ fails the conclusion.
Fix $\rho$ with $s < \rho < 1$, choose $c_j$ with $\abs{c_j} < r$ and $c_j \to c$ with $\abs{c} = r$, and let $\varphi_j(\zeta) = (c_j, \rho\zeta)$.
These discs lie in $H$, and their boundaries lie in the compact set $\set{\abs{z_1} \le r, \abs{z_2} = \rho} \subseteq H$.
But the centres $(c_j, 0)$ tend to $(c, 0) \notin H$, so no compact $L \subseteq H$ contains all the discs.
Hence $H$ is not a domain of holomorphy.

The converse also holds: an open set with the disc property of the statement is pseudoconvex, and hence a domain of holomorphy by the solution of the Levi problem.

## Explanations

### L1 human

Think of a sequence of holomorphic discs inside a domain whose rims stay in a fixed compact region.
In a domain of holomorphy the discs themselves cannot escape to the boundary either.
If a domain allows the discs to run out while their rims stay inside, then holomorphic functions get trapped and must extend.

### L2 human

The continuity principle is one of the oldest forms of pseudoconvexity.
It is a convenient practical test.
A single family of discs whose rims stay inside but whose centres leave the domain shows that the domain is not a domain of holomorphy.
The proof above shows how it follows from holomorphic convexity and the maximum principle.
