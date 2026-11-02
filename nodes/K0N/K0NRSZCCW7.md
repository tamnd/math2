---
tag: K0NRSZCCW7
kind: definition
name: Complex geodesic
msc: [32F45, 32H02]
defines: 275YT975A8
uses: [DY8QQ5GTTX, 3MQTWKBBBT, JSGWAN2RJV]
sources:
  - url: https://en.wikipedia.org/wiki/Kobayashi_metric
---

## Definition

Let $\mathbb{D}$ be the unit disc in $\C$ with its Poincaré distance $\rho$.
Let $X$ be a connected [[complex manifold|JSGWAN2RJV]] with [[Kobayashi pseudodistance|DY8QQ5GTTX]] $k_X$, normalised so that $k_{\mathbb{D}} = \rho$.
A *complex geodesic* of $X$ is a [[holomorphic map|3MQTWKBBBT]] $\varphi \colon \mathbb{D} \to X$ such that
$$k_X(\varphi(a), \varphi(b)) = \rho(a, b) \quad \text{for all } a, b \in \mathbb{D}.$$

## Remarks

Since holomorphic maps decrease Kobayashi distances, the inequality $\le$ always holds; the condition is the reverse inequality.
Some authors use the Carathéodory distance $c_X$ in place of $k_X$; on bounded convex domains the two notions agree, since $c_X = k_X$ there.
Example: in the unit ball $B \subset \C^n$, $\varphi(\zeta) = (\zeta, 0, \dots, 0)$ is a complex geodesic.
Check: the projection $\pi(z) = z_1$ maps $B$ into $\mathbb{D}$ and $\pi \circ \varphi = \id$, so $\rho(a, b) = \rho(\pi\varphi(a), \pi\varphi(b)) \le k_B(\varphi(a), \varphi(b)) \le \rho(a, b)$.
Non-example: $\psi(\zeta) = (\zeta / 2, 0, \dots, 0)$ is holomorphic into $B$, but $k_B(\psi(a), \psi(b)) = \rho(a/2, b/2) < \rho(a, b)$ for $a \ne b$, by the same argument and the Schwarz–Pick lemma for $\zeta \mapsto \zeta/2$.
A complex geodesic is injective, since $\rho(a, b) > 0$ for $a \ne b$.
