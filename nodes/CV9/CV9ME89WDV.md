---
tag: CV9ME89WDV
kind: definition
name: Random ordinary differential equation
msc: [34F05, 37H10]
defines: RWZ5KMPD1R
uses: [0NFPJVJJHX, 0QH5ENKZM1, 0NT64JV96A, B219G9SHJA, 22735FGJV6]
sources:
  - url: https://en.wikipedia.org/wiki/Random_dynamical_system
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0NFPJVJJHX]].
Let $\eta = (\eta_t)_{t \ge 0}$ be a [[stochastic process|0QH5ENKZM1]] with values in $\R^m$ whose sample paths $t \mapsto \eta_t(\omega)$ are continuous.
Let $f \colon \R^n \times \R^m \to \R^n$ be continuous.
The *random ordinary differential equation* driven by $\eta$ with right side $f$ is the family of [[ordinary differential equations|0NT64JV96A]]
$$\frac{dx}{dt} = f(x, \eta_t(\omega)), \qquad \omega \in \Omega.$$
A *solution* is a process $(X_t)_{t \ge 0}$ such that for $P$-almost every $\omega$ the path $t \mapsto X_t(\omega)$ is continuously differentiable and solves the equation for that $\omega$.

## Remarks

For fixed $\omega$ the right side $(t, x) \mapsto f(x, \eta_t(\omega))$ is continuous, so the usual existence theory for ordinary differential equations applies path by path.
Example: with $n = m = 1$ and $f(x, y) = -x + y$, the process $X_t = e^{-t} X_0 + \int_0^t e^{-(t - s)} \eta_s \, ds$ is a solution; differentiating gives $X_t' = -X_t + \eta_t$.
Non-example: let $W$ be a [[Wiener process|22735FGJV6]].
The equation $dX_t = X_t \, dW_t$ is not a random ordinary differential equation as written, since the noise enters through $dW_t$ and the paths of $W$ are not differentiable.
A [[stochastic differential equation|B219G9SHJA]] with additive noise, $dX_t = a(X_t) \, dt + dW_t$, becomes a random ordinary differential equation after the change of variables $Z_t = X_t - W_t$: then $Z_t' = a(Z_t + W_t)$.
Some authors allow $f$ to depend on $t$ and $\eta$ to have only measurable paths; then solutions are taken in the sense of Carathéodory.
