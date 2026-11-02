---
tag: XJMYGY0ZZF
kind: concept
name: p-Laplacian
msc: [35J92, 35J70]
sources:
  - url: https://en.wikipedia.org/wiki/P-Laplacian
same_as:
  wikidata: Q7116898
  wikipedia: P-Laplacian
---

## Summary

The $p$-Laplacian is the nonlinear operator $\Delta_p u = \operatorname{div}(\abs{\nabla u}^{p-2} \nabla u)$, for a real number $1 < p < \infty$.
For $p = 2$ it is the ordinary [[Laplacian|0E0B6RA8K0]].
It is the Euler–Lagrange operator of the energy $\int \abs{\nabla u}^p \, dx$, just as the Laplacian is for $\int \abs{\nabla u}^2 \, dx$.
It is the model of a quasilinear elliptic operator that degenerates where $\nabla u = 0$ for $p > 2$ and becomes singular there for $p < 2$.

## Explanations

### L1 human

The Laplacian measures how a function differs from its averages, with all slopes treated alike.
The $p$-Laplacian gives more weight to steep slopes when $p > 2$ and less weight when $p < 2$.
Functions with $\Delta_p u = 0$, called $p$-harmonic functions, minimize the total amount of $\abs{\nabla u}^p$ for given boundary values.
Every affine function $u(x) = a \cdot x + b$ is $p$-harmonic, because its gradient is constant and so the divergence vanishes.
