---
tag: NY9MCZXY6N
kind: definition
name: Hyperbolic set
msc: [37D05, 37D20]
defines: MPFD24TYW2
uses: [5HDG31YEPW, 0Z1Y7JHGBR, 80QZ05NFCB, 565B0Y76XE, 0QPHW703PV]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_set
---

## Definition

Let $M$ be a [[Riemannian manifold|5HDG31YEPW]] with norm $\norm{\cdot}$ on each tangent space, and let $f \colon M \to M$ be a $C^1$ [[diffeomorphism|0Z1Y7JHGBR]] with [[differential|565B0Y76XE]] $Df$.
A set $\Lambda \subseteq M$ is a *hyperbolic set* of $f$ if the following hold.

1. $\Lambda$ is [[compact|0QPHW703PV]] and $f(\Lambda) = \Lambda$.
2. For each $x \in \Lambda$ there is a splitting $T_x M = E^s_x \oplus E^u_x$ with $Df_x(E^s_x) = E^s_{f(x)}$ and $Df_x(E^u_x) = E^u_{f(x)}$.
3. There are constants $C > 0$ and $0 < \lambda < 1$ such that, for all $x \in \Lambda$ and $n \ge 0$, $\norm{Df^n_x v} \le C \lambda^n \norm{v}$ for $v \in E^s_x$ and $\norm{Df^{-n}_x v} \le C \lambda^n \norm{v}$ for $v \in E^u_x$.

## Remarks

The subspaces $E^s_x$ and $E^u_x$ are then unique and depend continuously on $x$.
Changing the Riemannian metric changes $C$ but not the property, because $\Lambda$ is compact; an adapted metric allows $C = 1$.
Example: a fixed point $p$ of $f$ is a hyperbolic set exactly when no eigenvalue of $Df_p$ has modulus $1$.
For $f(x, y) = (x/2, 2y)$ on $\R^2$ and $\Lambda = \set{0}$, take $E^s$ the $x$-axis, $E^u$ the $y$-axis, $C = 1$ and $\lambda = 1/2$.
Non-example: for the rotation $f(z) = e^{i\theta} z$ of $\R^2 = \C$, the set $\set{0}$ is compact and invariant, but $Df_0$ preserves lengths, so no splitting satisfies clause 3.
A flow version replaces clause 2 by $T_x M = E^s_x \oplus E^0_x \oplus E^u_x$, where $E^0_x$ is spanned by the vector field, as in the definition of an [[Anosov flow|EN4A9MM7RP]].
