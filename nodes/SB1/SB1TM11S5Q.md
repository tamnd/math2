---
tag: SB1TM11S5Q
kind: definition
name: MUSCL scheme
msc: [65M08, 35L65]
defines: W7QH1BPBS8
uses: [8RA7AMWSAF, HGKN8E09RS, NZ8XFNCKQW, ZY4GY93C4B]
sources:
  - url: https://en.wikipedia.org/wiki/MUSCL_scheme
---

## Definition

Let $f \colon \R \to \R$ be a $C^1$ function and consider the [[conservation law|8RA7AMWSAF]] $u_t + f(u)_x = 0$.
Take a uniform grid of cells $[x_{i-1/2}, x_{i+1/2}]$ of width $\Delta x$, and let $u_i(t)$ be the cell averages of a [[finite volume method|HGKN8E09RS]].
Let $H \colon \R^2 \to \R$ be a numerical flux, for example one given by a [[Riemann solver|ZY4GY93C4B]], with $H(v, v) = f(v)$ for all $v$.
Let $\phi \colon \R \to \R$ be a [[flux limiter|NZ8XFNCKQW]] with $\phi(r) = 0$ for $r \le 0$.
A *MUSCL scheme* is the semi-discrete scheme built in three steps.

1. Slope ratio: $r_i = \dfrac{u_i - u_{i-1}}{u_{i+1} - u_i}$, with $\phi(r_i)$ read as $0$ when $u_{i+1} = u_i$.
2. Limited reconstruction at each interface:
$$u^L_{i+1/2} = u_i + \tfrac{1}{2} \phi(r_i) (u_{i+1} - u_i), \qquad u^R_{i+1/2} = u_{i+1} - \tfrac{1}{2} \phi(r_{i+1}) (u_{i+2} - u_{i+1}).$$
3. Flux update:
$$\frac{d u_i}{dt} = -\frac{1}{\Delta x} \Big( H(u^L_{i+1/2}, u^R_{i+1/2}) - H(u^L_{i-1/2}, u^R_{i-1/2}) \Big).$$

The system of ordinary differential equations is then advanced in time, for example by a Runge–Kutta method.

## Remarks

Example: take the minmod limiter $\phi(r) = \max(0, \min(1, r))$.
For linear data $u_j = j \Delta x$ one gets $r_i = 1$ and $\phi(r_i) = 1$, so $u^L_{i+1/2} = u_i + \tfrac12 \Delta x$, the exact interface value.
For step data $u_{i-1} = u_i = 0$ and $u_{i+1} = u_{i+2} = 1$ one gets $r_i = 0$, so $u^L_{i+1/2} = u_i = 0$ and no overshoot appears.

Non-example: the choice $\phi \equiv 1$ fails the condition $\phi(r) = 0$ for $r \le 0$.
It gives unlimited central slopes, and the resulting scheme creates oscillations near discontinuities.

With $\phi \equiv 0$ the reconstruction is constant and the scheme reduces to a first-order scheme of Godunov type.
