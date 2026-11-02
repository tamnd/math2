---
tag: F6GKG7T6Y8
kind: definition
name: Sine-Gordon equation
msc: [35Q53, 35Q51]
defines: 802QSF9NM3
uses: [GC5BDZ6QBC, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Sine-Gordon_equation
---

## Definition

The *sine-Gordon equation* is the [[partial differential equation|GC5BDZ6QBC]]
$$u_{tt} - u_{xx} + \sin u = 0$$
for an unknown real function $u(x, t)$ of $x \in \R$ and $t \in \R$, where subscripts denote [[partial derivatives|09EGC6F8PT]].

## Remarks

Example: the static kink $u(x,t) = 4 \arctan(e^x)$ is a solution.
Put $\theta = \arctan(e^x)$; then $\sin 2\theta = \mathrm{sech}\, x$ and $\cos 2\theta = -\tanh x$.
So $\sin u = \sin 4\theta = -2\, \mathrm{sech}\, x \tanh x$.
Also $u_x = 2\, \mathrm{sech}\, x$, so $u_{xx} = -2\, \mathrm{sech}\, x \tanh x = \sin u$, and $u_{tt} = 0$.
For $\abs{v} < 1$, the moving kink $4 \arctan\!\big(\exp\big((x - vt)/\sqrt{1 - v^2}\big)\big)$ is also a solution, by Lorentz invariance.

Non-example: $u(x,t) = x$ is not a solution, because $u_{tt} - u_{xx} + \sin u = \sin x$ is not identically $0$.

In the coordinates $\xi = (x+t)/2$ and $\eta = (x-t)/2$ the equation becomes $u_{\xi\eta} = \sin u$.
This is the form in which it arises for surfaces of Gaussian curvature $-1$.
