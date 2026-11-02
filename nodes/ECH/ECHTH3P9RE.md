---
tag: ECHTH3P9RE
kind: example
name: Ginzburg–Landau functional
msc: [35Q56, 49J45, 82D55]
illustrates: [NW9MM370A5]
uses: [M4CEZ5K9HP, 713MRSZ9XA]
sources:
  - url: https://en.wikipedia.org/wiki/Ginzburg–Landau_theory
---

## Example

Let $\Omega \subseteq \R^2$ be a bounded open set and let $\varepsilon > 0$.
The simplified *Ginzburg–Landau functional* acts on maps $u \colon \Omega \to \C$ in the [[Sobolev space|M4CEZ5K9HP]] $H^1(\Omega; \C)$ by
$$E_\varepsilon(u) = \int_\Omega \Big( \frac12 \abs{\nabla u}^2 + \frac{1}{4 \varepsilon^2} \big(1 - \abs{u}^2\big)^2 \Big) \, dx.$$
The first term penalizes variation of $u$, and the second term pushes $\abs{u}$ towards $1$.

Check of the zero set: $E_\varepsilon(u) = 0$ holds exactly when $\nabla u = 0$ and $\abs{u} = 1$ almost everywhere.
When $\Omega$ is connected, this means that $u$ is a constant of modulus $1$.

Euler–Lagrange equation: the derivative of $E_\varepsilon$ at $u$ in a direction $v$ is
$$\int_\Omega \Big( \operatorname{Re}\big(\nabla u \cdot \overline{\nabla v}\big) - \frac{1}{\varepsilon^2} \big(1 - \abs{u}^2\big) \operatorname{Re}\big(u \, \overline{v}\big) \Big) \, dx.$$
So critical points solve $-\Delta u = \varepsilon^{-2} u \big(1 - \abs{u}^2\big)$ weakly, an equation of [[Ginzburg–Landau type|713MRSZ9XA]] without magnetic field.

## Remarks

Let $\Omega$ be smooth and simply connected.
Impose a boundary condition $u = g$ on $\partial \Omega$, where $g \colon \partial \Omega \to S^1$ is smooth with winding number $d \ne 0$.
No map in $H^1$ with these boundary values has $\abs{u} = 1$ everywhere, so minimizers must have zeros, called vortices.
The minimal energy grows like $\pi \abs{d} \log(1/\varepsilon)$ as $\varepsilon \to 0$.
The study of the limit $\varepsilon \to 0$, by direct estimates and by [[Γ-convergence|NW9MM370A5]] of $E_\varepsilon / \log(1/\varepsilon)$, locates the vortices.
The full functional of Ginzburg–Landau theory also contains a magnetic vector potential.

## Explanations

### L1 human

The functional models a superconductor or a superfluid by a complex number $u$ at each point of a plane domain.
The material prefers $\abs{u} = 1$, and it prefers $u$ not to change.
If the boundary values wind around the circle, both wishes cannot be met, and $u$ must vanish at a few points.
Near these points, the vortices, $u$ turns around once like the hands of a clock.
As $\varepsilon$ gets small, the vortices shrink to points and their positions are what the limit theory describes.
