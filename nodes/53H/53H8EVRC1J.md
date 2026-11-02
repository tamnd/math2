---
tag: 53H8EVRC1J
kind: definition
name: Lax–Friedrichs method
msc: [65M06, 65M08, 35L65]
defines: VY3J2NKGKW
uses: [8RA7AMWSAF, X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Lax%E2%80%93Friedrichs_method
---

## Definition

Let $F \colon \R^m \to \R^m$ be continuous, and consider the [[conservation law|8RA7AMWSAF]] $u_t + F(u)_x = 0$ for $u \colon \R \times [0, \infty) \to \R^m$.
Fix $\Delta x > 0$ and $\Delta t > 0$, and put $\lambda = \Delta t / \Delta x$.
Let $u_j^n$ denote the approximation of $u$ at $x_j = j \Delta x$ and $t_n = n \Delta t$.
The *Lax–Friedrichs method* is the explicit scheme
$$u_j^{n+1} = \frac{u_{j+1}^n + u_{j-1}^n}{2} - \frac{\lambda}{2} \left( F(u_{j+1}^n) - F(u_{j-1}^n) \right), \qquad j \in \Z,\ n \ge 0.$$

## Remarks

It is in conservation form $u_j^{n+1} = u_j^n - \lambda \left( G_{j+1/2} - G_{j-1/2} \right)$ with the numerical flux
$$G_{j+1/2} = \frac{F(u_j^n) + F(u_{j+1}^n)}{2} - \frac{u_{j+1}^n - u_j^n}{2 \lambda}.$$
Its truncation error is of first order in $\Delta x$ when $\lambda$ is fixed.

Example: for $u_t + a u_x = 0$ with $a \in \R$, the scheme reads $u_j^{n+1} = \frac{1 - a\lambda}{2} u_{j+1}^n + \frac{1 + a\lambda}{2} u_{j-1}^n$.
If $\abs{a} \lambda \le 1$, both weights lie in $[0, 1]$ and sum to $1$.
So $\max_j \abs{u_j^{n+1}} \le \max_j \abs{u_j^n}$, and the scheme is stable in the maximum norm.

Non-example: the forward-time centred-space scheme $u_j^{n+1} = u_j^n - \frac{\lambda}{2}(F(u_{j+1}^n) - F(u_{j-1}^n))$ differs only in the first term.
For $u_t + a u_x = 0$ with $a \ne 0$, it multiplies the Fourier mode $e^{i j \xi}$ by $1 - i a \lambda \sin \xi$, of modulus greater than $1$ when $\sin \xi \ne 0$.
So it is unstable for every $\lambda > 0$.

## Explanations

### L1 human

The update averages the two neighbours and then corrects by the flux difference across them.
The averaging is what makes the method work, at the price of some blurring of sharp fronts.
