---
tag: G0GQ89YCDB
kind: definition
name: Lifting-line theory
msc: [76G25, 76B47]
defines: YFM3DBFHWV
uses: [EYCZ9SGBND, BTHH4Y71QR, TZM7XNR4V0, ZXKV1HSQMW, 0SYR10HD4R]
sources:
  - url: https://en.wikipedia.org/wiki/Lifting-line_theory
---

## Definition

Consider a straight, unswept wing of span $b$ along the axis $-b/2 \le y \le b/2$, in a steady incompressible inviscid stream of speed $V$ and density $\rho$.
Let $c(y)$ be the chord, $\alpha(y)$ the geometric angle of attack and $\alpha_0(y)$ the zero-lift angle of the section at $y$.
*Lifting-line theory* is the model of this flow in which:

1. the wing is replaced by a bound vortex along the span with [[circulation|BTHH4Y71QR]] $\Gamma(y)$, where $\Gamma(\pm b/2) = 0$;
2. a sheet of straight trailing vortices leaves the line downstream; the strip $[y, y + dy]$ sheds a vortex of strength $\Gamma'(y)\, dy$ in absolute value.
By the [[Biot–Savart law|ZXKV1HSQMW]] this sheet induces the angle
$$\alpha_i(y) = \frac{1}{4\pi V}\, \mathrm{PV}\!\int_{-b/2}^{b/2} \frac{\Gamma'(\eta)}{y - \eta}\, d\eta;$$
3. each section behaves like a two-dimensional [[thin airfoil|EYCZ9SGBND]] at the effective angle $\alpha - \alpha_i$, so that
$$\Gamma(y) = \pi V c(y) \bigl(\alpha(y) - \alpha_0(y) - \alpha_i(y)\bigr).$$

Here $\mathrm{PV}$ is the [[Cauchy principal value|0SYR10HD4R]].
The lift is $L = \rho V \int_{-b/2}^{b/2} \Gamma(y)\, dy$, by the [[Kutta–Joukowski theorem|TZM7XNR4V0]] applied to each section, and the induced drag is $D_i = \rho V \int_{-b/2}^{b/2} \Gamma(y)\, \alpha_i(y)\, dy$.

## Remarks

Example: the elliptic distribution $\Gamma(y) = \Gamma_0 \sqrt{1 - 4y^2/b^2}$ gives a constant induced angle $\alpha_i = \Gamma_0 / (2Vb)$.
With wing area $S$ and aspect ratio $AR = b^2 / S$, this gives $C_{D,i} = C_L^2 / (\pi\, AR)$ for the coefficients relative to $\frac{1}{2}\rho V^2 S$.
For any other distribution $C_{D,i} = C_L^2 / (\pi e\, AR)$ with a span efficiency $e < 1$.
Non-example: a swept wing or a wing of small aspect ratio, such as a delta wing, is outside the model.
A single straight line cannot represent how the circulation varies along the chord there.
Combining clauses 2 and 3 gives [[Prandtl's lifting-line equation|6GZ8DXT7TN]].
