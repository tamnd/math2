---
tag: 2EM3EQEX2J
kind: definition
name: Catastrophe theory
msc: [58K35, 37G10]
defines: 6FKJ6SXP3G
uses: [42V5XGZS4F, 0YTCMFB4HC, 0V33BNKZ9S, KPQ96640ZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Catastrophe_theory
---

## Definition

Let $V \colon \R^n \times \R^k \to \R$ be a [[smooth function|0V33BNKZ9S]], written $V(x, c)$, with state variables $x$ and control parameters $c$.
The *catastrophe manifold* is the set $M = \set{(x, c) : \nabla_x V(x, c) = 0}$ of [[critical points|0YTCMFB4HC]] of the functions $V(\cdot, c)$.
The *catastrophe map* is the projection $\chi \colon M \to \R^k$, $(x, c) \mapsto c$.
The *bifurcation set* is the set of $c$ for which $V(\cdot, c)$ has a degenerate critical point, one where the Hessian in $x$ is singular.
*Catastrophe theory* studies these sets and the local forms of such families up to smooth changes of coordinates.

## Remarks

Example: the cusp catastrophe $V(x, a, b) = x^4/4 + a x^2/2 + b x$ with $n = 1$ and $k = 2$.
The critical points solve $x^3 + a x + b = 0$, and they are degenerate when also $3x^2 + a = 0$.
Eliminating $x$ gives the bifurcation set $4a^3 + 27b^2 = 0$, a curve with a cusp at the origin.
Inside the cusp, where $4a^3 + 27b^2 < 0$, the function has two local minima, and outside it has one.
Non-example: $V(x, c) = x^2 + c x$ has the single critical point $x = -c/2$, which is nondegenerate for every $c$, so its bifurcation set is empty.
Away from the bifurcation set every $V(\cdot, c)$ is a [[Morse function|KPQ96640ZJ]] near its critical points, so the theory is about the degenerate points.
Thom's theorem lists the seven generic local forms for $k \le 4$: fold, cusp, swallowtail, butterfly, and the hyperbolic, elliptic and parabolic umbilics.
