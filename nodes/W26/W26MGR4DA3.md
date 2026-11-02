---
tag: W26MGR4DA3
kind: statement
role: theorem
name: Feynman–Kac formula
msc: [60H30, 35K15]
uses: [B219G9SHJA, 22735FGJV6, 1CCTH8X2FT, VP2HN86VAG, VPA41PWRR1, 2J1RVQB0CM]
about: [1CCTH8X2FT, B219G9SHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Feynman%E2%80%93Kac_formula
same_as:
  wikidata: Q1317359
  wikipedia: Feynman–Kac formula
---

## Statement

Let $T > 0$ and let $W$ be a one-dimensional [[Wiener process|22735FGJV6]].
Let $\mu, \sigma \colon \R \times [0, T] \to \R$ be continuous and Lipschitz in $x$ with linear growth, uniformly in $t$.
For $(x, t) \in \R \times [0, T)$, let $X^{x,t}$ be the solution of the [[stochastic differential equation|B219G9SHJA]]
$$dX_s = \mu(X_s, s)\, ds + \sigma(X_s, s)\, dW_s, \quad s \ge t, \qquad X_t = x.$$
Let $V \colon \R \times [0, T] \to [0, \infty)$ be continuous, and let $f \colon \R \times [0, T] \to \R$ and $\psi \colon \R \to \R$ be continuous with polynomial growth in $x$.
Let $u \colon \R \times [0, T] \to \R$ be continuous, of class $C^{2,1}$ on $\R \times [0, T)$, of polynomial growth in $x$ uniformly in $t$, and a solution of the [[parabolic problem|1CCTH8X2FT]]
$$u_t + \mu\, u_x + \frac{1}{2}\sigma^2 u_{xx} - V u + f = 0 \ \text{ on } \R \times [0, T), \qquad u(x, T) = \psi(x).$$
Then for all $(x, t) \in \R \times [0, T]$,
$$u(x, t) = \mathbb{E}\Big[ \int_t^T e^{-\int_t^r V(X_\tau, \tau)\, d\tau} f(X_r, r)\, dr + e^{-\int_t^T V(X_\tau, \tau)\, d\tau}\, \psi(X_T) \Big],$$
where $X = X^{x,t}$.

## Remarks

The proof applies [[Itô's formula|2J1RVQB0CM]] to $Y_s = e^{-\int_t^s V(X_\tau, \tau) d\tau} u(X_s, s)$.
By the equation for $u$, the drift of $Y_s$ equals $-e^{-\int_t^s V d\tau} f(X_s, s)$, so $Y_s$ plus the integral of this term is a local martingale.
The growth conditions and the moment bounds for $X$ make it a true martingale, after a localization by stopping times.
Taking expectations between $s = t$ and $s = T$ gives the formula.
Example: with $\mu = 0$, $\sigma = 1$, $V = f = 0$, the formula says that the solution of the backward [[heat equation|VP2HN86VAG]] $u_t + \frac{1}{2}u_{xx} = 0$ with $u(\cdot, T) = \psi$ is $u(x, t) = \mathbb{E}[\psi(x + W_{T} - W_t)]$, a Gaussian average of $\psi$.
Without a growth condition on $u$ the conclusion can fail, because the heat equation has nonzero solutions with zero data that grow very fast in $x$.
The same formula holds in $\R^n$ with $\frac{1}{2}\sum_{i,j} (\sigma\sigma^T)_{ij}\, \partial_{x_i}\partial_{x_j}$ in place of $\frac{1}{2}\sigma^2 \partial_x^2$.

## Explanations

### L1 human

The Feynman–Kac formula says that the solution of a certain parabolic equation is an average over random paths.
Start a random walker at the point $x$ at time $t$, let it wander until time $T$, and record a reward collected along the way and at the end.
The average reward is the value $u(x, t)$.
This lets one compute solutions of equations by simulating random paths, and it lets one study random paths by solving equations.

### L2 human

The formula is the bridge between [[stochastic differential equations|B219G9SHJA]] and second-order parabolic equations.
The operator $\mu \partial_x + \frac{1}{2}\sigma^2 \partial_x^2$ is the [[infinitesimal generator|VPA41PWRR1]] of the diffusion $X$, and the potential $V$ acts as a killing rate.
In finance it gives the risk-neutral pricing formula: the Black–Scholes equation is a special case with $V = r$ constant.
The dual statement, for the density of $X$ rather than for expectations, is the Fokker–Planck equation.
Its proof is the standard use of Itô's formula together with the optional stopping theorem.
