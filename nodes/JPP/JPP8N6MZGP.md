---
tag: JPP8N6MZGP
kind: definition
name: Regular and singular points of an analytic set
msc: [32B10, 32C25, 32S05]
defines: ZW5A88PCPK
uses: [VMDTGTMN9P, VKFW27WXEZ, JSGWAN2RJV]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_analytic_variety
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] and let $A$ be an [[analytic subset|VMDTGTMN9P]] of $X$.
A point $a \in A$ is a *regular point* of $A$ if it has an open neighbourhood $U$ in $X$ with the following property.
The set $A \cap U$ is a complex [[submanifold|VKFW27WXEZ]] of $U$.
A point $a \in A$ is a *singular point* of $A$ if it is not a regular point.
The sets of regular and singular points are written $\operatorname{reg} A$ and $\operatorname{sing} A$.

## Remarks

Example: for the cusp $A = \set{z_1^2 = z_2^3}$ in $\C^2$, every point $a \ne 0$ is regular, since the gradient $(2 z_1, -3 z_2^2)$ of $f = z_1^2 - z_2^3$ is nonzero there and the holomorphic implicit function theorem applies.
The origin is singular.
If $A$ were a complex submanifold near $0$, it would have dimension $1$ and be a graph over its tangent line at $0$.
The secant directions from $0$ to $(t^3, t^2)$ tend to the $z_2$-axis, so this tangent line is the $z_2$-axis, but the projection $(t^3, t^2) \mapsto t^2$ to it is two-to-one near $0$.
Regularity is a property of the set, not of the equations.
The set $A = \set{z_1^2 = 0}$ in $\C^2$ is the line $\set{z_1 = 0}$, so all its points are regular, although the gradient of $z_1^2$ vanishes on $A$.
The set $\operatorname{reg} A$ is open in $A$ by definition, and it is dense in $A$.
The set $\operatorname{sing} A$ is a closed analytic subset of $X$ that is nowhere dense in $A$; this is a theorem, not a direct consequence of the definition.
