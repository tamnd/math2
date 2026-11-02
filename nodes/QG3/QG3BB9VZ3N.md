---
tag: QG3BB9VZ3N
kind: definition
name: G2 manifold
msc: [53C29, 53C10, 53C38]
defines: P1TFW9QWAD
uses: [7CBT4SM83Y, WHDZ3MK56B, CAZYGE1T4E, 0E3G0GRPZ6, VYNQVZ8XVF, 1Y4WX4XQWJ]
sources:
  - url: https://en.wikipedia.org/wiki/G2_manifold
---

## Definition

On $\R^7$ with coordinates $x_1, \ldots, x_7$, write $dx_{ijk} = dx_i \wedge dx_j \wedge dx_k$ and let
$$\varphi_0 = dx_{123} + dx_{145} + dx_{167} + dx_{246} - dx_{257} - dx_{347} - dx_{356}.$$
The group $G_2$ is the group of linear maps $A \in GL(7, \R)$ with $A^* \varphi_0 = \varphi_0$.
It is a compact Lie group of dimension $14$ contained in $SO(7)$.

Let $(M, g)$ be a connected [[Riemannian manifold|7CBT4SM83Y]] of dimension $7$.
Identify the tangent space at a point with $\R^7$ by a suitable linear isomorphism.
The manifold $M$ is a *$G_2$ manifold* if its [[holonomy|WHDZ3MK56B]] group is then contained in $G_2$.

## Remarks

Equivalently, $M$ carries a [[$3$-form|0E3G0GRPZ6]] $\varphi$ that agrees with $\varphi_0$ at each point in suitable linear coordinates, that determines $g$, and that is parallel for the [[Levi-Civita connection|CAZYGE1T4E]].
Such a $\varphi$ is a [[$G_2$-structure|VYNQVZ8XVF]], and it is parallel exactly when $d\varphi = 0$ and $d{*\varphi} = 0$, where $*$ is the [[Hodge star|1Y4WX4XQWJ]] of $g$.

Example: $\R^7$ with the Euclidean metric and $\varphi = \varphi_0$; the form has constant coefficients, so it is parallel and the holonomy is trivial.
The flat torus $\R^7 / \Z^7$ is a compact example with the same form.

Non-example: the round sphere $S^7$ is not a $G_2$ manifold.
A metric with holonomy in $G_2$ is Ricci-flat, while the round metric has positive Ricci curvature.

Compact manifolds with holonomy exactly $G_2$ were first constructed by Joyce, by resolving singularities of quotients of $T^7$ by finite groups.
