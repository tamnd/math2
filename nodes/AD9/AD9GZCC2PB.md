---
tag: AD9GZCC2PB
kind: definition
name: Linear multistep method
msc: [65L06, 65L05]
defines: BX4D85A79P
uses: [0FXDW992DS, 0JARTXX4XP, 7DBPJKYC6C]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_multistep_method
---

## Definition

Let $f \colon \R \times \R^n \to \R^n$, and consider the [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$.
Let $k \ge 1$ be an integer, let $h > 0$, let $t_j = t_0 + j h$, and write $f_j = f(t_j, y_j)$.
Let $\alpha_0, \ldots, \alpha_k$ and $\beta_0, \ldots, \beta_k$ be real numbers with $\alpha_k = 1$ and $(\alpha_0, \beta_0) \ne (0, 0)$.
The *linear $k$-step method* with these coefficients determines $y_{j+k}$ from $y_j, \ldots, y_{j+k-1}$ by
$$\sum_{i=0}^{k} \alpha_i \, y_{j+i} = h \sum_{i=0}^{k} \beta_i \, f_{j+i}, \qquad j = 0, 1, 2, \ldots$$
The method is *explicit* if $\beta_k = 0$ and *implicit* otherwise.

## Remarks

The characteristic polynomials of the method are $\rho(\zeta) = \sum_i \alpha_i \zeta^i$ and $\sigma(\zeta) = \sum_i \beta_i \zeta^i$.
The method is consistent if $\rho(1) = 0$ and $\rho'(1) = \sigma(1)$, and zero-stable if every root of $\rho$ satisfies $\abs{\zeta} \le 1$ and the roots with $\abs{\zeta} = 1$ are simple.
Dahlquist's equivalence theorem says that a consistent method converges for all smooth problems with consistent starting values if and only if it is zero-stable.
Example: the two-step Adams–Bashforth method $y_{j+2} - y_{j+1} = h \left( \frac32 f_{j+1} - \frac12 f_j \right)$ has $\rho(\zeta) = \zeta^2 - \zeta$ and $\sigma(\zeta) = \frac32 \zeta - \frac12$, so $\rho(1) = 0$ and $\rho'(1) = 1 = \sigma(1)$; it is explicit, consistent and zero-stable.
The [[Euler method|0JARTXX4XP]] is the case $k = 1$, $\alpha_0 = -1$, $\beta_0 = 1$, $\beta_1 = 0$.
Non-example: the classical fourth-order [[Runge–Kutta method|7DBPJKYC6C]] is not a linear multistep method, since its update uses values of $f$ at intermediate points that are not of the form $f_{j+i}$.
The explicit method $y_{j+2} + 4 y_{j+1} - 5 y_j = h (4 f_{j+1} + 2 f_j)$ is consistent of order $3$, but $\rho(\zeta) = (\zeta - 1)(\zeta + 5)$ has the root $-5$, so it is not zero-stable and its errors grow without bound.
