---
tag: 1RGPVZXVD9
kind: definition
name: Flux limiter
msc: [65M08, 35L65]
defines: NZ8XFNCKQW
uses: [8RA7AMWSAF, MTCRZC5QKT, YHZ9BCNDRZ, NX8RE9B72A]
sources:
  - url: https://en.wikipedia.org/wiki/Flux_limiter
---

## Definition

Consider a scalar [[conservation law|8RA7AMWSAF]] $u_t + f(u)_x = 0$ and a conservative scheme $u_j^{n+1} = u_j^n - \lambda (F_{j+1/2} - F_{j-1/2})$ with $\lambda = \Delta t / \Delta x$.
Let $F^L_{j+1/2}$ be a low-order numerical flux, such as that of the [[upwind scheme|MTCRZC5QKT]].
Let $F^H_{j+1/2}$ be a high-order one, such as that of the [[Lax–Wendroff method|YHZ9BCNDRZ]].
For flow from left to right, the smoothness ratio at $j$ is
$$r_j = \frac{u_j^n - u_{j-1}^n}{u_{j+1}^n - u_j^n},$$
with a fixed convention when the denominator is zero.
A *flux limiter* is a function $\varphi \colon \R \to [0, \infty)$ with $\varphi(r) = 0$ for $r \le 0$, used to define the limited flux
$$F_{j+1/2} = F^L_{j+1/2} + \varphi(r_j) \left( F^H_{j+1/2} - F^L_{j+1/2} \right).$$

## Remarks

Take $u_t + a u_x = 0$ with $a > 0$ and $0 \le \nu \le 1$, with upwind and Lax–Wendroff fluxes.
Then Sweby's condition
$$0 \le \varphi(r) \le \min(2r, 2) \quad \text{for } r > 0$$
makes the scheme [[total variation diminishing|NX8RE9B72A]].
If moreover $\varphi(1) = 1$ and $\varphi$ is Lipschitz near $1$, the scheme is second-order accurate in smooth monotone regions.
Example: the minmod limiter $\varphi(r) = \max(0, \min(1, r))$ vanishes for $r \le 0$, satisfies $\varphi(r) \le \min(r, 1) \le \min(2r, 2)$ for $r > 0$, and $\varphi(1) = 1$.
Other standard limiters are superbee $\varphi(r) = \max(0, \min(2r, 1), \min(r, 2))$ and van Leer $\varphi(r) = (r + \abs{r}) / (1 + \abs{r})$.
Non-example: the constant function $\varphi \equiv 1$ is not a flux limiter, because $\varphi(r) \ne 0$ for $r \le 0$; it gives back the unlimited Lax–Wendroff scheme, which is not TVD.
At extrema $r_j \le 0$, so the scheme reduces to the low-order scheme there.

## Explanations

### L1 human

The limiter is a dial between $0$ (use only the safe low-order flux) and about $1$ or $2$ (use the high-order correction fully or more).
Its setting at each point depends on how smooth the solution looks there.
