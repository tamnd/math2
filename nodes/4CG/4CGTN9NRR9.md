---
tag: 4CGTN9NRR9
kind: definition
name: Teichmüller space
msc: [30F60, 32G15]
defines: ZZGC6BZNJ5
uses: [5K0N8QMV6Q, 8AJEMCZ29B, 05GZ11PWRY]
sources:
  - url: https://en.wikipedia.org/wiki/Teichmüller_space
---

## Definition

Let $S$ be a closed, connected, oriented topological surface of genus $g \ge 0$.
A *marked Riemann surface* of type $S$ is a pair $(X, f)$, where $X$ is a [[Riemann surface|5K0N8QMV6Q]] and $f \colon S \to X$ is an orientation-preserving [[homeomorphism|05GZ11PWRY]].
Two marked Riemann surfaces $(X, f)$ and $(Y, h)$ are *equivalent* if there is a [[biholomorphism|8AJEMCZ29B]] $\varphi \colon X \to Y$ such that $\varphi \circ f$ is isotopic to $h$.
The *Teichmüller space* $T(S)$ is the set of equivalence classes of marked Riemann surfaces of type $S$.
It depends up to natural bijection only on $g$ and is written $T_g$.

## Remarks

Riemann surfaces carry their orientation from the complex structure, which is why the marking is required to preserve orientation.
$T_g$ carries a natural complete metric, the Teichmüller metric, defined from the least dilatation of [[quasiconformal maps|SB8KG46NHP]] between marked surfaces.
For $g \ge 2$, $T_g$ is a complex manifold of dimension $3g - 3$, homeomorphic to $\R^{6g - 6}$; $T_0$ is a point.
The mapping class group of $S$ acts on $T(S)$ by changing the marking, and the quotient is the moduli space $M_g$.

Example: $g = 1$.
For $\tau$ in the upper half-plane let $X_\tau = \C / (\Z + \tau \Z)$.
Mark it by the homeomorphism $f_\tau$ from the standard torus $\R^2/\Z^2$ induced by the real linear map sending $(1, 0)$ to $1$ and $(0, 1)$ to $\tau$.
Every marked torus is equivalent to exactly one such $(X_\tau, f_\tau)$, so $T_1$ is identified with the upper half-plane.

Non-example: a pair $(X, f)$ with $f$ orientation-reversing is not a marked Riemann surface, so it is not a point of $T(S)$.
