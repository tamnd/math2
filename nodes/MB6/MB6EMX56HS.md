---
tag: MB6EMX56HS
kind: definition
name: Tissot's indicatrix
msc: [86A30, 53A05]
defines: RCMYJPDMGJ
uses: [Y2C8D9VC7D, 0VKCCEXBJ1, 0YYT36R4YD]
sources:
  - url: https://en.wikipedia.org/wiki/Tissot%27s_indicatrix
---

## Definition

Let $P \colon U \to \R^2$ be a [[map projection|Y2C8D9VC7D]] of an open set $U$ of a sphere or an ellipsoid, and let $p \in U$.
Let $T_pU$ be the tangent plane of the surface at $p$, with the inner product induced from $\R^3$.
Let $dP_p \colon T_pU \to \R^2$ be the differential of $P$.
The *Tissot indicatrix* of $P$ at $p$ is the set
$$dP_p\big(\set{v \in T_pU : \norm{v} = 1}\big),$$
the image of the unit circle of $T_pU$.
It is an [[ellipse|0VKCCEXBJ1]] whose semi-axes $a \ge b > 0$ are the singular values of $dP_p$.

## Remarks

Example: for the equirectangular projection $(\varphi, \lambda) \mapsto (R\lambda, R\varphi)$ of the sphere of radius $R$, the scale is $\sec\varphi$ east-west and $1$ north-south, and these directions stay perpendicular, so $a = \sec\varphi$ and $b = 1$.
Non-example: at a pole the Mercator projection is not defined, so it has no indicatrix there.
The area scale at $p$ is $ab$, so $P$ preserves areas near $p$ exactly when $ab = 1$.
The map $P$ is [[conformal|0YYT36R4YD]] at $p$ exactly when $a = b$, that is, when the indicatrix is a circle.
The largest change of an angle at $p$ is $2\arcsin\big((a - b)/(a + b)\big)$.
