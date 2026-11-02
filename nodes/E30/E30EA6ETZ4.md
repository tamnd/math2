---
tag: E30EA6ETZ4
kind: concept
name: Singular integral equation
msc: ["45E05", "45E99"]
specializes: [R3SG1SN7JQ]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral
---

## Summary

A singular integral equation is an [[integral equation|R3SG1SN7JQ]] whose kernel has a strong singularity.
The integral does not converge absolutely, and it is taken as a [[Cauchy principal value|0SYR10HD4R]].
The main case is the one-dimensional equation on a curve with the Cauchy kernel $1/(\tau - t)$.
Its integral operator is not compact, so the Fredholm theory does not apply directly.
Instead, the theory of Noether, Muskhelishvili and others gives an index that measures the failure of the Fredholm alternative.
Such equations arise in elasticity, aerodynamics, fracture mechanics and boundary value problems for holomorphic functions.

## Explanations

### L1 human

In an ordinary integral equation, the kernel stays bounded or blows up mildly, so the integral makes sense as it is.
In a singular integral equation, the kernel blows up like $1/(\tau - t)$ at the point $t$ of evaluation, which is too strong.
The integral only makes sense by cutting out a small symmetric piece around $t$ and letting it shrink, so that the positive and negative parts cancel.
For example, on the real line, $\frac{1}{\pi} \, \mathrm{p.v.} \int \frac{\varphi(\tau)}{t - \tau} \, d\tau = g(t)$ asks for the function whose [[Hilbert transform|NSCEBXM7ZM]] is $g$.
