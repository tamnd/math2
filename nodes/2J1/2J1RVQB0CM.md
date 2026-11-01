---
tag: 2J1RVQB0CM
kind: statement
role: theorem
name: Itô's lemma
msc: [60H05, 60H10]
uses: [22735FGJV6, JA95NH206E, 09EGC6F8PT, X4DHMZD5JA, D48DR46B97]
about: [JA95NH206E]
sources:
  - url: https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma
same_as:
  wikidata: Q1151100
  wikipedia: Itô's lemma
---

## Statement

Let $(B_t)_{t \ge 0}$ be a [[Brownian motion|22735FGJV6]] for a filtration $(\mathcal{F}_t)$.
Let $X$ be an Itô process
$$X_t = X_0 + \int_0^t \mu_s \, ds + \int_0^t \sigma_s \, dB_s,$$
where the second integral is an [[Itô integral|JA95NH206E]].
The processes $\mu$ and $\sigma$ are progressively measurable with $\int_0^t (\abs{\mu_s} + \sigma_s^2) \, ds < \infty$ almost surely for every $t$.
Let $f \colon [0, \infty) \times \R \to \R$ be once continuously differentiable in $t$ and twice continuously differentiable in $x$.
Then, almost surely, for all $t \ge 0$,
$$f(t, X_t) = f(0, X_0) + \int_0^t \left( \partial_t f + \mu_s \, \partial_x f + \tfrac12 \sigma_s^2 \, \partial_{xx} f \right)(s, X_s) \, ds + \int_0^t \sigma_s \, \partial_x f(s, X_s) \, dB_s.$$
Here $\partial_t$, $\partial_x$ and $\partial_{xx}$ are [[partial derivatives|09EGC6F8PT]].

## Remarks

The proof expands $f$ by Taylor's formula to second order over a fine partition of $[0, t]$.
The sums of $(\Delta X)^2$ converge to $\int \sigma_s^2 \, ds$, the [[quadratic variation|X4DHMZD5JA]] of $X$, while higher-order terms vanish in the limit.
In differential form, $df = \partial_t f \, dt + \partial_x f \, dX + \tfrac12 \partial_{xx} f \, (dX)^2$ with the rules $(dB)^2 = dt$ and $dt \, dB = (dt)^2 = 0$.
Example: for $f(x) = x^2$ and $X = B$ with $B_0 = 0$, it gives $B_t^2 = 2 \int_0^t B_s \, dB_s + t$.
Example: for [[geometric Brownian motion|D48DR46B97]] $dS = \mu S \, dt + \sigma S \, dB$ with constants $\mu, \sigma$ and $S_0 > 0$, the function $\log$ gives $\log S_t = \log S_0 + (\mu - \tfrac12 \sigma^2) t + \sigma B_t$.
The $C^2$ hypothesis matters: for $f(x) = \abs{x}$ the formula needs an extra local time term, which is [[Tanaka's formula|GEM0ERJ5ZB]].

## Explanations

### L1 human

Itô's lemma is the chain rule for functions of a random process driven by Brownian motion.
Compared with the ordinary chain rule, it has one more term, half the second derivative times the squared noise intensity.
This term appears because a Brownian path moves by about $\sqrt{dt}$ in time $dt$, so squares of its moves do not vanish.

### L2 human

The lemma is the main computational tool of stochastic calculus.
It solves linear stochastic differential equations, such as those for geometric Brownian motion and the Ornstein–Uhlenbeck process.
It links expectations of diffusions to partial differential equations, as in the Kolmogorov backward equation and the Feynman–Kac formula.
The multidimensional and semimartingale versions have the same shape, with the quadratic covariations $d[X^i, X^j]$ in the second-order term.
