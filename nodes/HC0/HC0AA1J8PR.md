---
tag: HC0AA1J8PR
kind: statement
role: theorem
name: Buchdahl's theorem
msc: ["83C55", "83C15"]
uses: [2T335F8H8F, H4FNPG6ZY1, 6Y50T68WKY, 3MCZ97SW6V, G48AGJAZNG]
about: [2T335F8H8F]
sources:
  - url: https://en.wikipedia.org/wiki/Buchdahl%27s_theorem
same_as:
  wikidata: Q18415473
  wikipedia: Buchdahl's theorem
---

## Statement

Let $G$ be the gravitational constant and $c$ the speed of light.
Consider a static, spherically symmetric solution of the [[Einstein field equations|3MCZ97SW6V]] with zero cosmological constant.
Assume it consists of a ball of [[perfect fluid|H4FNPG6ZY1]] of radius $R$, regular at the centre, surrounded by vacuum.
Assume the mass density $\rho(r)$ satisfies $\rho \ge 0$ and is non-increasing in $r$, and the pressure $p \ge 0$.
Let $M$ be the mass of the exterior [[Schwarzschild metric|6Y50T68WKY]].
Then
$$\frac{2GM}{Rc^2} \le \frac{8}{9}, \qquad \text{that is,} \qquad R \ge \frac{9}{4} \frac{GM}{c^2}.$$

## Remarks

The proof works with the [[Tolman–Oppenheimer–Volkoff equation|2T335F8H8F]].
One writes the metric as $-e^{2\nu} c^2 dt^2 + (1 - 2Gm/(rc^2))^{-1} dr^2 + r^2 d\Omega^2$ and shows from the field equations that, when the mean density $m(r)/r^3$ does not increase, $\zeta = e^{\nu}$ satisfies an inequality that makes $\frac{d}{dr}\left(\frac{1}{r}\sqrt{1 - 2Gm/(rc^2)}\, \frac{d\zeta}{dr}\right) \le 0$.
Integrating this from the centre to the surface and requiring the central value of $\zeta$ to be positive gives the bound.

The bound is sharp: the constant-density star, the interior Schwarzschild solution, has central pressure that becomes infinite exactly as $R$ decreases to $\frac94 GM/c^2$.
So no static star with these hypotheses can be more compact than this.
In particular $R$ is strictly larger than the [[Schwarzschild radius|G48AGJAZNG]] $2GM/c^2$, so such a star cannot be compressed to a black hole while staying static.
Without the hypotheses on the matter, for example with anisotropic stresses or negative pressures, the bound can fail.

## Explanations

### L1 human

A star made of ordinary fluid cannot be squeezed too much without collapsing.
Buchdahl's theorem gives the limit: its radius must be at least $9/4$ times $GM/c^2$, a little more than the radius at which it would become a black hole.
This holds whatever the material of the star, as long as its density does not grow toward the surface.

### L2 human

The theorem is a universal compactness bound: it does not need any equation of state.
It shows that there is a gap between the most compact static fluid stars and black holes.
Its proof is an elementary but clever use of the TOV equations, and similar arguments give bounds with charge or a cosmological constant.
