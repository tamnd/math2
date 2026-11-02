---
tag: RT9EYEQ6S2
kind: definition
name: Harmonic functions on Riemann surfaces
msc: [30F15, 31C05]
defines: P214QJ0S3B
uses: [5K0N8QMV6Q, 0DEB0JMN0W, 1VGB63K5HS, 0NAHXR1FRH, 0J78KBPFZB]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_surface
---

## Definition

Let $X$ be a [[Riemann surface|5K0N8QMV6Q]] and let $U \subseteq X$ be an open set.
A function $u \colon U \to \R$ is *harmonic* if for every holomorphic chart $\phi \colon V \to \phi(V) \subseteq \C$ of $X$, the function $u \circ \phi^{-1}$ is [[harmonic|0DEB0JMN0W]] on the open set $\phi(U \cap V)$.

## Remarks

It suffices to check the condition for the charts of one atlas.
Indeed, transition maps are holomorphic, and [[harmonicity is preserved by holomorphic maps|1VGB63K5HS]].
Equivalently, $u$ is harmonic if each point of $U$ has a neighbourhood on which $u = \operatorname{Re} f$ for a [[holomorphic|0NAHXR1FRH]] function $f$.
Example: on $X = \C \setminus \set{0}$ with the chart $z \mapsto z$, the function $u(z) = \log\abs{z}$ is harmonic, since $\Delta \log\abs{z} = 0$ there.
Non-example: $u(z) = \abs{z}^2$ on $X = \C$ is not harmonic, since in the chart $z \mapsto z$ its Laplacian is $4$.
On the [[Riemann sphere|0J78KBPFZB]], or on any compact Riemann surface, the maximum principle forces each harmonic function on the whole surface to be constant.
The Laplacian of $u$ depends on the chart, but the condition $\Delta(u \circ \phi^{-1}) = 0$ does not; in coordinate-free form it reads $\partial \bar\partial u = 0$.
Subharmonic and superharmonic functions on $X$ are defined in the same way, chart by chart.
