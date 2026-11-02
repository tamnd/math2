---
tag: T7E2EW2T0G
kind: concept
name: Hammerstein integral equation
msc: [45G10]
specializes: [WZ4Z26XSVC]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

A Hammerstein integral equation has the form $\varphi(x) = f(x) + \int_\Omega k(x, t)\, g(t, \varphi(t))\, dt$: a linear kernel $k$ acts on a pointwise nonlinear function of the unknown.
In operator form it is $\varphi = f + K N_g \varphi$, where $K$ is a linear integral operator and $N_g$ is the [[Nemytskii operator|W8G3AZ0DNG]] of $g$.
It is a special case of the [[Urysohn equation|WZ4Z26XSVC]].
Its split structure lets one combine linear tools, such as spectral theory of $K$, with monotone operators and fixed point theorems.
Boundary value problems $-u'' = g(x, u)$ with Dirichlet conditions become Hammerstein equations with the Green's function as kernel.

## Explanations

### L1 human

First apply a nonlinear rule to the unknown at each point, for example squaring it.
Then smear the result out with a fixed weight function and integrate.
The Hammerstein equation asks that this give back the unknown, up to a known term.
For example, on $[0, 1]$ the function $\varphi(x) = 4x$ solves $\varphi(x) = \int_0^1 x t\, \varphi(t)^2\, dt$, because $\int_0^1 x t \cdot 16 t^2\, dt = 4x$.
