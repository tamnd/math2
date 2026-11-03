---
tag: WR0F7AJZVD
kind: statement
role: proposition
name: Prandtl–Glauert transformation
msc: [76G25, 76N15]
uses: [FJC2GMVARF, GFHJ858AN1, 84K7TEWZ2Z, S8RG6N1PRT, EYCZ9SGBND]
about: [FJC2GMVARF]
sources:
  - url: https://en.wikipedia.org/wiki/Prandtl%E2%80%93Glauert_transformation
same_as:
  wikidata: Q828112
  wikipedia: Prandtl–Glauert transformation
---

## Statement

Consider a steady, plane, inviscid, irrotational and isentropic [[compressible flow|FJC2GMVARF]] past a thin airfoil.
The airfoil is $y = h_\pm(x)$, $0 \le x \le c$, and the uniform stream has speed $U$ along the $x$-axis.
Assume the free stream [[Mach number|GFHJ858AN1]] satisfies $M_\infty < 1$, and set $\beta = \sqrt{1 - M_\infty^2}$.
Assume the disturbance is small.
In the linearised theory the perturbation potential $\varphi$ solves
$$\beta^2 \varphi_{xx} + \varphi_{yy} = 0, \qquad \varphi_y(x, 0^\pm) = U h_\pm'(x) \text{ for } 0 < x < c.$$
Also $\nabla\varphi \to 0$ at infinity, and the pressure coefficient is $C_p = -2\varphi_x / U$.
Then $\varphi(x, y) = \beta^{-1} \Phi(x, \beta y)$, where $\Phi$ is the perturbation potential of the incompressible [[potential flow|84K7TEWZ2Z]] past the same airfoil.
The function $\Phi$ solves [[Laplace's equation|S8RG6N1PRT]] with the same boundary conditions.
Let $C_{p,0}$ be the pressure coefficient of the incompressible flow.
Consequently, at each point of the airfoil,
$$C_p = \frac{C_{p,0}}{\sqrt{1 - M_\infty^2}}.$$
The lift coefficient obeys the same rule $c_l = c_{l,0} / \sqrt{1 - M_\infty^2}$.

## Remarks

The proof is a direct substitution.
If $\varphi(x, y) = \beta^{-1}\Phi(x, \beta y)$, then $\beta^2\varphi_{xx} + \varphi_{yy} = \beta(\Phi_{xx} + \Phi_{\eta\eta})$ with $\eta = \beta y$, and $\varphi_y(x, 0^\pm) = \Phi_\eta(x, 0^\pm)$, so the boundary conditions are unchanged.
Then $\varphi_x = \beta^{-1}\Phi_x$ on the airfoil, which gives the rule for $C_p$.
For example, a [[thin airfoil|EYCZ9SGBND]] at small angle $\alpha$ has $c_l = 2\pi\alpha / \sqrt{1 - M_\infty^2}$, so at $M_\infty = 0.6$ its lift is $1.25$ times the incompressible value.
The hypothesis $M_\infty < 1$ is needed: as $M_\infty \to 1$ the factor blows up, and the linearised equation stops being valid because the neglected nonlinear terms become important in transonic flow.

## Explanations

### L1 human

At low speed air behaves almost like an incompressible fluid, and the flow around a wing is well understood.
As the speed approaches the speed of sound, the air is squeezed more and the pressures on the wing grow.
The Prandtl–Glauert rule says that, for a thin wing, all pressures and the lift are simply multiplied by the factor $1/\sqrt{1 - M^2}$.
So one can use incompressible results and correct them for compressibility with one number.

### L2 human

The transformation stretches one coordinate by $\beta$ so that the linearised subsonic potential equation becomes Laplace's equation.
It reduces subsonic thin airfoil problems to incompressible ones, and in three dimensions a similar stretching relates a wing to an affinely distorted incompressible wing.
Its failure near $M_\infty = 1$ motivates the transonic small disturbance equation, which keeps the leading nonlinear term.
For $M_\infty > 1$ the same linear equation becomes hyperbolic, and the analogous factor is $1/\sqrt{M_\infty^2 - 1}$.
