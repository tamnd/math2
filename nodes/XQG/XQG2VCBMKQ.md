---
tag: XQG2VCBMKQ
kind: definition
name: Hyperbolic partial differential equation
msc: [35L10, 35L25]
defines: 92C3S03AQZ
uses: [6DZETZ5T9G, F31T650DKY, B4TTNHSTRX]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_partial_differential_equation
---

## Definition

Let $U \subseteq \R^n$ be open, let $T > 0$, and write the variables in $U \times (0, T)$ as $(x, t)$.
Consider a [[linear PDE|6DZETZ5T9G]] in $U \times (0, T)$ of the following form.
$$\partial_t^2 u - \sum_{i,j=1}^{n} a_{ij}(x, t) \, \partial_i \partial_j u + \sum_{i=1}^{n} b_i(x, t) \, \partial_i u + b_0(x, t) \, \partial_t u + c(x, t) \, u = f(x, t).$$
Here all coefficients are real and $a_{ij} = a_{ji}$.
The equation is a *second-order linear hyperbolic equation* if its spatial part is [[uniformly elliptic|B4TTNHSTRX]].
That is, there is $\theta > 0$ with $\sum_{i,j} a_{ij}(x, t) \xi_i \xi_j \ge \theta \abs{\xi}^2$ for all $(x, t)$ and all $\xi \in \R^n$.

More generally, let $P$ be a linear operator of order $m$ in the variables $(x, t)$, with [[principal symbol|F31T650DKY]] $\sigma_m$.
It is *hyperbolic with respect to the time direction* at a point $y$ if both conditions hold:

1. $\sigma_m(y, (0, \dots, 0, 1)) \ne 0$;
2. for every $\xi \in \R^n$ the polynomial $\tau \mapsto \sigma_m(y, (\xi, \tau))$ has only real roots.

It is *strictly hyperbolic* if, in addition, these $m$ roots are distinct for every $\xi \ne 0$.

## Remarks

Example: the [[wave equation|5EHD2XBQDG]] $\partial_t^2 u - c^2 \Delta u = 0$ with $c > 0$ is hyperbolic with $a_{ij} = c^2 \delta_{ij}$; its symbol $\tau^2 - c^2 \abs{\xi}^2$ has the distinct real roots $\tau = \pm c \abs{\xi}$ for $\xi \ne 0$.
Non-example: the equation $\partial_t^2 u + \Delta u = 0$ is not hyperbolic; its symbol $\tau^2 + \abs{\xi}^2$ has the non-real roots $\tau = \pm i \abs{\xi}$, and the equation is elliptic.
A first-order system $\partial_t u + \sum_j A_j(x, t) \partial_j u = 0$ is called hyperbolic when every matrix $\sum_j \xi_j A_j$ with $\xi \in \R^n$ has real eigenvalues and a basis of eigenvectors; see also [[strict hyperbolicity|P3VXR8FW17]].

## Explanations

### L1 human

A hyperbolic equation is built like the wave equation: a second time derivative minus a uniformly elliptic operator in space.
