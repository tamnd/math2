---
tag: HV003CB8EP
kind: example
name: Umbilic catastrophes
msc: [58K35, 58K05]
illustrates: [6FKJ6SXP3G, 23RVD8K8RB]
uses: [6FKJ6SXP3G, 0YTCMFB4HC, 0693Y2METT, JV45S0KQE6]
sources:
  - url: https://en.wikipedia.org/wiki/Catastrophe_theory
---

## Example

The *umbilic catastrophes* are the three elementary catastrophes with two state variables $(x, y) \in \R^2$.
In their standard forms they are:

1. the *hyperbolic umbilic* $V = x^3 + y^3 + a xy + b x + c y$, with controls $(a, b, c) \in \R^3$;
2. the *elliptic umbilic* $V = \tfrac{1}{3}x^3 - x y^2 + a(x^2 + y^2) + b x + c y$, with controls $(a, b, c) \in \R^3$;
3. the *parabolic umbilic* $V = x^2 y + y^4 + a x^2 + b y^2 + c x + d y$, with controls $(a, b, c, d) \in \R^4$.

When all controls vanish, each $V$ has a [[critical point|0YTCMFB4HC]] at the origin where the whole [[Hessian matrix|0693Y2METT]] is zero.
For the hyperbolic umbilic, the Hessian of $x^3 + y^3$ is $\begin{pmatrix} 6x & 0 \\ 0 & 6y \end{pmatrix}$, which is $0$ at the origin.
For the elliptic umbilic, the Hessian of $\tfrac13 x^3 - x y^2$ is $\begin{pmatrix} 2x & -2y \\ -2y & -2x \end{pmatrix}$, again $0$ at the origin.
For the parabolic umbilic, the Hessian of $x^2 y + y^4$ is $\begin{pmatrix} 2y & 2x \\ 2x & 12y^2 \end{pmatrix}$, again $0$ at the origin.
So the degeneracy has corank $2$: no change of coordinates can split off a nondegenerate square in one of the variables.
This separates the umbilics from the fold, cusp, swallowtail and butterfly, which have corank $1$ and need only one state variable.

For the elliptic umbilic, the slices $a = \text{const} \ne 0$ of the [[bifurcation set|JV45S0KQE6]] are curves with three cusps.

## Explanations

### L1 human

The fold, cusp, swallowtail and butterfly describe a ball rolling along a line.
The umbilics describe a ball rolling on a surface, so the potential has two state variables.
At the most degenerate setting the surface is flat to second order in every direction, like the monkey saddle $\tfrac13 x^3 - x y^2$ of the elliptic umbilic.
Small changes of the controls break this point into several ordinary critical points, in a few typical patterns.
Thom's list of seven elementary catastrophes contains exactly three of these: the hyperbolic, elliptic and parabolic umbilics.
