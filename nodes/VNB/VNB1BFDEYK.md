---
tag: VNB1BFDEYK
kind: definition
name: Heat equation
msc: [35K05]
defines: VP2HN86VAG
uses: [1CCTH8X2FT, 0E0B6RA8K0, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_equation
---

## Definition

Let $n \ge 1$, let $\Omega \subseteq \R^n$ be an open set, and let $T > 0$.
Let $u \colon \Omega \times (0, T) \to \R$ have one continuous [[partial derivative|09EGC6F8PT]] in $t$ and two continuous partial derivatives in $x$.
The *heat equation* on $\Omega \times (0, T)$ is the [[parabolic|1CCTH8X2FT]] equation
$$\frac{\partial u}{\partial t}(x, t) = \Delta u(x, t), \qquad x \in \Omega, \ 0 < t < T.$$
Here $\Delta = \partial_{x_1}^2 + \cdots + \partial_{x_n}^2$ is the [[Laplacian|0E0B6RA8K0]] in $x$.

## Remarks

Many authors write $\partial_t u = \alpha \Delta u$ with a constant $\alpha > 0$, the diffusivity; the change of variable $t \mapsto \alpha t$ reduces it to $\alpha = 1$.
Example: for $k > 0$, $u(x, t) = e^{-k^2 t} \sin(k x)$ solves the heat equation on $\R \times (0, \infty)$, since $\partial_t u = -k^2 u$ and $\partial_x^2 u = -k^2 u$.
Non-example: $u(x, t) = e^{k^2 t} \sin(k x)$ is not a solution, since $\partial_t u = k^2 u$ while $\partial_x^2 u = -k^2 u$; it solves the backward heat equation $\partial_t u = -\Delta u$.
The equation is usually completed by an initial condition $u(x, 0) = g(x)$ and, when $\Omega \ne \R^n$, by boundary conditions on $\partial \Omega$.
