---
tag: EVS4JPEE45
kind: concept
name: Fourier integral operator
msc: [35S30, 58J40]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_integral_operator
same_as:
  wikidata: Q4262191
  wikipedia: Fourier integral operator
---

## Summary

A Fourier integral operator is an operator of the form $u \mapsto \int e^{i \varphi(x, \xi)} a(x, \xi) \hat{u}(\xi) \, d\xi / (2\pi)^n$.
Here the phase $\varphi$ is homogeneous of degree one in $\xi$ and $a$ is a symbol.
The phase $x \cdot \xi$ gives the [[pseudo-differential operators|FF27N0BWTP]], and other phases move singularities along a canonical transformation of the cotangent bundle.
Solution operators of strictly hyperbolic equations, such as the wave equation, are Fourier integral operators.
The general theory was developed by Lars Hörmander.

## Explanations

### L1 human

A pseudo-differential operator can smooth or sharpen a function, but it does not move its singularities, such as jumps or kinks.
The solution of the wave equation does move them: a sharp wave front travels at the speed of light.
Fourier integral operators are the class of operators that can move singularities in a controlled way.
For example, the operator $e^{it\sqrt{-\Delta}}$, which multiplies the frequency $\xi$ by $e^{it\abs{\xi}}$, moves each singularity a distance $t$ in a direction set by its frequency.
