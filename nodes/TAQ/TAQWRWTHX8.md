---
tag: TAQWRWTHX8
kind: definition
name: Langevin equation
msc: [60H10, 82C31]
defines: ZW2RBS9VTR
uses: [22735FGJV6, HZM2ASCDY4, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Langevin_equation
---

## Definition

Let $d \ge 1$, let $m > 0$ be a mass, let $\gamma > 0$ be a friction coefficient, and let $\beta > 0$ be an inverse temperature.
Let $U \colon \R^d \to \R$ be a continuously differentiable potential, and let $B$ be a $d$-dimensional [[Brownian motion|22735FGJV6]].
The *Langevin equation* is the system of stochastic differential equations for a position $X_t$ and a velocity $V_t$ in $\R^d$:
$$dX_t = V_t \, dt, \qquad m \, dV_t = -\nabla U(X_t) \, dt - \gamma V_t \, dt + \sqrt{2\gamma / \beta} \, dB_t.$$

## Remarks

In physics notation, $\beta = 1 / (k_B T)$ for the temperature $T$ and the Boltzmann constant $k_B$.
The equation is often written $m \ddot{X} = -\nabla U(X) - \gamma \dot{X} + \xi$, where $\xi$ is white noise.
Example: for $U = 0$ and $d = 1$, the velocity solves $dV = -(\gamma/m) V \, dt + (\sqrt{2\gamma/\beta}/m) \, dB$.
This is an [[Ornstein–Uhlenbeck process|HZM2ASCDY4]], and its stationary law is [[normal|05AQE0QR0D]] with mean $0$ and variance $1/(\beta m)$.
Non-example: the equation $m \, dV = -\gamma V \, dt$ lacks the random force, so its solutions decay to $0$ and never reach thermal equilibrium.
The overdamped Langevin equation $dX_t = -\nabla U(X_t) \, dt + \sqrt{2/\beta} \, dB_t$ is the limit of large friction after a change of time scale.
When $e^{-\beta U}$ is integrable, the overdamped equation has a stationary law with density proportional to $e^{-\beta U(x)}$.
Under the same condition, the full equation has a stationary law with density proportional to $e^{-\beta (U(x) + m \abs{v}^2 / 2)}$ in $(x, v)$.
