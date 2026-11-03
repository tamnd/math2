---
tag: G5Y0ECEW5K
kind: statement
role: theorem
name: Green–Kubo relations
msc: [82C70, 82C05, 60G10]
uses: [DT0QXJE705, YCZHYY8VE5]
about: [YCZHYY8VE5]
sources:
  - url: https://en.wikipedia.org/wiki/Green–Kubo_relations
same_as:
  wikidata: Q4390265
  wikipedia: Green–Kubo relations
---

## Statement

Let $(v_t)_{t \ge 0}$ be a real, square-integrable, weakly [[stationary process|DT0QXJE705]] with mean $0$, jointly measurable in time and chance.
Let $C(t) = \mathbb{E}[v_t v_0]$ be its [[autocorrelation function|YCZHYY8VE5]], and assume that $C$ is continuous.
Assume that $C$ is integrable on $[0, \infty)$.
Let $X_t = X_0 + \int_0^t v_s \, ds$ be the displacement process.
Then the diffusion coefficient exists and is given by the Green–Kubo formula
$$D := \lim_{t \to \infty} \frac{\mathbb{E}\big[(X_t - X_0)^2\big]}{2t} = \int_0^\infty C(s) \, ds.$$

## Remarks

The proof is a short computation.
By stationarity, $\mathbb{E}[(X_t - X_0)^2] = \int_0^t \int_0^t C(s - u)\, du\, ds = 2\int_0^t (t - s) C(s)\, ds$.
Dividing by $2t$ gives $\int_0^t (1 - s/t) C(s)\, ds$, which tends to $\int_0^\infty C(s)\, ds$ by dominated convergence.
For the Ornstein–Uhlenbeck velocity with $C(t) = \tfrac{k_B T}{m} e^{-\gamma t}$, the formula gives $D = k_B T/(m\gamma)$, which is the Einstein relation with mobility $1/(m\gamma)$.
The general Green–Kubo relations have the same form.
A transport coefficient equals the time integral of the equilibrium autocorrelation of the corresponding current, times a prefactor.
For the electrical conductivity of a system of volume $V$, the prefactor is $1/(V k_B T)$, applied to one component of the total current.
Without integrability of $C$ the limit can be infinite, which happens in anomalous diffusion.

## Explanations

### L1 human

A particle wanders because its velocity keeps changing at random.
If the velocity forgets its past quickly, the particle spreads like a diffusing ink drop.
The formula says that the speed of spreading is the total memory of the velocity: add up how much the velocity now is correlated with the velocity later.
The same idea gives viscosity, heat conductivity and electrical conductivity from fluctuations at equilibrium.

### L2 human

Green–Kubo relations are the time-integrated form of linear response theory.
They are how molecular dynamics simulations compute transport coefficients: one records currents in an equilibrium run and integrates their autocorrelation.
The diffusion case above is G. I. Taylor's lemma on dispersion by continuous movements, and the conductivity case follows from the Kubo formula at zero frequency.
In low dimensions the current correlations of interacting fluids can decay so slowly that the integral diverges, so a transport coefficient need not exist.
