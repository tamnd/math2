---
tag: GSX1KFCB65
kind: statement
role: theorem
name: Dupire's formula for local volatility
msc: [91G20, 60H30, 35Q91]
uses: [Y99MCTGZHZ, 22735FGJV6, 858BHBY2BD, 09EGC6F8PT, XNA12XG7ZK]
about: [2TYE23YVS5]
sources:
  - url: https://en.wikipedia.org/wiki/Local_volatility
---

## Statement

Let $r \ge 0$ be a constant interest rate and let $W$ be a [[Brownian motion|22735FGJV6]] under a [[risk-neutral measure|858BHBY2BD]] $Q$.
Let the asset price $S$ solve the [[stochastic differential equation|Y99MCTGZHZ]]
$$dS_t = r S_t \, dt + \sigma(S_t, t) S_t \, dW_t, \qquad S_0 > 0,$$
where $\sigma(s, t) > 0$ is a deterministic function, the *local volatility*.
For $K > 0$ and $T > 0$ let $C(K, T) = e^{-rT} E_Q[(S_T - K)^+]$ be the price of the European call with strike $K$ and maturity $T$.
Assume that $S_T$ has a density that is smooth in $(K, T)$, and that $C$ is once differentiable in $T$ and twice in $K$.
Then $C$ solves the forward equation
$$\frac{\partial C}{\partial T} = \frac{1}{2} \sigma(K, T)^2 K^2 \frac{\partial^2 C}{\partial K^2} - r K \frac{\partial C}{\partial K}.$$
Hence, wherever $\partial^2 C / \partial K^2 > 0$,
$$\sigma(K, T)^2 = \frac{\dfrac{\partial C}{\partial T} + r K \dfrac{\partial C}{\partial K}}{\dfrac{1}{2} K^2 \dfrac{\partial^2 C}{\partial K^2}}.$$

## Remarks

The proof starts from $\partial^2 C / \partial K^2 = e^{-rT} p(K, T)$, where $p(\cdot, T)$ is the density of $S_T$.
The density $p$ solves the Fokker–Planck equation of the diffusion.
Differentiating $C$ in $T$, inserting the Fokker–Planck equation and integrating by parts twice in $K$ gives the forward equation.
Example: if $\sigma(s, t) = \sigma_0$ is constant, then $C$ is the Black–Scholes price, and the formula returns $\sigma_0^2$ at every $(K, T)$.
The formula needs prices for a continuum of strikes and maturities; with finitely many quoted options one must interpolate, and the result is sensitive to the interpolation.

## Explanations

### L1 human

Option prices for many strikes and maturities show a [[volatility smile|2TYE23YVS5]], which the constant-volatility Black–Scholes model cannot produce.
A local volatility model lets the volatility depend on the current price and on time.
Dupire's formula says that there is exactly one such volatility function that matches all call prices, and it gives that function directly from the prices and their slopes.

### L2 human

Dupire's formula is the standard way to calibrate a local volatility model to an [[implied volatility|XNA12XG7ZK]] surface.
The numerator involves the calendar slope $\partial C / \partial T$ and the denominator the convexity $\partial^2 C / \partial K^2$, which is a discounted risk-neutral density.
So absence of calendar and butterfly arbitrage is what makes the right side positive.
The forward equation is the dual of the backward Black–Scholes equation: it moves in the strike and maturity variables instead of the spot and current time.
A calibrated local volatility model fits today's smile exactly, but its predictions for future smiles are often unrealistic, which is one motivation for [[stochastic volatility|2KQF3JSAQ7]] models.
