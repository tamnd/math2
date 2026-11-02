---
tag: PT1P6Z6GEY
kind: definition
name: Complex manifold
msc: [32Q99, 53C15]
defines: JSGWAN2RJV
uses: [0S1FJ8VEX9, 03PPNCM9GG, J7P32JQTVE, 3MQTWKBBBT, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_manifold
---

## Definition

Let $n \ge 0$ and let $M$ be a [[Hausdorff|0S1FJ8VEX9]], [[second-countable|03PPNCM9GG]] topological space.
A *complex chart* on $M$ is a pair $(U, \varphi)$ with $U \subset M$ open and $\varphi$ a [[homeomorphism|0QT00PB5G2]] of $U$ onto an open subset of $\C^n$.
A *holomorphic atlas* is a family of complex charts $(U_\alpha, \varphi_\alpha)$ such that:

1. the sets $U_\alpha$ cover $M$;
2. for all $\alpha, \beta$, the transition map $\varphi_\beta \circ \varphi_\alpha^{-1} \colon \varphi_\alpha(U_\alpha \cap U_\beta) \to \varphi_\beta(U_\alpha \cap U_\beta)$ is [[holomorphic|3MQTWKBBBT]].

Two holomorphic atlases are equivalent if their union is a holomorphic atlas.
A *complex manifold of dimension $n$* is such a space $M$ together with an equivalence class of holomorphic [[atlases|J7P32JQTVE]], called a *complex structure*.
A function $f \colon V \to \C$ on an open set $V \subset M$ is holomorphic if $f \circ \varphi^{-1}$ is holomorphic for every chart $(U, \varphi)$ of the structure.

## Remarks

Example: the [[Riemann sphere|0J78KBPFZB]] $\hat\C = \C \cup \set{\infty}$ with the charts $\varphi_0(z) = z$ on $\C$ and $\varphi_\infty(z) = 1/z$ on $\hat\C \setminus \set{0}$, with $\varphi_\infty(\infty) = 0$.
On the overlap, $\varphi_0(\C \setminus \set{0}) = \C \setminus \set{0}$, and the transition map $w \mapsto 1/w$ is holomorphic there; so $\hat\C$ is a complex manifold of dimension $1$.

Non-example: on $\C$, the two charts $\varphi_1(z) = z$ and $\varphi_2(z) = \bar z$ do not form a holomorphic atlas.
Each is a homeomorphism onto $\C$, but the transition map $w \mapsto \bar w$ is not holomorphic, so clause 2 fails.

Every complex manifold of dimension $n$ is a smooth manifold of dimension $2n$, since holomorphic maps are smooth.
It is canonically oriented, because the real Jacobian determinant of a holomorphic map is $\abs{\det J_\C}^2 \ge 0$, where $J_\C$ is its complex Jacobian matrix.
Further examples are open subsets of $\C^n$, [[complex projective space|7GJ4STCNNM]], [[complex tori|Y7MA6KBE9M]] and [[Hopf manifolds|Z8R2D33WSM]].
A complex structure induces an [[almost complex structure|9SYWRGVTRS]]; by the [[Newlander–Nirenberg theorem|VCT848WV1T]], the almost complex structures that arise this way are exactly the integrable ones.
