---
tag: TBRWZE42A8
kind: definition
name: Levi-flat hypersurface
msc: [32V40, 32V05, 53C12]
defines: S4842D7MAE
uses: [JSGWAN2RJV, 80MTNXWW80, ZC78JKZX9S]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] of complex dimension $n \ge 2$.
Let $M \subset X$ be a real hypersurface of class $C^2$.
Near a point $p \in M$, write $M = \set{\rho = 0}$ in local holomorphic coordinates $z = (z_1, \dots, z_n)$, where $\rho$ is a real $C^2$ function with $d\rho \ne 0$ on $M$.
The [[Levi form|80MTNXWW80]] of $M$ at $p$ is the Hermitian form
$$\mathcal{L}_p(w) = \sum_{j,k=1}^{n} \frac{\partial^2 \rho}{\partial z_j \partial \bar z_k}(p)\, w_j \bar w_k$$
on the complex tangent space $H_p = \set{w \in \C^n : \sum_{j} \frac{\partial \rho}{\partial z_j}(p)\, w_j = 0}$.
The hypersurface $M$ is *Levi-flat* if $\mathcal{L}_p = 0$ on $H_p$ for every $p \in M$.

## Remarks

The condition does not depend on the choice of $\rho$ or of the coordinates.
Example: $M = \set{\operatorname{Im} z_1 = 0} \subset \C^n$ with $\rho = \operatorname{Im} z_1 = (z_1 - \bar z_1)/(2i)$.
All mixed derivatives $\partial^2 \rho / \partial z_j \partial \bar z_k$ vanish, so the Levi form is $0$ and $M$ is Levi-flat.
Non-example: the unit sphere $\set{\abs{z_1}^2 + \cdots + \abs{z_n}^2 = 1}$ with $\rho = \abs{z}^2 - 1$.
Its Levi form is $\abs{w_1}^2 + \cdots + \abs{w_n}^2$, which is not zero on $H_p$, since $H_p \ne 0$ when $n \ge 2$.
For a smooth hypersurface, an equivalent condition is that the complex tangent distribution $p \mapsto H_p$ is integrable.
Then $M$ is locally [[foliated|98HTB7MSPX]] by complex hypersurfaces of $X$; this foliation is called the Levi foliation.
A Levi-flat hypersurface is a [[CR manifold|ZC78JKZX9S]] of hypersurface type.
