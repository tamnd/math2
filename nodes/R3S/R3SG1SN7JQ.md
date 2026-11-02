---
tag: R3SG1SN7JQ
kind: concept
name: Integral equation
msc: [45A05, 45G10]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
same_as:
  wikidata: Q580101
  wikipedia: Integral equation
---

## Summary

An integral equation is an equation in which the unknown function appears under an integral sign.
The typical linear example is $\varphi(x) = f(x) + \lambda \int_a^b K(x, s) \varphi(s) \, ds$, where $f$ and the [[kernel|GSMBXT7FPK]] $K$ are given and $\varphi$ is unknown.
Many problems for differential equations, such as [[initial value problems|0FXDW992DS]] and [[boundary value problems|TM8VQJWGHZ]], can be rewritten as integral equations.
The integral form often needs less smoothness and suits fixed point and operator methods.

## Explanations

### L1 human

In an ordinary equation the unknown is a number; here the unknown is a whole function.
The function appears once on its own and once inside an integral, which mixes its values over a range of points.
A picture: the value of $\varphi$ at $x$ is a known value $f(x)$ plus a weighted sum, an integral, of the values of $\varphi$ over a range.
For example, $\varphi(x) = 1 + \int_0^x \varphi(s) \, ds$ has the solution $\varphi(x) = e^x$, since $1 + \int_0^x e^s \, ds = e^x$.
