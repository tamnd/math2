---
tag: GKFDKRHEP4
kind: definition
name: Mixed-type equation
msc: [35M10]
defines: 7WFKPAMQFG
uses: [5FC6BMM1NA, B4TTNHSTRX, 92C3S03AQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%E2%80%93Tricomi_equation
---

## Definition

Let $\Omega$ be a connected open set in $\R^n$.
Consider a linear second-order partial differential equation in $\Omega$ with real coefficients.
Its type at each point is given by the [[classification of second-order PDEs|5FC6BMM1NA]].
The equation is of *mixed type* in $\Omega$ if both conditions hold:

1. it is [[elliptic|B4TTNHSTRX]] on some nonempty open subset of $\Omega$;
2. it is [[hyperbolic|92C3S03AQZ]] on some nonempty open subset of $\Omega$.

## Remarks

Example: the Tricomi equation $u_{yy} + y \, u_{xx} = 0$ on $\Omega = \R^2$, written as $A u_{xx} + 2B u_{xy} + C u_{yy}$, has $A = y$, $B = 0$ and $C = 1$, so $AC - B^2 = y$.
It is elliptic on the open set $y > 0$ and hyperbolic on the open set $y < 0$, so it is of mixed type.
Non-example: the equation $u_{xx} + (1 + y^2) u_{yy} = 0$ has $AC - B^2 = 1 + y^2 > 0$ everywhere, so it is elliptic on all of $\R^2$ and not of mixed type.
If the coefficients are continuous, the elliptic and hyperbolic regions are open, and in a connected $\Omega$ they are separated by a closed set where the coefficient matrix is degenerate.

## Explanations

### L1 human

An equation is of mixed type when it is elliptic in some region and hyperbolic in another region of the same domain.
