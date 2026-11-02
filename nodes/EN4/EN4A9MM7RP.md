---
tag: EN4A9MM7RP
kind: definition
name: Anosov flow
msc: [37D20, 37D40]
defines: 8FQJXSA4DT
uses: [HZKFNZTHZS, 0N67NBKQ5T, 02903SSA48, 0QPHW703PV]
sources:
  - url: https://en.wikipedia.org/wiki/Anosov_diffeomorphism
---

## Definition

Let $M$ be a [[compact|0QPHW703PV]] Riemannian manifold with norm $\norm{\cdot}$ on each tangent space.
Let $X$ be a $C^1$ [[vector field|0N67NBKQ5T]] on $M$ with no zeros, and let $\varphi_t$ be its [[flow|02903SSA48]].
The flow $\varphi_t$ is an *Anosov flow* if the following hold.

1. For each $x \in M$ there is a splitting $T_x M = E^s_x \oplus E^0_x \oplus E^u_x$, where $E^0_x$ is the line spanned by $X(x)$.
2. The splitting is invariant: $D\varphi_t(E^s_x) = E^s_{\varphi_t(x)}$ and $D\varphi_t(E^u_x) = E^u_{\varphi_t(x)}$ for all $t \in \R$.
3. There are constants $C > 0$ and $\lambda > 0$ such that, for all $x \in M$ and $t \ge 0$, $\norm{D\varphi_t v} \le C e^{-\lambda t}\norm{v}$ for $v \in E^s_x$ and $\norm{D\varphi_{-t} v} \le C e^{-\lambda t}\norm{v}$ for $v \in E^u_x$.

## Remarks

Example: the [[geodesic flow|VF43FTDA1H]] on the unit tangent bundle of a compact surface of constant curvature $-1$ is an Anosov flow.
In the model $\Gamma \backslash \mathrm{PSL}_2(\R)$, the flow is right multiplication by $a_t = \operatorname{diag}(e^{t/2}, e^{-t/2})$, and $E^s$, $E^u$ are tangent to the orbits of the two [[horocycle flows|2DC88BMQVX]].
Conjugating $\begin{pmatrix} 1 & s \\ 0 & 1\end{pmatrix}$ by $a_t$ multiplies $s$ by $e^{t}$ or by $e^{-t}$, which gives clause 3 with $\lambda = 1$.
Another example is the suspension flow of an [[Anosov diffeomorphism|X1P48KQFXQ]] with constant roof function.
Non-example: the linear flow $\varphi_t(x) = x + t v$ on the torus $\R^n/\Z^n$ has derivative the identity, so no direction is contracted and clause 3 fails.
