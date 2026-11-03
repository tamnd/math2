---
tag: 8V5JJ98MTJ
kind: definition
name: Grad–Shafranov equation
msc: [76W05, 35Q35, 76X05]
defines: 8XC0NEBJD0
uses: [ZSA13P8P81, T8JWCBK9M6, B4TTNHSTRX]
sources:
  - url: https://en.wikipedia.org/wiki/Grad–Shafranov_equation
---

## Definition

Use cylindrical coordinates $(R, \varphi, Z)$ on $\R^3$, and let $\mu_0$ be the magnetic permeability.
Consider a static equilibrium of [[ideal MHD|ZSA13P8P81]], given by a pressure $p$ and a magnetic field $\mathbf{B}$ with
$$\nabla p = \mathbf{J} \times \mathbf{B}, \qquad \mu_0 \mathbf{J} = \nabla \times \mathbf{B}, \qquad \nabla \cdot \mathbf{B} = 0.$$
Assume that $p$ and $\mathbf{B}$ do not depend on $\varphi$.
Write the field as
$$\mathbf{B} = \frac{1}{R} \nabla \psi \times \mathbf{e}_\varphi + \frac{F}{R} \mathbf{e}_\varphi$$
with the poloidal flux function $\psi(R, Z)$ and $F = R B_\varphi$.
Then $p$ and $F$ are functions of $\psi$ alone, and the *Grad–Shafranov equation* is
$$\Delta^* \psi = -\mu_0 R^2 \frac{dp}{d\psi} - F \frac{dF}{d\psi}, \qquad \text{where } \Delta^* \psi = R \frac{\partial}{\partial R} \left( \frac{1}{R} \frac{\partial \psi}{\partial R} \right) + \frac{\partial^2 \psi}{\partial Z^2}.$$

## Remarks

The operator $\Delta^*$ is a second-order [[elliptic operator|B4TTNHSTRX]] away from the axis $R = 0$; the equation is nonlinear when $p$ or $F$ is not affine in $\psi$.
Example, vacuum field: $\psi = R^2$ gives $\Delta^* \psi = R \partial_R (2) = 0$, and $\mathbf{B} = (1/R) (2R \, \mathbf{e}_R) \times \mathbf{e}_\varphi = 2 \mathbf{e}_Z$, a uniform field with $p$ and $F$ constant.
Example with pressure: if $dp/d\psi = c$ is constant and $F$ is constant, then $\psi = -\mu_0 c R^4 / 8$ is a solution, since $\Delta^* R^4 = R \partial_R (4 R^2) = 8 R^2$.
Adding solutions of $\Delta^* \psi = 0$ to such particular solutions gives the Solov'ev family of equilibria.
Non-example: a stellarator equilibrium depends on $\varphi$, so it is not described by this equation.
