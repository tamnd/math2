---
tag: XV0MFX6SA2
kind: example
name: Three-dimensional gravity and BTZ black hole
msc: ["83C80", "83C57", "83C15"]
instance_of: [YHJ0PDNY8T]
uses: [3MCZ97SW6V, WVKKDY9V61, EQX6M75VB1, D8NZ32Z3SQ, 1VM1AQT956]
sources:
  - url: https://en.wikipedia.org/wiki/BTZ_black_hole
---

## Example

In a spacetime of dimension $3$, the [[Einstein field equations|3MCZ97SW6V]] in vacuum with [[cosmological constant|WVKKDY9V61]] $\Lambda$ are $R_{ab} - \tfrac{1}{2} R g_{ab} + \Lambda g_{ab} = 0$.
Taking the trace gives $R = 6\Lambda$ and then $R_{ab} = 2\Lambda g_{ab}$.
In dimension $3$ the Weyl tensor vanishes identically, so the Riemann tensor is determined by the Ricci tensor.
Hence every solution has constant sectional curvature $\Lambda$.
So three-dimensional gravity has no local degrees of freedom: every vacuum solution is locally Minkowski, de Sitter or [[anti-de Sitter|EQX6M75VB1]].

Let $\Lambda = -1/\ell^2$ with $\ell > 0$, and use units with $c = 1$ and $8G = 1$.
For constants $M > 0$ and $J$ with $\abs{J} \le M\ell$, the *BTZ black hole* is the metric
$$ds^2 = -f(r)\, dt^2 + \frac{dr^2}{f(r)} + r^2 \left( d\phi - \frac{J}{2r^2}\, dt \right)^2, \qquad f(r) = -M + \frac{r^2}{\ell^2} + \frac{J^2}{4r^2},$$
with $\phi$ an angle of period $2\pi$.
It has constant curvature $-1/\ell^2$, so it solves the equations above, and it is locally isometric to anti-de Sitter space.
The zeros of $f$ are at $r_\pm^2 = \tfrac{\ell^2}{2}\left( M \pm \sqrt{M^2 - J^2/\ell^2} \right)$, and the outer one, $r = r_+$, is an [[event horizon|D8NZ32Z3SQ]].

## Remarks

Check of the horizons: $r^2 f(r) = r^4/\ell^2 - M r^2 + J^2/4$ is a quadratic polynomial in $r^2$ with roots $r_\pm^2$, which are real and nonnegative exactly when $M > 0$ and $\abs{J} \le M\ell$.
For $J = 0$ there is one horizon, at $r_+ = \ell\sqrt{M}$.
The choice $M = -1$, $J = 0$ gives $f(r) = 1 + r^2/\ell^2$, which is anti-de Sitter space itself, and $-1 < M < 0$ gives conical defects, not black holes.
The BTZ black hole has no curvature singularity, since its curvature is constant.
It is a black hole because of its global causal structure.
It is a quotient of a region of anti-de Sitter space by a discrete group of isometries.
It was found by Bañados, Teitelboim and Zanelli in 1992.
Like black holes in four dimensions, it has a Hawking temperature and an entropy proportional to the horizon length $2\pi r_+$.

## Explanations

### L1 human

Gravity in a world with two space dimensions is much simpler than ours: empty space cannot be curved in a varying way, so there are no gravitational waves.
It was a surprise that this world still has black holes when the cosmological constant is negative.
The BTZ black hole has a horizon and a mass, and it can rotate, yet near every point it looks exactly like empty anti-de Sitter space.
Because it is so simple, it is a favourite test case for ideas about quantum gravity and black hole entropy.
