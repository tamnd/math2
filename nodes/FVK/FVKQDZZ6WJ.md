---
tag: FVKQDZZ6WJ
kind: definition
name: Transonic small disturbance equation
msc: [76H05, 35M10]
defines: ZHPZ1E4PXV
uses: [20G6N8JGEH, GFHJ858AN1, 84K7TEWZ2Z, PV8DQ41Q55, 7WFKPAMQFG, 21DD2334NR, WR0F7AJZVD]
sources:
  - url: https://en.wikipedia.org/wiki/Transonic
---

## Definition

Consider a steady, plane, inviscid and irrotational flow of an ideal gas past a thin body.
The free stream is uniform, with speed $U$ along the $x$-axis.
Let $M_\infty$ be the free stream [[Mach number|GFHJ858AN1]] and $\gamma$ the ratio of specific heats.
Write the velocity as $(U + \varphi_x, \varphi_y)$, where $\varphi(x, y)$ is the perturbation [[potential|84K7TEWZ2Z]].
The *transonic small disturbance equation* is the [[partial differential equation|PV8DQ41Q55]]
$$\left(1 - M_\infty^2 - (\gamma + 1) M_\infty^2 \frac{\varphi_x}{U}\right)\varphi_{xx} + \varphi_{yy} = 0.$$

## Remarks

The equation is of [[mixed type|7WFKPAMQFG]]: it is elliptic where $1 - M_\infty^2 - (\gamma + 1) M_\infty^2 \varphi_x / U > 0$, which corresponds to locally subsonic flow, and hyperbolic where this quantity is negative.
Example: if $M_\infty < 1$ and $\varphi_x / U$ is negligible next to $1 - M_\infty^2$, the equation reduces to the linear equation $(1 - M_\infty^2)\varphi_{xx} + \varphi_{yy} = 0$ of the [[Prandtl–Glauert transformation|WR0F7AJZVD]].
Non-example: that linear equation is not a transonic small disturbance equation, because it lacks the term $\varphi_x \varphi_{xx}$, and so it cannot change type or describe a sonic line.
Its linear analogue of mixed type is the [[Tricomi equation|21DD2334NR]] $y\, u_{xx} + u_{yy} = 0$.
Solutions with shocks are understood as weak solutions of the conservation form $\partial_x\bigl((1 - M_\infty^2)\varphi_x - \frac{\gamma + 1}{2U} M_\infty^2 \varphi_x^2\bigr) + \partial_y \varphi_y = 0$.
