---
tag: PRPN60G0GB
kind: definition
name: Conformal compactification and Penrose diagram
msc: ["83C30", "53C50"]
defines: E4TDQZ7DDV
uses: [BY4QYYS788, KZWG5F0TSB, G49G4R1K04, 0YYT36R4YD, JZ9ADDZX8D]
sources:
  - url: https://en.wikipedia.org/wiki/Penrose_diagram
---

## Definition

Let $(M, g)$ be a time-oriented [[Lorentzian manifold|BY4QYYS788]].
A *conformal compactification* of $(M, g)$ consists of a Lorentzian manifold $(\tilde M, \tilde g)$, an open embedding $\psi \colon M \to \tilde M$ with $\overline{\psi(M)}$ compact, and a smooth function $\Omega \colon \tilde M \to \R$ such that

1. $\Omega > 0$ on $\psi(M)$ and $\tilde g = \Omega^2 (\psi^{-1})^* g$ on $\psi(M)$, so $\psi$ is a [[conformal map|0YYT36R4YD]];
2. $\Omega = 0$ on the boundary $\partial \psi(M)$ of $\psi(M)$ in $\tilde M$.

The boundary $\partial \psi(M)$ is the *conformal boundary* of $M$.
Assume $(M, g)$ is spherically symmetric.
A *Penrose diagram* of $M$ is a plane drawing of the two-dimensional quotient $\overline{\psi(M)} / SO(3)$.
Its coordinates are chosen so that radial null curves are straight lines at $\pm 45°$.

## Remarks

Since $\tilde g$ and $g$ differ by a positive factor on $\psi(M)$, they have the same [[light cones|JZ9ADDZX8D]] there, so the compactification keeps the [[causal structure|KZWG5F0TSB]] of $M$.

Example: for [[Minkowski space|G49G4R1K04]] with $ds^2 = -dt^2 + dr^2 + r^2 d\Omega^2$, set $U = \arctan(t - r)$ and $V = \arctan(t + r)$, so $-\pi/2 < U \le V < \pi/2$.
A direct computation gives
$$ds^2 = \frac{1}{4\cos^2 U \cos^2 V} \left( -4\, dU\, dV + \sin^2(V - U)\, d\Omega^2 \right).$$
With $\Omega = 2 \cos U \cos V$, the metric $\tilde g = \Omega^2 g$ is, with $T = V + U$ and $R = V - U$, the metric $-dT^2 + dR^2 + \sin^2 R \, d\Omega^2$ of the Einstein static universe $\R \times S^3$.
Minkowski space becomes the region $\abs{T} + R < \pi$, $R \ge 0$, and its Penrose diagram is a triangle.
Its boundary consists of future and past null infinity $\mathscr{I}^\pm$ (where $V = \pi/2$, resp. $U = -\pi/2$), spatial infinity $i^0$ and future and past timelike infinity $i^\pm$.

Non-example: the identity map of Minkowski space onto itself, with $\Omega = 1$, satisfies clause 1, but $\overline{\psi(M)} = M$ is not compact, so it is not a conformal compactification.
