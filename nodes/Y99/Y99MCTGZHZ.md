---
tag: Y99MCTGZHZ
kind: definition
name: Stochastic differential equation
msc: [60H10, 34F05]
defines: B219G9SHJA
uses: [0NFPJVJJHX, HNK1Y62G7V, YRNFE016FF, 22735FGJV6, JA95NH206E, 2J1RVQB0CM, 0AW1E6YTJY, D48DR46B97]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_differential_equation
---

## Definition

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, P)$ be a [[probability space|0NFPJVJJHX]] with a [[filtration|HNK1Y62G7V]] that satisfies the usual conditions.
Let $W = (W_t)_{t \ge 0}$ be an $m$-dimensional [[Wiener process|22735FGJV6]] with respect to this filtration.
Let $T > 0$, and let $b \colon [0, T] \times \R^n \to \R^n$ and $\sigma \colon [0, T] \times \R^n \to \R^{n \times m}$ be Borel measurable.
Let $\xi$ be an $\R^n$-valued $\mathcal{F}_0$-measurable random variable.
The *stochastic differential equation* with drift $b$, diffusion coefficient $\sigma$ and initial value $\xi$ is
$$dX_t = b(t, X_t) \, dt + \sigma(t, X_t) \, dW_t, \qquad X_0 = \xi.$$
A *strong solution* is a continuous [[adapted process|YRNFE016FF]] $X$ with values in $\R^n$ with two properties.
Almost surely, $\int_0^T \left( \abs{b(s, X_s)} + \abs{\sigma(s, X_s)}^2 \right) ds < \infty$.
Almost surely,
$$X_t = \xi + \int_0^t b(s, X_s) \, ds + \int_0^t \sigma(s, X_s) \, dW_s \quad \text{for all } t \in [0, T],$$
where the last integral is the Itô integral of [[Itô calculus|JA95NH206E]].

## Remarks

Assume that $b$ and $\sigma$ are [[Lipschitz|0AW1E6YTJY]] in $x$ uniformly in $t$ and grow at most linearly in $x$, and that $\xi$ has a finite second moment.
Then a strong solution exists and is unique up to indistinguishability.
Example: for $n = m = 1$, $b(t, x) = \mu x$ and $\sigma(t, x) = s x$ with constants $\mu, s$, the process $X_t = X_0 \exp\left( (\mu - s^2/2) t + s W_t \right)$ is a solution; [[Itô's lemma|2J1RVQB0CM]] gives $dX_t = \mu X_t \, dt + s X_t \, dW_t$.
This is [[geometric Brownian motion|D48DR46B97]].
Non-example: $Y_t = e^{W_t}$ does not solve $dY_t = Y_t \, dW_t$, $Y_0 = 1$, because Itô's lemma gives $dY_t = Y_t \, dW_t + \frac{1}{2} Y_t \, dt$, with an extra drift term.
A *weak solution* allows the probability space and the Wiener process to be constructed together with $X$.
