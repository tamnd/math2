---
tag: 6GZ8DXT7TN
kind: example
name: Prandtl's lifting-line equation
msc: [76G25, "45E05", 45J05]
illustrates: [E30EA6ETZ4]
uses: [0SYR10HD4R, 5JYBXH9BP6, E30EA6ETZ4]
sources:
  - url: https://en.wikipedia.org/wiki/Lifting-line_theory
---

## Example

Consider a wing of span $2s$ along the axis $-s \le y \le s$, in a uniform flow of speed $V$.
Let $c(y)$ be the chord, $\alpha(y)$ the geometric angle of attack and $\alpha_0(y)$ the angle of zero lift of the section at $y$.
Assume the sections have the thin airfoil lift slope $2\pi$.
*Prandtl's lifting-line equation* for the circulation $\Gamma(y)$ is
$$\Gamma(y) = \pi V c(y) \bigl(\alpha(y) - \alpha_0(y)\bigr) - \frac{c(y)}{4}\, \mathrm{PV}\!\int_{-s}^{s} \frac{\Gamma'(\eta)}{y - \eta}\, d\eta, \quad -s < y < s,$$
with $\Gamma(\pm s) = 0$, where $\mathrm{PV}$ is the [[Cauchy principal value|0SYR10HD4R]].
The integral term is $\pi V c(y)\, \alpha_i(y)$, where the induced angle is $\alpha_i(y) = \frac{1}{4\pi V}\, \mathrm{PV}\!\int_{-s}^{s} \frac{\Gamma'(\eta)}{y - \eta}\, d\eta$.
It is a singular integro-differential equation: the derivative of the unknown appears under a Cauchy kernel, so it is close to a [[singular integral equation|E30EA6ETZ4]].

Check with the elliptic distribution $\Gamma(y) = \Gamma_0 \sqrt{1 - y^2/s^2}$.
Substituting $y = s x$ and $\eta = s t$ gives
$$\alpha_i = \frac{\Gamma_0}{4\pi V s}\, \mathrm{PV}\!\int_{-1}^{1} \frac{t}{\sqrt{1 - t^2}\,(t - x)}\, dt = \frac{\Gamma_0}{4 V s},$$
since $\frac{1}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{t\, dt}{\sqrt{1 - t^2}\,(t - x)} = 1$ for $-1 < x < 1$.
So the induced angle is constant along the span.
For an untwisted wing with $\alpha$ constant, $\alpha_0 = 0$ and elliptic chord $c(y) = c_0 \sqrt{1 - y^2/s^2}$, the equation reduces to $\Gamma_0 = \pi V c_0 \bigl(\alpha - \Gamma_0/(4 V s)\bigr)$.
It gives $\Gamma_0 = \pi V c_0 \alpha / \bigl(1 + \pi c_0/(4 s)\bigr)$.

## Remarks

The integral term is a [[finite Hilbert transform|5JYBXH9BP6]] of $\Gamma'$ after scaling to $[-1, 1]$.
A standard way to solve the equation in general expands $\Gamma$ in the Fourier sine series $\Gamma = \sum_n A_n \sin(n\theta)$ with $y = -s \cos\theta$.
The Cauchy integral acts diagonally on this basis, and the equation becomes a linear system for the coefficients $A_n$.

## Explanations

### L1 human

A wing of finite length leaves trailing vortices at its tips, and these push the air near the wing downwards.
This downwash lowers the effective angle of attack, so the lift at each point depends on the lift everywhere else along the span.
Prandtl's equation writes this coupling as one equation for the circulation along the span.
For an elliptic wing the downwash is the same everywhere, and the equation can be solved by hand.
