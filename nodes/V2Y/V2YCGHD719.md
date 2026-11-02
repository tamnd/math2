---
tag: V2YCGHD719
kind: statement
role: theorem
name: Lewy extension theorem
msc: [32V25, 32D15, 32V10]
uses: [80MTNXWW80, JFKYYK2CEB, 507C34W0ZT]
about: [JFKYYK2CEB]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Statement

Let $n \ge 2$ and let $M$ be a smooth real hypersurface in $\C^n$.
Let $p \in M$, and let $\rho$ be a smooth real function on a neighbourhood $V$ of $p$ with $M \cap V = \set{\rho = 0}$ and $d\rho \ne 0$ on $M \cap V$.
Assume that the [[Levi form|80MTNXWW80]] of $\rho$ at $p$, restricted to the complex tangent space of $M$ at $p$, has at least one positive eigenvalue.
Then there is a neighbourhood $U \subset V$ of $p$ with the following property.
Let $f$ be a [[CR function|JFKYYK2CEB]] of class $C^1$ on $M \cap V$.
Then there is a unique continuous function $F$ on $U \cap \set{\rho \le 0}$ with $F = f$ on $M \cap U$ that is [[holomorphic|507C34W0ZT]] on $U \cap \set{\rho < 0}$.

## Remarks

The theorem is due to Hans Lewy.
One proof fills the side $\set{\rho < 0}$ near $p$ with small analytic discs whose boundaries lie in $M$.
The values of $f$ on the boundary circles define $F$ by the Cauchy integral, and the CR equations make $F$ holomorphic.
If the Levi form at $p$ has eigenvalues of both signs, extensions exist on both sides.
Then $f$ is the restriction of a function holomorphic on a full neighbourhood of $p$.
For the unit sphere with $\rho = \abs{z}^2 - 1$, the Levi form is positive, so CR functions extend locally into the ball.
The hypothesis on the Levi form is needed.
On the [[Levi-flat hypersurface|S4842D7MAE]] $\set{\operatorname{Im} z_1 = 0}$, the function $f(z) = g(\operatorname{Re} z_1)$ is CR for every real $C^1$ function $g$.
If $f$ extended holomorphically to one side, the Schwarz reflection principle in $z_1$ would make $g$ real-analytic, so a $g$ that is $C^1$ but not real-analytic gives no extension.

## Explanations

### L1 human

A CR function lives only on a hypersurface, but it satisfies the part of the Cauchy–Riemann equations that makes sense there.
The theorem says that when the hypersurface curves in a complex direction, such a function is automatically the boundary value of a holomorphic function on one side.
So the data on the thin hypersurface secretly carry a holomorphic function on an open set.

### L2 human

The Lewy extension theorem is a local form of the Hartogs phenomenon for CR functions.
It turns questions about CR functions into questions about holomorphic functions on one-sided neighbourhoods.
It is the starting point of the extension theory of CR functions, which treats submanifolds of higher codimension as well.
A global analogue for the boundary of a bounded domain with connected boundary is the [[Hartogs–Bochner extension theorem|8QYVM1JTMF]].
